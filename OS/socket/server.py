# 1. Написать два скрипта: сервер и клиент (запускаются отдельно). Сервер крутится в вечном цикле и ждёт
# подключений от клиентов (их может быть несколько). При подключении ждёт от клиента сначала ждёт от
# него логин (уникальный для каждого клиента), а затем ждёт сообщения. Возвращает клиенту
# зашифрованное сообщение (методом XOR) и снова ждёт сообщений от клиента, пока не получит
# сообщение "End session". Хранит где-то у себя (файлик) информацию логин-ключ шифрования, чтобы при
# повторном подключении была возможность шифровать с тем же ключом. При появлении нового клиента
# генерирует ключ. При получении сообщения SIGTERM пишет сообщение и завершает свою работу.
# Клиент-скрипт подключается к серверу, получает от пользователя логин и сообщения, посылает их серверы
# и выводит результат на экран.


import socket
import sys
import os
import signal
import pickle
from encryption import encrypt
from string import ascii_lowercase
import random


def generate_key() -> str:
    letters = [i for i in ascii_lowercase]
    key = ''
    for i in range(random.randint(7, 10)):
        key += random.choice(letters)

    return key


def get_info(clients_file):
    if os.path.exists(clients_file) and os.path.getsize(clients_file) > 0:
        with open(clients_file, "rb") as file:
            clients = pickle.load(file)
    else:
        clients = {}

    return clients


def save_clients(clients):
    with open(clients_file, "wb") as file:
        pickle.dump(clients, file)


def handle_client(conn, addr):
    print(f"New connection from {addr}")

    clients_db = get_info(clients_file)

    client_login = conn.recv(1024).decode()

    if client_login in clients_db:
        key = clients_db[client_login]
    else:
        key = generate_key()
        clients_db[client_login] = key
        save_clients(clients_db)

    clients_db[client_login] = key

    conn.send(key.encode())
    print(f'Key sent')

    while True:
        try:
            message = conn.recv(1024).decode()

            if message.upper() in ("END SESSION", "SIGTERM"):
                break

            print(f'just got a message: {message}')
            decrypted_message = encrypt(message, key)
            print(f'Just decrypted received message - {decrypted_message}')
            conn.send(f'Received message after encryption: {message}\nMessage after decryption: {decrypted_message}'.encode())
        except KeyboardInterrupt:
            conn.send('SIGTERM'.encode())
            conn.close()

    conn.close()
    if len(clients_db):
        with open(clients_file, 'wb') as file:
            pickle.dump(clients_db, file)


def accept_data(n):
    host = "127.0.0.1"
    port = 12345

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(n)

    print(f"Server listening on {host}:{port}")

    while True:
        server.settimeout(5)
        conn, addr = server.accept()
        try:
            server.close()
            handle_client(conn, addr)

        except socket.timeout:
            print(f'Client connection timeout exceeded. Closing socket...')
            conn.close()


if __name__ == '__main__':
    clients_file = 'clients.pkl'
    n = int(input('Enter number of messages to send:'))
    accept_data(n)
