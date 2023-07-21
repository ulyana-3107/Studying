# Имеется N потоков и m общих переменный (разделяемые между ними). Каждый поток работает по
# следующему принципу: пытается захватить k переменных, вычисляет их среднее, умножает на случайное
# число (от 1 до 3) и перезаписывает их значения, спит случайное время (1-5 секунд) и снова повторяет свои
# действия (делает так t раз). При всех действиях пусть пишет соответствующие сообщения (в файл).
# Реализовать эту логику.


import threading
import random
import time
import multiprocessing as mp

file_name = 'logs2.txt'
file = open(file_name, 'w')


def thread_function(thread_id, k, t, mutex, values):
    mutex.acquire()

    for _ in range(t):

        avg = sum(values) / len(values)
        mult = random.randint(1, 3)
        indxs = [random.choice(range(len(values))) for i in range(k)]
        acquired_variables = [values[i] for i in indxs]
        for i in indxs:
            values[i] = values[i] * mult

        message = f'Thread {thread_id}: Acquired variables: {acquired_variables}, avg: {avg}, multiplied: {values}\n'
        file.write(message)

        time.sleep(random.randint(1, 5))

    mutex.release()

    file.flush()


if __name__ == '__main__':
    jobs = []
    n, m, k, t = 5, 3, 2, 3
    common_vars = [random.choice([i for i in range(10)]) for _ in range(m)]
    pid = 0

    mutex = mp.Lock()
    manager = mp.Manager()
    vars = manager.list(common_vars)

    for i in range(n):
        pid += 1
        pr = mp.Process(target=thread_function, args=(pid, k, t, mutex, vars))
        pr.start()
        pr.join()
        jobs.append(pr)

    for proc in jobs:
        proc.join()

    file.close()



