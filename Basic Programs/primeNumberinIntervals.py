def print_primenumber(a , b):

    for i in range(a, b+1):
        factor = 0
        for j in range(1,i):
            if i % j == 0:
                factor = factor + 1

        if factor == 2:
            print(i)

print_primenumber(11,45)