#1.....
names_ages = {
    "Alice": 28,
    "Bob": 32,
    "Charlie": 25,
    "David": 40
}

for name, age in names_ages.items():
    print(f"{name}: {age}")

#2.....
my_dict = {"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40}
threshold = 30

for key, value in my_dict.items():
    if value > threshold:
        print(key)

#3.......
squares_dict = {x: x**2 for x in range(1, 11)}

print(squares_dict)
