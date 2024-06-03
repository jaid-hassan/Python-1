# 1.............
userin =int(input("Enter your number sir: "))

if userin > 0 :
    print("The number is positive.")
elif userin < 0 :
    print("The number is negative.")
else :
    print("The number is zero.")
 
# 2.............
userin2 =int(input("Enter your age sir: "))

if userin2 >= 18 :
    print("You are elegible for vote.")
else :
    print("You are not elegible for vote.")

# 3.............
num1 =float(input("Enter the first number: "))
num2 =float(input("Enter the second number: "))

if num1 < num2 :
   print("Second number is the larger number.")
elif num1 > num2 :
   print("First number is the larger number.")
else :
    print("The two numbers are equal." )

# 4.............
userin3 =float(input("Enter your number sir: "))  
if userin3 % 5 == 0 :
    print("The number is divisible by 5.") 
else : 
    print("The number is not divisible by 5.") 

# 5............
userin4 =float(input("Enter your score (out of 100) : "))
if 50 <= userin4 >= 100 :
    print("Pass.")
else :
    print("Fail.")

# 6.............
operator = input("Enter a operator(  +, _ , * , / ) : ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+" :
    result = num1+num2
if operator == "-" :
    result = num1-num2
if operator == "*" :
    result = num1*num2
if operator == "/" :
    result = num1/num2
print("The result is: ",int(result))