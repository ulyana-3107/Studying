# Подготовить скрипт: подаётся csv-файл (через cmd), где в каждой строке лежит задача на шифровку/дешифровку.
# Вид строки: file_path|output_path
# |encryption_type|encryption/decryption|key
# encryption_type - 1 (Цезарь), 2 (Ключ+сдвиг), 3 (XOR).
# Запускать для каждой задачи соответствующий python-скрипт (из задачи 1.).
# Важно: именно запускать скрипты, а не импортировать!
# То есть подготавливаешь cmd и запускаешь через subprocess.call/subprocess.run.


import subprocess
from pathlib import Path
import csv
import argparse
import time
from string import ascii_lowercase as letters


def en_or_de_crypt_texts(path: str, call_paths: list) -> None:
    if not Path(path).exists:
        raise FileExistsError()

    path1 = call_paths[0]
    path2 = call_paths[1]
    path3 = call_paths[2]

    with open(path, 'r', newline='') as csv_rd:
        reader = csv.DictReader(csv_rd)
        modes = {'e': True, 'd': False}

        for enc_data in reader:
            src_path, dst_path = enc_data['Source_path'], enc_data['Dst_path']
            enc_type, mode, key = enc_data['Enc_type'], modes[enc_data['Mode'].strip()], enc_data['Key']

            script_code = int(enc_type.strip())

            t = time.time()

            if script_code == 1:
                proc = subprocess.run(['python', eval('path' + str(script_code)), src_path, dst_path,
                                       f'--decrypt={mode}', f'--shift={key}'], capture_output=True, text=True)
            else:
                proc = subprocess.run(['python', eval('path' + str(script_code)), src_path, dst_path, key,
                                       f'--decrypt={mode}'], capture_output=True, text=True)

            t2 = time.time()

            if not proc.returncode == 0:
                print(proc.stderr)
                continue

            print(f'Time taken: {t2 - t}')


if __name__ == '__main__':
    call_paths = list()
    call_paths.append(input('Path for caesar encryption script:').strip())
    call_paths.append(input('Path for shift encryption script:').strip())
    call_paths.append(input('Path for XOR encryption script:').strip())

    parser = argparse.ArgumentParser(description='En/de_crypts data from the given csv file')
    parser.add_argument('path', type=str, help='path to the csv file')
    args = parser.parse_args()
    en_or_de_crypt_texts(args.path, call_paths)
