# Generate keys:
# Pick two primes p and q
# Calculate n = p * q
# z = (p-1)*(q-1)
# Choose a prime number k, such that k is co-prime to z: that is, z is not divisible by k
# So, the numbers n and k are the public key.

# To find the secret key:
# d*k = 1 % z (solve for d)  => (k*d)/z = d, with a remainder of one
# d is the secret key.

# To encrypt the message:
# The message is P.
# P ^ k = E % n
# This is to say: (P^k)/n gives a remainder of E.
# This yields the encrypted message E.

# To decrypt the message:
# E ^ j = P % n
# Where j is the secret key, E is the message, and P is the plaintext message.
import time, random
from fractions import gcd

def isPrime(x):
    divisors = [i for i in range(2,x) if x%i==0]
    return len(divisors)==0
def extendedEuclidianMMI(a,b):
    t=0
    t1=1
    r=b
    r1=a
    while r1 !=0:
        q = r//r1
        t,t1=t1,t-q*t1
        r,r1=r1,r-q*r1
    if r > 1: return None
    elif t<0:t=t+b
    return t
def RSAKeygen(p,q):
    n = p*q
    z = (p-1)*(q-1)
    coprimes = [i for i in range(2,z+1) if isPrime(i)]
    random.seed(time.time())
    k = coprimes[random.randint(0,len(coprimes)-1)]
    publicKey = (n,k)
    privateKey = (n,extendedEuclidianMMI(k,z))
    return [privateKey,publicKey]

def paddingFunk(message,key):
    m = 1
    for char in message:
        m*=ord(char)
    print m%key[0]
    if m>key[0]: return m%key[0]
    else:
        print m
        return m

def encrypt(message,key,padding):
    m=padding(message,key)
    return m**key[1]%key[0]

def decrypt(message,key): return message**key[1]%key[0]

keys = RSAKeygen(61,53)
M=encrypt('hello',keys[1],paddingFunk)
print M
print decrypt(M,keys[0])
