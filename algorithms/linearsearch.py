import random

def create_list():
    numbers = []
    x = 1
    list_length = input("What is number list length? ")
    while len(numbers) < int(list_length):
        x += random.randint(1,20)
        numbers.append(x)
    return numbers

def find_number(numbers, number_to_find):
    index = ''
    for i in range(0,len(numbers)):
        if numbers[i] == int(number_to_find):
            return i
    return -1

numbers = create_list()
print(numbers)   # print list to debug
number_to_find = input("what is number to find? ")
result = find_number(numbers, number_to_find)
if result == -1:
    print("number not in list")
else:
    print(f"{number_to_find} is index {result}")
