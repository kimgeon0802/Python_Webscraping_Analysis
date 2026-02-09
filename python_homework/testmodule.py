import math

def cir(rad):
    return math.pi * rad * rad

def rec(wid, hei):
    return wid * hei

def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fac(n-1)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a