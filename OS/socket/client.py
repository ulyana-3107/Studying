import socket
from encryption import encrypt


def send_data():

    host = "127.0.0.1"
    port = 12345

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    login = input("Enter your login: ")
    client.send(login.encode())
    my_key = client.recv(1024).decode()
    print(f'key received: {my_key}')

    while True:
        message = input("Enter a message ('End Session' or 'SIGTERM' to quit): ")

        if message.upper() in ("END SESSION", "SIGTERM"):
            client.send(message.encode())
            break

        decrypted_msg = encrypt(message, my_key)
        client.send(decrypted_msg.encode())

    client.close()


if __name__ == '__main__':
    send_data()

