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


def distribute(n: int, files: list) -> list:

    res = [[] for _ in range(n)]
    c1, even, end = 0, True, False

    while not end:
        if not even:
            start, end, step = 0, n, 1
        else:
            start, end, step = n - 1, -1, -1

        for i in range(start, end, step):
            if c1 == len(files):
                end = True
                break
            next = files[c1]
            c1 += 1
            res[i].append(next)

        even = not even

    return res


def main(mask: str, n_procs: int,  *args):
    all = []
    for elem in args:
        all.extend(pl.Path(elem).rglob(mask))

    size_sorted = sorted(all, key=lambda file: os.path.getsize(file))
    distributed = distribute(n_procs, size_sorted)

    mutex = mp.Lock()
    manager = mp.Manager()
    db = manager.dict()
    pat = r'KEY:\[.+?\]\s+VALUE:\[.+?\]'

    processes = []

    for files_arr in distributed:
        if not len(files_arr):
            continue

        proc = mp.Process(target=find_data, args=(files_arr, pat, db))
        proc.start()
        processes.append(proc)

    for proc in processes:
        proc.join()

    procs2 = []

    sorted_texts = list(dict(sorted(db.items(), key=lambda item: len(item[1][0]))).keys())
    distributed2 = distribute(n_procs, sorted_texts)

    for arr in distributed2:
        pr = mp.Process(target=write_data, args=(arr, db))
        pr.start()
        procs2.append(pr)
        
    for pr in procs2:
        pr.join()


def find_data(files_arr: str, pat: str, db) -> None:
    for file in files_arr:
        with open(file, 'r', encoding='utf-8-sig') as reader:
            for line in reader.readlines():
                matches = re.findall(pat, line)

                for m in matches:
                    key = re.findall(r"KEY:\[(.+?)\]", m)[0]
                    value = re.findall(r"VALUE:\[(.+?)\]", m)[0]

                    if key not in db:
                        db[key] = [value]
                    else:
                        db[key].append(value)


def write_data(keys: list, db: dict) -> None:
    for k in keys:
        values = db[k]
        with open(f'{k.strip()}.txt', 'w', encoding='utf-8-sig') as vals_writer:
            for v in values:
                vals_writer.write(v.strip() + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mask', type=str, help='template for finding file')
    parser.add_argument('--proc_num', type=int, default=2, help='Max number of processes to start')
    parser.add_argument('Paths', help='paths to the folders with files', nargs='*')
    args = parser.parse_args()
    main(args.mask, args.proc_num, *args.Paths)

