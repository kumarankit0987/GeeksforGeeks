# Armstrong number is a number which is the sum of power of digit is equal to that number i.e:- 153, 11
def armstrong_number(num):
    temp = num
    sum = 0
    while num !=0:
       digit = num % 10
       sum = sum + digit**3
       num = num // 10

    
    if sum == temp:
        print(temp, "is an Armstrong number")
    else:
           print(temp, "is not an Armstrong number")

armstrong_number(153)
            