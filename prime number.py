def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_primes(count):
    primes = []
    num = 100
    while len(primes) < count:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

prime_list = generate_primes(10)
for prime in prime_list:
    print(prime)
