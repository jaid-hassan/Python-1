#1......
my_tuple = (5, 10, 15, 20, 25)
value_to_check = 10

is_present = value_to_check in my_tuple
print(is_present)

#2......
my_tuple = (5, 10, 15, 20, 25)
value_to_find = 10

index_of_value = my_tuple.index(value_to_find)
print(index_of_value)

#3......
list_of_tuples = [('a', 1), ('b', 2), ('c', 3)]

dict_from_list = dict(list_of_tuples)
print(dict_from_list)  # Output: {'a': 1, 'b': 2, 'c': 3}
