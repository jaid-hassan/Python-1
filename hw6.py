# 1. Tuple Creation and Indexing

tup = (1,2,3,4,5,6,7,8,9,10)
print(tup[3])
print(tup[-1])
# 2. Tuple Operations

tup_1 = (1,2,3)
tup_2 = (4,5,6)
new_tup = tup_1+tup_2
print(len(new_tup))
# 3. Tuple Unpacking

fruit_tup = ("Apple","banana","mango")
fruit_1,fruit_2,fruit_3 = fruit_tup
print(fruit_1)
print(fruit_2)
print(fruit_3)
# 4. Tuple Methods

num_tup = (1,2,5,30,23,5,30,5,10,34)
count_5= num_tup.count(5)
index_10 = num_tup.index(10)
print(count_5)
print(index_10)
# 1. Set Crea􀆟on and Basic Operations

set_prime_num = {2,3,5,7,11}
set_prime_num.add (13)
set_prime_num.remove (3)
print(set_prime_num)
# 2. Set Opera􀆟ons

set_1 = {1, 2, 3, 4}
set_2 = {3, 4, 5, 6}
print("Union of this set is : ", set_1 | set_2)
print("Intersection of this set is : ", set_1 & set_2 )
print("Difference of these two set is : ",set_1 - set_2 )
# 3. Set Methods

set_python = {"P","y","t","h","o","n"}
print('h' in set_python)
print(len(set_python))
# 1. Dictionary Crea􀆟on and Access

dic = {'name': 'Alice', 'age': 25, 'city': 'NewYork'}
print(dic['name'])
dic ['Job']= 'Engineer'
dic ['age']= 26
print(dic)
# 2. Dictionary Methods

dic_1 = {'a': 1, 'b': 2, 'c': 3}
dic_2 = dic_1.keys()
print(dic_2)
dic_3 = dic_1.values()
print(dic_3)
print(dic_1.items())
# Challenge

phone_book = {'Alice': {'phone': '1234', 'email': 'alice@example.com'},'Bob': {'phone': '5678', 'email': 'bob@example.com'}}
alice_num = phone_book['Alice']
num = alice_num['phone']
print("Alice phone number : ",num)
phone_book['charlie'] =  {'phone': '9101', 'email': 'charlie@example.com'}
del phone_book['Bob']
print(phone_book)