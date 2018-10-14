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

msg = 220997

# Alice creates message tuple
(x, y) = (G.power(g, k), G.compose(G.power(B, k), msg))


# Bob decrypts
decrypt = G.compose(G.power(G.inverse(x), b), y)

print(msg, decrypt)
