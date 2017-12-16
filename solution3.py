import time


def reverse(num):
    rev = 0
    while num > 0:
        rev = (10*rev) + num%10
        num //= 10
    return rev


def is_pal(i):
    return i == reverse(i)


###################################################################################


def generate_prime_list(n):
    prime_list = []
    for num in range(10 ** (n - 1), 10 ** n):
        if all(num % i != 0 for i in range(2, num)):
            prime_list.append(num)
    return prime_list


def solve_problem(n):
    max_pal = 0
    max_a = 0
    max_b = 0
    prime_list = generate_prime_list(n)
    for a in prime_list:
        for b in prime_list:
            prod = a * b
            if is_pal(prod) and prod > max_pal:
                max_pal = prod
                max_a = a
                max_b = b
    return max_pal, max_a, max_b


def measure_time(n):
    sum = 0
    for i in range(1, (n+1)):
        start = time.time()
        solve_problem(5)
        end = time.time()
        sum += end - start
    return sum/n


print(measure_time(10))
