# Шифровка через ключ, но используя XOR.
import argparse
from itertools import cycle
from string import ascii_lowercase as letters
from pathlib import Path


def read_text(path: str) -> str:
    if Path(path).exists:
        return Path(path).read_text('utf-8-sig')

    raise FileNotFoundError()


def write_encrypted_text(text: str, dst_path: str) -> None:
    if not Path(dst_path).exists():
        Path(dst_path).touch()

    with open(dst_path, 'w', encoding='utf-8-sig') as wr:
        wr.write(text)


def encrypt(text: str, key: str) -> str:
    encypted = []

    for idx in range(len(text)):
        encypted.append(chr(ord(text[idx]) ^ ord(key[idx % len(key)])))

    return "".join(encypted)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='XOR encryption and decryption')
    parser.add_argument('path', type=str, help='path to the file with text')
    parser.add_argument('dst_path', type=str, help='path for the en/de_crypted text to be written')
    parser.add_argument('key', type=str, help='key to encrypt given text')
    args = parser.parse_args()

    text = read_text(args.path)
    text2 = encrypt(text, args.key)
    write_encrypted_text(text2, args.dst_path)

