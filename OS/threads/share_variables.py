# Имеется N потоков и m общих переменный (разделяемые между ними). Каждый поток работает по
# следующему принципу: пытается захватить k переменных, вычисляет их среднее, умножает на случайное
# число (от 1 до 3) и перезаписывает их значения, спит случайное время (1-5 секунд) и снова повторяет свои
# действия (делает так t раз). При всех действиях пусть пишет соответствующие сообщения (в файл).
# Реализовать эту логику.
import os
import threading
import random
import time
import multiprocessing as mp


def logger(queue, file_name):
    file = open(file_name, 'a+')
    while not queue.empty():
        try:
            msg = queue.get()
            file.write(msg)
            file.flush()
        except:
            time.sleep(0.2)

    file.close()


def thread_function(thread_id, k, t, mutex, values, q):

    for _ in range(t):
        mutex.acquire()

        indxs = [random.choice(range(len(values))) for _ in range(k)]
        nums = [values[i] for i in indxs]
        avg = sum(nums) / len(nums)
        mult = random.randint(1, 3)
        acquired_variables = [values[i] for i in indxs]
        for i in indxs:
            values[i] = avg * mult

        mutex.release()

        message = f'Thread {thread_id}: Acquired variables: {acquired_variables}, avg: {avg}, multiplied: {values}\n'
        q.put(message)

        sl_time = random.randint(1, 5)
        time.sleep(sl_time)
        print(f'Process {thread_id} will sleep for {sl_time}')


if __name__ == '__main__':
    jobs = []
    n, m, k, t = 5, 3, 2, 3
    common_vars = [random.choice([i for i in range(10)]) for _ in range(m)]
    pid = 0

    file_name = 'logs2.txt'
    if os.path.getsize(file_name) > 0:
        with open(file_name, 'w') as f:
            pass

    mutex = mp.Lock()
    manager = mp.Manager()
    q = mp.Queue()
    vars = manager.list(common_vars)

    for i in range(n):
        pid += 1
        pr = mp.Process(target=thread_function, args=(pid, k, t, mutex, vars, q,))
        pr.start()
        jobs.append(pr)

    for proc in jobs:
        proc.join()

    logger_pr = mp.Process(target=logger, args=(q, file_name,))
    logger_pr.start()
    logger_pr.join()