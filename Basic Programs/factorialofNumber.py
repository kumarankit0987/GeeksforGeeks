def factorial(num):
    factorial = 1
    for i in range(2, num + 1):
        factorial = factorial * i

    print("Factorial of ", num ," is", factorial)

factorial(5)