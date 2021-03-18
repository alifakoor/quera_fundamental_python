n = int(input())

def is_number_prime(number):
    square = int(number ** (1/2))
    for i in range(2, square+1):
        if (number % i) == 0:
            return False
    return True

def count_primes_less_number(number):
    count = 0
    for i in range(2, number):
        if is_number_prime(i):
            count += 1
    return count

def count_prime_divisor(number):
    count = 0
    for i in range(2, number):
        if is_number_prime(i):
            if number % i == 0:
                count += 1
    return count

def calculate_price_or_discount(weight):
    if is_number_prime(weight):
        return count_primes_less_number(weight)
    else:
        return count_prime_divisor(weight)

total_price = 0
for i in range(n):
    weight = int(input())
    total_price += calculate_price_or_discount(weight)

print(total_price - calculate_price_or_discount(total_price))