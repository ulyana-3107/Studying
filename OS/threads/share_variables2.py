import random
import time
import multiprocessing as mp


class Process:
    __vars = [1, 2, 3, 4, 5]

    def __init__(self, pid, k, t, file):
        self.__dict__['vars'] = self.__vars
        self.pid = pid
        self.k, self.t = k, t
        self.file = file

    def run(self):
        for _ in range(self.t):
            avg = sum(self.__vars) / len(self.__vars)
            mult = random.randint(1, 3)
            indxs = [random.choice(range(len(self.__vars))) for _ in range(self.k)]
            acquired_variables = [self.__vars[i] for i in indxs]
            for i in indxs:
                self.__vars[i] = self.__vars[i] * mult

            message = f'Thread {self.pid}: Acquired variables: {acquired_variables}, avg: {avg}, multiplied: {self.__vars}\n'
            file.write(message)

            time.sleep(random.randint(1, 2))


def main(pid: int, k: int, t: int, file: str):
    obj = Process(pid, k, t, file)
    obj.run()


if __name__ == '__main__':
    file_name = 'logs2.txt'
    file = open(file_name, 'w')

    jobs = []
    objects = []
    n, k, t = 5, 2, 3
    pid = 0

    for i in range(n):
        pid += 1
        obj = Process(pid, k, t, file)
        objects.append(obj)

    for o in objects:
        o.run()

    file.close()





