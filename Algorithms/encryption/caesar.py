# Дан текст (через cmd). Произвести шифровку над ним: Цезаря
# Сделать функции дешифровки в каждом скрипте. Если через cmd будет подаваться параметр --decryption, то тогда вызывай
# дешифровку, если же --encryption, то шифровку. По умолчанию шифровка, оба параметра использованы быть не могут.


from pathlib import Path
from string import ascii_lowercase as letters
import argparse


def read_text(file_path: str) -> str:
    if Path(file_path).exists:
        return Path(file_path).read_text()

    raise FileNotFoundError()


def ceasar_encrypt(text: str, shift: int = 2) -> str:
    indxs, text2 = {}, ''
    for i in range(len(letters)):
        if letters[i] in text or letters[i].upper():
            indxs[letters[i]] = i

    for let in text:

        if let.lower() in letters:
            lowered = False
            if let.lower() != let:
                lowered = True

            index = indxs[let.lower()] + shift

            if index >= len(letters):
                index = index - len(letters)
            let2 = letters[index].upper() if lowered else letters[index]

        else:
            let2 = let

        text2 += let2

    return text2


def decrypt_from_ceasar(text: str, shift: int = 2) -> str:
    indxs, real_text = {}, ''
    for i in range(len(letters)):
        if letters[i] in text or letters[i].upper() in text:
            indxs[letters[i]] = i

    for let in text:
        if let.lower() in letters:
            lowered = False
            if let.lower() != let:
                lowered = True

            index = indxs[let.lower()] - shift
            let2 = letters[index] if not lowered else letters[index].upper()

        else:
            let2 = let
        real_text += let2

    return real_text


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ceasar encryption')
    parser.add_argument('path', type=str, help='path to the file with text')
    parser.add_argument('-sh', '--shift', type=int, default=2, help='number of indexes to shift letters')
    parser.add_argument('-dec', '--decrypt', type=bool, default=False, help='will decrypt text if True, else encrypt')
    args = parser.parse_args()
    text = read_text(args.path)
    if args.decrypt:
        res = decrypt_from_ceasar(text, args.shift)
    else:
        res = ceasar_encrypt(text, args.shift)
    print(res)


