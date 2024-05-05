# Given a number, we have to find the prime numbers below the given number...

def isprime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def numbers(n):
    for i in range(2, n + 1):
        if isprime(i):
            print(i)


n = int(input("Enter a number:"))
print(numbers(n))


