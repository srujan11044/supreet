def is_prime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def find_primes(start,end):
    primes = [num for num in range(start,end+1)if is_prime(num)]
    return primes

start = 2
end = 50
prime_numbers=find_primes(start,end)
print("prime numbers in the given range",prime_numbers)