# Дан текст (через cmd). Произвести шифровку над ним: Цезаря
# Сделать функции дешифровки в каждом скрипте. Если через cmd будет подаваться параметр --decryption, то тогда вызывай
# дешифровку, если же --encryption, то шифровку. По умолчанию шифровка, оба параметра использованы быть не могут.


from pathlib import Path
from string import ascii_lowercase as letters
import argparse


def read_text(path: str) -> str:
    if not Path(path).exists:
        raise FileExistsError()

    with open(path, 'r', encoding='utf-8-sig') as fr:
        text = fr.read()
        return text


def write_encrypted_text(text: str, dst_path: str) -> None:
    if not Path(dst_path).exists():
        Path(dst_path).touch()

    with open(dst_path, 'w', encoding='utf-8-sig') as writer:
        writer.write(text)


def encrypt(text, decrypt: bool = False, shift: int = 2) -> str:
    indxs, text2 = {}, ''

    for i in range(len(letters)):
        if letters[i] in text or letters[i].upper() in text:
            indxs[letters[i]] = i
    if decrypt:
        shift = -shift

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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ceasar encryption')
    parser.add_argument('path', type=str, help='path to the file with text')
    parser.add_argument('dst_path', type=str, help = 'path for the en/de_crypted text to be written')
    parser.add_argument('-dec', '--decrypt', type=bool, default=False, help='will decrypt text if True, else encrypt')
    parser.add_argument('-sh', '--shift', type=int, default=2, help='number of indexes to shift letters')
    args = parser.parse_args()

    text = read_text(args.path)

    text_enc = encrypt(text, args.decrypt, args.shift)
    write_encrypted_text(text_enc, args.dst_path)







