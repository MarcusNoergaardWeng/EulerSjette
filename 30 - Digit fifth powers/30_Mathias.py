from functools import reduce

def number_to_digits(n):
    return list(map((lambda x : int(x)), str(n)))

def digit_power_sum(digits, power):
    return reduce(lambda total,digit: total + digit**power, digits, 0)

total = 0
for i in range(2,1000000):
    l = number_to_digits(i)
    if digit_power_sum(l, 5) == i:
        total += i

print(total)