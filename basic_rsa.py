# Generate keys:
# Pick two primes p and q
# Calculate n = p * q
# z = (p-1)*(q-1)
# Choose a prime number k, such that k is co-prime to z: that is, z is not divisible by k
# So, the numbers n and k are the public key.

# To find the secret key:
# d*e = 1 % z (solve for d)  => (k*j)/z = d, with a remainder of one
# d is the secret key.

# To encrypt the message:
# The message is P.
# P ^ k = E % n
# This is to say: (P^k)/n gives a remainder of E.
# This yields the encrypted message E.

# To decrypt the message:
# E ^ j = P % n
# Where j is the secret key, E is the message, and P is the plaintext message.
