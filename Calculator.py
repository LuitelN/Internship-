x = float(input("Enter the first number: "))
y = float(input("Enter the second number:"))
Operation = input("Enter the operation (+,-,/,*):")


def add_num(num1, num2):
    result = num1 + num2
    x = round(result, 4)
    #integer_number = int(result)
    print("The sum of two numbers is:", x)

def difference_num(num1, num2):
    result = num1 - num2
    x = round(result, 4)
    print("The difference of two numbers is: ", x)

def multiply_num(num1, num2):
    result = num1 * num2 
    x = round(result, 4)
    print("The product of two numbers is: ", x)

def remainder(num1, num2):
    result = num1 / num2 
    x = round(result, 4) 
    print("The remainder is: ", x)

if Operation == '+':
    add_num(x,y)

elif Operation == '-':
    difference_num(x,y)

elif Operation == '*':
    multiply_num(x,y) 

elif Operation == "/":
    
    if y == 0:
        print('Math Error')
    else: 
        remainder(x,y)
   
