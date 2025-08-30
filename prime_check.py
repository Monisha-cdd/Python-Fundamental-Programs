# Program: Check if number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

print("Is 17 prime?:", is_prime(17))
print("Is 18 prime?:", is_prime(18))
