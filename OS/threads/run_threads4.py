# 4. Написать программу, которая будет порождать потомка, который будет порождать потомка и так далее
# (всего будет порождено n потомков). Каждый потомок будет ждать завершение порождённого (кроме
# последнее) и спать случайное время (от 1 до 10 секунд), а после завершаться с кодом возврата = код
# возврата ожидаемого потока (0 для последнего) + случайное число (от 1 до 100)


import multiprocessing
import random
import time
import inspect
import os


def child_process(n):
    time.sleep(random.randint(1, 10))
    par_ret_code = 0 if n == 1 else n - 1

    random_return_code = random.randint(1, 100)
    return_code = par_ret_code + random_return_code

    process_id = multiprocessing.current_process().pid
    print(f"Process {process_id} finished with return code {return_code}")

    return return_code


def main(n):
    process = None
    for i in range(n, 0, -1):
        if process is not None:
            process.join()

        process = multiprocessing.Process(target=child_process, args=(i,))
        process.start()

    process.join()


if __name__ == "__main__":
    main(3)
