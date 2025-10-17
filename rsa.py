"""
RSA encryption algorithm
a method for encrypting a number that uses seperate encryption and decryption keys
this file only implements the key generation algorithm

there are three important numbers in RSA called n, e, and d
e is called the encryption exponent
d is called the decryption exponent
n is called the modulus

these three numbers satisfy
((x ** e) ** d) % n == x % n

to use this system for encryption, n and e are made publicly available, and d is kept secret
a number x can be encrypted by computing (x ** e) % n
the original number can then be recovered by computing (E ** d) % n, where E is
the encrypted number

fortunately, python provides a three argument version of pow() that can compute powers modulo
a number very quickly:
(a ** b) % c == pow(a,b,c)
"""

# sample usage:
# n,e,d = generate_key(16)
# data = 20
# encrypted = pow(data,e,n)
# decrypted = pow(encrypted,d,n)
# assert decrypted == data


"""
RSA encryption algorithm
— keygen + encrypt/decrypt routines
— simple self-test harness built in
#!/usr/bin/env python3
"""

"""import random
from sympy import isprime

def generate_key(k, seed=None):
    def modinv(a, m):
        b = 1
        while (a * b) % m != 1:
            b += 1
        return b

    def gen_prime(bits, seed=None):
        random.seed(seed)
        while True:
            p = random.randrange(2**(bits-1), 2**bits)
            if isprime(p):       # <-- use sympy to test
                return p          # <— return the *prime* candidate

    print(f" Generating two {k}-bit primes…", end="", flush=True)
    e = gen_prime(k, seed)
    print(" ✓e", end="", flush=True)

    half = k // 2
    p = gen_prime(half, seed)
    while p % e == 1:
        p = gen_prime(half, seed)
    print(" ✓p", end="", flush=True)

    q = gen_prime(k-half, seed)
    while q % e == 1:
        q = gen_prime(k-half, seed)
    print(" ✓q")

    n = p * q
    phi = (p-1)*(q-1)
    d = modinv(e, phi)
    return n, e, d """

from sympy import randprime, mod_inverse

def gen_prime(bits):
    return randprime(2**(bits-1), 2**bits)

def generate_key(k, seed=None):
    print(f" Generating two {k}-bit primes…", end="", flush=True)
    e = gen_prime(k)
    print(" ✓e", end="", flush=True)

    half = k//2
    p = gen_prime(half)
    while p % e == 1:
        p = gen_prime(half)
    print(" ✓p", end="", flush=True)

    q = gen_prime(k-half)
    while q % e == 1:
        q = gen_prime(k-half)
    print(" ✓q")

    n = p*q
    phi = (p-1)*(q-1)
    d = mod_inverse(e, phi)
    return n, e, d


def encrypt_int(m_int, e, n):
    return pow(m_int, e, n)

def decrypt_int(c_int, d, n):
    return pow(c_int, d, n)

def str_to_int(s: str) -> int:
    return int.from_bytes(s.encode("utf-8"), "big")

def int_to_str(i: int) -> str:
    return i.to_bytes((i.bit_length()+7)//8, "big").decode("utf-8")

if __name__ == "__main__":
    # *** Quick demo with very small keys for instant feedback ***
    print(" Running quick 64-bit demo…")
    n, e, d = generate_key(64, seed=42)
    msg = "Hi"
    m_int = str_to_int(msg)
    c = encrypt_int(m_int, e, n)
    p = decrypt_int(c, d, n)
    recovered = int_to_str(p)
    print(f" • msg={msg!r}, recovered={recovered!r}")
    assert recovered == msg
    print(" 64-bit self-test OK\n")

    # *** Full 512-bit generation (will take a few seconds) ***
    print("🔑 Generating real 512-bit keypair…")
    n, e, d = generate_key(512)
    message = "Hello, RSA!"
    print(f"Original message: {message!r}")
    m_int = str_to_int(message)
    cipher = encrypt_int(m_int, e, n)
    print(f"Encrypted (hex, first 60 chars): {hex(cipher)[2:62]}…")
    plain_int = decrypt_int(cipher, d, n)
    plaintext = int_to_str(plain_int)
    print(f"Decrypted message: {plaintext!r}")
    assert plaintext == message
    print(" RSA self-test passed!")

