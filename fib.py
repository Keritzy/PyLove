num = int(input("enter numbers"))
 
num1, num2 = 0, 1
i = 0
 
while i < num:
    print(num1)
    temp = num1 + num2
    num1 = num2
    num2 = temp
    i += 1
