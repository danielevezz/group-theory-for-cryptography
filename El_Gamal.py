from Group import *
import random

prime = 2**19 - 1
G = U(prime)

rng = random.SystemRandom()
# Number of generators = Euler's totient function
# g may be 0
g = int(rng.random() * 10000 % prime)

# Bob generate a nonce
b = int(rng.random() * 10000)

# Bob key
B = G.power(g, b)

# Alice generate a nonce
k = int(rng.random() * 10000)

msg = 29

# Alice creates message tuple
(x, y) = (G.power(g, k), G.compose(G.power(B, k), msg))

# Bob decrypts
decrypt = G.compose(G.power(G.inverse(x), b), y)

print(msg, decrypt)


# Mixer
# Generate k'
k1 = int(rng.random() * 10000)

# Encryption of identity
(x1, y1) = (G.power(g, k1), G.compose(G.power(B, k1), G.identity()))

(x2, y2) = (G.compose(x, x1), G.compose(y, y1))
decrypt2 = G.compose(G.power(G.inverse(x2), b), y2)

print(x, y)
print(x2, y2)

print(msg, decrypt2)
