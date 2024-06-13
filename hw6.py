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