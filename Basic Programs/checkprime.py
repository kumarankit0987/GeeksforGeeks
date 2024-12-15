def check_prime(num):
    factor = 0
    
    for i in range(1,num + 1):
        if num % i == 0:
            factor = factor + 1
  
    if factor == 2:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

check_prime(11)