num1 = 8
num2 = 5
tmp = num2

for i in range(num1):
    num2 += i
    if num2 > num1:
        num2 = num2 - num1
    
    for e in range(num1):
        print(num2, end=" ")
        num2 += 1
        if num2 > num1:
            num2 = 1
    
    num2 = tmp
    
    print("")