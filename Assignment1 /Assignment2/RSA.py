import math
p = int(input("Enter a prime number p: "))
q = int(input("Enter a prime number q: "))
n = p * q
t = (p - 1) * (q - 1)
e = int(input(f"Enter a public exponent e (1 < e < {t} and gcd(e, {t}) = 1): "))
def mod_inverse(e, t):
    for d in range(1, t):
        if (e * d) % t == 1:
            return d
    return None
d = mod_inverse(e, t)
m = int(input(f"Enter message number (0 < m < {n}): "))
c = pow(m, e, n)
decrypted_m = pow(c, d, n)
print(f"\nPublic Key: (e={e}, n={n})")
print(f"Private Key: (d={d}, n={n})")
print(f"Original Message: {m}")
print(f"Encrypted Message: {c}")
print(f"Decrypted Message: {decrypted_m}")