def fib(n):
    if n < 1:
        return -1
    
    first = 0
    second = 1
    
    if n == 1:
        return first
    
    if n == 2:
        return second
    
    count = 3 # Starting from 3 becuase we already know the first two values

    while count <= n:
        fib_number = first + second
        first = second
        second = fib_number
        count += 1 # increment count in each iteration
    return fib_number

n = 11
print("\n 11th fibonacci number is  ",fib(n))