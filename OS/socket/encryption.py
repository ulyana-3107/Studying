def encrypt(text: str, key: str) -> str:
    encypted = []

    for idx in range(len(text)):
        encypted.append(chr(ord(text[idx]) ^ ord(key[idx % len(key)])))

    return "".join(encypted)