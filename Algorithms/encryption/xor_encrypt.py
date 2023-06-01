# Шифровка через ключ, но используя XOR.
import argparse
from itertools import cycle
from string import ascii_lowercase as letters
from pathlib import Path


def read_text(path: str) -> str:
    if Path(path).exists:
        return Path(path).read_text()

    raise FileNotFoundError()


def xor_encrypt(path: str, dst_path: str,  key: str) -> None:
    if not Path(path).exists():
        raise FileExistsError()

    text = Path(path).read_text()

    text2, i = '', 0
    cycle_ = cycle([i + 1 for i in range(len(key))])

    while i < len(text):

        text2 += chr(ord(text[i]) ^ next(cycle_))

        i += 1

    if not Path(dst_path).exists():
        Path(dst_path).touch()

    with open(dst_path, 'w', encoding='utf-8-sig') as writer:
        writer.write(text2)


def decrypt_from_xor(path: str, dst_path: str, key: str) -> None:
    if not Path(path).exists():
        raise FileExistsError()

    text = Path(path).read_text()

    real_text, ind = '', len(text) - 1

    last = len(text) % len(key)
    lst = [i for i in range(last, 0, -1)]
    for i in range(len(key), last, -1):
        lst.append(i)

    cycle_ = cycle(lst)

    while ind > -1:

        elem = ord(text[ind]) ^ next(cycle_)
        real_text = chr(elem) + real_text
        ind -= 1

    if not Path(dst_path).exists():
        Path(dst_path).touch()

    with open(dst_path, 'w', encoding='utf-8-sig') as writer:
        writer.write(real_text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='XOR encryption and decryption')
    parser.add_argument('path', type=str, help='path to the file with text')
    parser.add_argument('dst_path', type=str, help='path for the en/de_crypted text to be written')
    parser.add_argument('key', type=str, help='key to encrypt given text')
    parser.add_argument('-d', '--decrypt', type=bool, default=False, help='if True, will decrypt text else encrypt')
    args = parser.parse_args()

    if args.decrypt:
        decrypt_from_xor(args.path, args.dst_path,  args.key)
    else:
        xor_encrypt(args.path, args.dst_path, args.key)
