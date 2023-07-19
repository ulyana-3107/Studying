# Имеется N потоков и m общих переменный (разделяемые между ними). Каждый поток работает по
# следующему принципу: пытается захватить k переменных, вычисляет их среднее, умножает на случайное
# число (от 1 до 3) и перезаписывает их значения, спит случайное время (1-5 секунд) и снова повторяет свои
# действия (делает так t раз). При всех действиях пусть пишет соответствующие сообщения (в файл).
# Реализовать эту логику.


import threading
import random
import time

file_name = 'logs2.txt'
file = open(file_name, 'w')


def thread_function(thread_id, m, k, t):
    mutex = threading.Lock()

    for _ in range(t):

        acquired_variables = random.sample(range(m), k)

        avg = sum(i for i in acquired_variables) / k
        mult = random.randint(1, 3)
        result = avg * mult

        with mutex:
            message = f'Thread {thread_id}: Acquired variables: {acquired_variables}, avg: {avg}, multiplied: {result}\n'
            file.write(message)

        time.sleep(random.randint(1, 5))

    file.flush()


if __name__ == '__main__':
    threads = []
    n, m, k, t = 5, 3, 2, 3

    for i in range(n):
        thread = threading.Thread(target=thread_function, args=(i, m, k, t))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    file.close()



