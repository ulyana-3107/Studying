# Шифровка со сдвигом текста используя ключ (передаётся через cmd)
# Сделать функции дешифровки в каждом скрипте. Если через cmd будет подаваться параметр --decryption, то тогда вызывай
# дешифровку, если же --encryption, то шифровку. По умолчанию шифровка, оба параметра использованы быть не могут.


from string import ascii_lowercase as letters
import argparse
from pathlib import Path


def read_text(path: str) -> str:
    if Path(path).exists:
        return Path(path).read_text()

    raise FileNotFoundError()


def shift_encrypt(text: str, key: str) -> str:
    print(letters)
    indxs, text2 = {}, ''

    for i in range(len(letters)):
        if letters[i] in text or letters[i].upper() in text:
            indxs[letters[i].lower()] = i

    i, c = 0, 0
    while i < len(text):
        if text[i].lower() in letters:
            lowered = False
            if text[i].lower() != text[i]:
                lowered = True

            if c == len(key):
                c = 0
            shift = c + 1
            index = indxs[text[i].lower()] + shift

            if index >= len(letters):
                index = index - len(letters)
            let2 = letters[index] if not lowered else letters[index].upper()
            c += 1

        else:
            let2 = text[i]

        i += 1
        text2 += let2

    return text2


def decrypt_from_shift(text: str, key: str) -> str:
    len_nums = len([elem for elem in text if elem.lower() in letters])
    real_text, indxs = '', {}

    for i in range(len(letters)):
        if letters[i] in text or letters[i].upper() in text:
            indxs[letters[i]] = i

    i = len(text) - 1
    if len_nums % len(key):
        shift = len_nums % len(key)
    else:
        shift = len(key)

    while i > -1:
        if text[i].lower() in letters:
            lowered = False
            if text[i].lower() != text[i]:
                lowered = True
            shift = len(key) if shift == 0 else shift
            index = indxs[text[i].lower()] - shift
            let2 = letters[index] if not lowered else letters[index].upper()
            shift -= 1
        else:
            let2 = text[i]

        i -= 1
        real_text = let2 + real_text

    return real_text


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Shift encryption realisation')
    parser.add_argument('path', type=str, help='path to the file with text')
    parser.add_argument('key', type=str, help='key for encryption')
    parser.add_argument('-d', '--decrypt', type=bool, default=False, help='will decrypt text if True, else encrypt')
    args = parser.parse_args()
    text = read_text(args.path)
    if args.decrypt:
        res = decrypt_from_shift(text, args.key)
    else:
        res = shift_encrypt(text, args.key)
    print(res)
