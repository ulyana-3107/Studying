# 2. Написать обработчик для сигнала, получаемого при завершении дочернего процесса, который будет писать
# в консоль что-то вроде "Child process {pid} was finished". Породить n потоков и проверить работу этого
# обработчика.


import threading
import subprocess
import time
import win32con
import win32event


def check_child_processes(processes):
    events = [win32event.CreateEvent(None, 0, 1, None) for _ in processes]

    for i in range(len(processes)):
        thread = threading.Thread(target=wait_for_child_process, args=(processes[i].pid, events[i]))
        thread.start()


def wait_for_child_process(pid, event):
    wait_status = win32event.WaitForSingleObject(event, -1)
    if wait_status == win32con.WAIT_OBJECT_0:
        print(f"Child process {pid} was finished")


if __name__ == "__main__":
    processes = [subprocess.Popen(["python", "-c", "import time; time.sleep(1)"]) for _ in range(5)]
    check_child_processes(processes)
