def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def primes(n):
    for i in range(2, n+1):
        if prime(i):
            yield i

n = int(input())
print(*primes(n))