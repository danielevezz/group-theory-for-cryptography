from Group import *
import random

prime = 2**19 - 1
G = U(prime)

rng = random.SystemRandom()
# Number of generators = Euler's totient function
# g may be 0
g = int(rng.random() * 10000 % prime)


# Alice generate a nonce
alfa = int(rng.random() * 10000)


# Bob generate a nonce
beta = int(rng.random() * 10000)


# Alice message
A = G.power(g, alfa)

# Bob message
B = G.power(g, beta)


# Alice calculates her key
k = G.power(B, alfa)

# Bob calculates her key
k1 = G.power(A, beta)

print(k, k1)
