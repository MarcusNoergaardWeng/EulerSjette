def factorial(n):
    return factorial_rec(1,n)

def factorial_rec(acc, n):
    if(n == 0):
        return acc
    else:
        return factorial_rec(n * acc, n-1)

def digit_sum(n):
    s = str(n)
    total = 0
    for char in s:
        total += int(char)
    return total

print(digit_sum(factorial(100)))