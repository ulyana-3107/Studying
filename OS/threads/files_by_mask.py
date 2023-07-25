# На вход подаётся несколько папок. Надо:
# 1. Найти все файлы, имена которых соответствуют определённой маске (подаётся через cmd)
# 2. Считать их содержимое и сохранить только те строки, которые начинаются с фразы "KEY:[VALUE],
# VALUE:[...]". Распределить VALUEs по KEY
# 3. Сохранить по файлам: для каждого KEY свой файл (KEY.txt, например)
# Учитывать, что файлы могут быть очень большими. Применить распараллеливание грамотно (чтобы
# задачи между потоками были распределены +- равномерно (особенно для 2)).
# В идеале каждый пункт будет реализован через распараллеливание. Число потоков ограничено
# параметром --proc_num.
import fnmatch
import os
import argparse
import sys
import pathlib as pl
import multiprocessing as mp
import re


def main(mask: str, n_procs: int,  *args):
    all = []
    for elem in args:
        all.extend(pl.Path(elem).rglob(mask))

    size = 0

    for elem in all:
        size += os.path.getsize(elem)

    temp_file = 'temp.txt'
    pl.Path(temp_file).touch()

    avg = size // n_procs
    mutex = mp.Lock()
    pat = r'KEY:\[.+?\]\s+VALUE:\[.+?\]'

    processes = []

    while all:
        file = all.pop()
        with open(file, 'r') as reader:
            with open(temp_file, 'a') as writer:
                text = reader.read(avg)
                text2 = reader.read()
                writer.write(text2)
                pr = mp.Process(target=find_nd_write_data, args=(text, pat, mutex,))
                pr.start()
                processes.append(pr)

    if sys.getsizeof(temp_file) != 0:
        with open(temp_file, 'r') as reader:
            text = reader.read()
            last = mp.Process(target = find_nd_write_data, args=(text, pat, mutex, ))
            last.start()
            processes.append(last)

    for proc in processes:
        proc.join()


def find_nd_write_data(text: str, pat: str, mutex) -> None:
    matches = re.findall(pat, text)
    for m in matches:
        key = re.findall(r"KEY:\[(.+?)\]", m)[0]
        value = re.findall(r"VALUE:\[(.+?)\]", m)[0]

        if pl.Path(f'{key}.txt').exists():
            mode = 'a'
        else:
            mode = 'w'

        with mutex:
            with open(f'{key}.txt', mode) as writer:
                writer.write(value + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mask', type=str, help='template for finding files')
    parser.add_argument('--proc_num', type=int, default=2, help='Max number of processes to start')
    parser.add_argument('Paths', help='paths to the folders with files', nargs='*')
    args = parser.parse_args()
    main(args.mask, args.proc_num, *args.Paths)
