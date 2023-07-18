# Есть N потоков. Каждый пишет m сообщений: "Hi! I'm {pid} and it is my {i}th message!". Между
# сообщениями пусть спит случайное время от (1 до 4) секунд. Все эти сообщения выводятся не на консоль,
# а в один файл (logs.txt, например). Организовать грамотный вывод


import time
import random
from threading import Thread, Lock


def write2file(pid, i, mutex: Lock, file_path):
    message = f"Hi! I'm {pid} and it is my {i}th message!\n"
    sleep_time = random.randint(1, 4)
    time.sleep(sleep_time)

    mutex.acquire()
    with open(file_path, "a") as file:
        file.write(message)
    mutex.release()


def thread_function(pid, m, mutex: Lock, file_path):

    for i in range(1, m + 1):
        write2file(pid, i, mutex, file_path)


if __name__ == '__main__':
    n, m, file_path = 4, 4, 'logs.txt'

    mutex = Lock()
    threads = []

    for pid in range(1, n + 1):

        t = Thread(target=thread_function, args=(pid, m, mutex, file_path, ))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()