# Есть N потоков. Каждый пишет m сообщений: "Hi! I'm {pid} and it is my {i}th message!". Между
# сообщениями пусть спит случайное время от (1 до 4) секунд. Все эти сообщения выводятся не на консоль,
# а в один файл (logs.txt, например). Организовать грамотный вывод.
# Реализовать эту логику через один поток логгер, который будет писать всё в файл, и остальные обычные,
# которые будут слать сообщения логгеру.
import multiprocessing
import random
import time


def write_message(pid, m, queue):
    for i in range(1, m + 1):
        time.sleep(random.randint(1, 4))
        message = f"Hi! I'm {pid} and it is my {i}th message!\n"
        queue.put(message)


def logger(queue):
    with open("my_logs.txt", "a") as file:
        while True:
            message = queue.get()
            if message == "STOP":
                break
            file.write(message)
            file.flush()


if __name__ == "__main__":
    n, m = 5, 3
    queue = multiprocessing.Queue()
    logger_process = multiprocessing.Process(target=logger, args=(queue,))
    logger_process.start()

    processes = []

    for pid in range(n):
        process = multiprocessing.Process(target=write_message, args=(pid, m, queue))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    queue.put("STOP")
    logger_process.join()