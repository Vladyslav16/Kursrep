import random


def generate_keys(p, g):
    private_key = random.randint(1, p - 2)
    public_key = pow(g, private_key, p)
    return private_key, public_key


def encrypt(p, g, public_key, plaintext):
    k = random.randint(1, p - 2)
    c1 = pow(g, k, p)
    c2 = (plaintext * pow(public_key, k, p)) % p
    return c1, c2


def decrypt(p, private_key, c1, c2):
    s = pow(c1, private_key, p)
    s_inv = pow(s, -1, p)
    plaintext = (c2 * s_inv) % p
    return plaintext


def text_to_int(text):
    return int.from_bytes(text.encode('utf-8'), 'big')


def int_to_text(number):
    return number.to_bytes((number.bit_length() + 7) // 8, 'big').decode('utf-8', 'ignore')


def encrypt_text(p, g, public_key, text):
    plaintext_int = text_to_int(text)
    return encrypt(p, g, public_key, plaintext_int)


def decrypt_text(p, private_key, c1, c2):
    plaintext_int = decrypt(p, private_key, c1, c2)
    return int_to_text(plaintext_int)
