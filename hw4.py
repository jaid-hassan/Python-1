operator = input("Enter a operator(  +, _ , * , / ) : ")
num1 = int (input("Enter the first number: "))
num2 = int (input("Enter the second number: "))

if operator == "+" :
    print("The result is: ", int(num1+num2))
if operator == "-" :
    print("The result is: ", int(num1-num2))
if operator == "*" :
    print("The result is: ", int(num1*num2))
if operator == "/" :
    print("The result is: ", int(num1/num2))