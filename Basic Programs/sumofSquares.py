def sum_squares(num):
    sum = 0
    for i in range(1,num + 1):
        sum = sum + (i**2)
    print("Sum of squares: ", sum)

sum_squares(4)