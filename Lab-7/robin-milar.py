import random

def is_prime_miller_rabin(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # write n as d * 2^r + 1
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    # repeat k times
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Example
P = int(input("Enter number to check: "))
if is_prime_miller_rabin(P):
    print(f"{P} is probably prime.")
else:
    print(f"{P} is composite.")
