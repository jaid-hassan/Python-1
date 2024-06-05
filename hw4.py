# 1...........
for num in range(21):
    if num % 2 == 0 :
            print(num)

# 2...........
sum = 0
for num in range(21) :
      if num % 2 != 0 :
            sum += num
print ("The sum of all odd numbers between 1 and 20 is : ",sum)

# 3...........
num = 10
while num >= 1:
    print(num)
    num -= 1

# 4...........
for i in range(1,11) :
    print (f"{i*i}")

# 5...........
userin = input("Type a string : ")
char_in_str = 0 

for char in userin :
     char_in_str += 1 
print ("Character number in this str is : ", char_in_str) 

# 6...........
five_times = 0
while five_times < 5 :
     print("Hello, World!")
     five_times += 1

# 7............
num = int(input("Enter your number : "))
factorial = 1
for i in range(1,num+1) :
    factorial *= i
print(f"The factorial of {num} is : {factorial}")

# 8............
num = 0
for i in range(11) :
    num += i
print ("The sum of the first 10 natural number is : ",num)

# 9............
num = int(input("Enter a number: "))
print(f"Multiplication table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# 10...........
for num in range(20, 0, -1):
    print(num)
    