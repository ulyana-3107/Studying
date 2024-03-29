# Шифровка со сдвигом текста используя ключ (передаётся через cmd)
# Сделать функции дешифровки в каждом скрипте. Если через cmd будет подаваться параметр --decryption, то тогда вызывай
# дешифровку, если же --encryption, то шифровку. По умолчанию шифровка, оба параметра использованы быть не могут.


from string import ascii_lowercase as letters
import argparse
from pathlib import Path


def read_text(path: str) -> str:

    if not Path(path).exists():
        raise FileExistsError()

    with open(path, 'r', encoding='utf-8-sig') as reader:
        text = reader.read()
        return text


def encrypt(text, key: str, decrypt: bool = False) -> str:

    indxs_txt, indxs_key, text2 = {}, {}, ''

    for i in range(len(letters)):
        if letters[i] in text or letters[i].upper() in text:
            indxs_txt[letters[i].lower()] = i
        if letters[i] in key or letters[i].upper() in key:
            indxs_key[letters[i].lower()] = i

    i, c = 0, 0
    while i < len(text):
        if text[i].lower() in letters:
            lowered = False
            if text[i].lower() != text[i]:
                lowered = True

            if c == len(key):
                c = 0
            shift = indxs_key[key[c]] if not decrypt else -indxs_key[key[c]]
            index = indxs_txt[text[i].lower()] + shift

            if index >= len(letters):
                index = index - len(letters)
            let2 = letters[index] if not lowered else letters[index].upper()
            c += 1

        else:
            let2 = text[i]

        i += 1
        text2 += let2

    return text2


def write_encrypted_text(text: str, dst_path: str) -> None:
    if not Path(dst_path).exists():
        Path(dst_path).touch()

    with open(dst_path, 'w', encoding='utf-8-sig') as writer:
        writer.write(text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Shift encryption realisation')
    parser.add_argument('path', type=str, help='path to the file with text')
    parser.add_argument('dst_path', type=str, help='path for the en/de_crypted text to be written')
    parser.add_argument('key', type=str, help='key for encryption')
    parser.add_argument('-d', '--decrypt', type=bool, default=False, help='will decrypt text if True, else encrypt')

    args = parser.parse_args()
    text = read_text(args.path)
    text2 = encrypt(text, args.key, args.decrypt)
    write_encrypted_text(text2, args.dst_path)
