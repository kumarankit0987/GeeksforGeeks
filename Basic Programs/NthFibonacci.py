# Fibonacci Number Program
def fibonacci_series(num):
    a = 0
    b = 1
    print(a, b, end=" ")
    for i in range(1,num+1):
        c = a + b
        print(c, end=" ")
        a = b
        b = c

fibonacci_series(10)
