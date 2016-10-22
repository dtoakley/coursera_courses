import math

def add_up(n):
    if n == 0:
        return 0
    else:
        return n + add_up(n - 1)

print((150**2 + 150) / 2)
print(add_up(150))

def multiply_up(n):
    if n == 0:
        return 1
    else:
        return n * multiply_up(n - 1)

print(math.factorial(10))
print(multiply_up(10))

counter = 0

def fib(num):
    global counter
    counter += 1
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)

def memoized_fib(num, memo_dict):
    global counter
    counter += 1
    if num in memo_dict:
        return memo_dict[num]
    else:
        sum1 = memoized_fib(num - 1, memo_dict)
        sum2 = memoized_fib(num - 2, memo_dict)
        memo_dict[num] = sum1 + sum2
        return sum1 + sum2


print(memoized_fib(25, {0:0, 1:1}), counter)
