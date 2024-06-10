# 1......................
num_list = [1,2,3,4,5,6]
print (num_list)

# 2......................
num_list = [1,2,3,4,5,6,7,8]
print("First element: ",num_list[0])
print("Last element: ",num_list[-1])
print("Index 5 is : ",num_list[5])

# 3.....................
num_list = [1,2,3,4,5,6,7,8]
print("First three element of the list is : ",num_list[0:3])
print("Last three element of the list is : ",num_list[-3:])
print("Every alternate element of the list is :",num_list[::2])

# 4.....................
num_list = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200]
num_list[3]=15
num_list.append(11)
del num_list[2]

# 5....................
num_list = [1,2,3,4,5,6]
print(len(num_list))
doubled_numbers=num_list+num_list
print(doubled_numbers)
print(7 in num_list)

# 6...................
num_list = [1,2,3,4,5,6,7,8]
for i in num_list:
    print(i)

# 7...................
num_list = [1,2,3,4,5,6,7,8,9]
square_num = [i * i for i in num_list]
print(square_num)

# 8..................
duplicates_num = [10, 20, 30, 15, 50, 60, 70, 80, 90, 100, 11, 20, 30, 50, 100]
unique_numbers = []
for i in duplicates_num:
    if i not in unique_numbers:
        unique_numbers.append(i)
print("Unique numbers:", unique_numbers)