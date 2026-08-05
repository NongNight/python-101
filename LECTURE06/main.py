# prime_number = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# print(f"Prime number: {prime_number}")
# fifth_prime = prime_number[4]
# print(f"Fifth prime number: {fifth_prime}")

# colors = ["red", "blue", "green", "yellow", "purple"]
# second_to_last_color = colors[-2]
# print(f"Second to last color: {second_to_last_color}")

# shapes = ["cirscle", "square", "triangle", "rectangle", "hexagon"]
# shapes[1] = "ellipse"
# shapes[3] = "pentagon"
# print(f"Modified shapes: {shapes}")

# fruits = ["apple", "banana", "cherry"]
# more_fruit = ["mango", "pineapple"]
# for fruit in more_fruit:
#     fruits.append(fruit)
# print(f"Fruits after append: {fruits}")

# berries = ["raspberry", "blackberry"]
# berries.insert(1, "strawberry")
# berries.insert(2, "blueberry")
# print(f"Berries after in sert: {berries}")

# fruits_with_duplicates = ["apple", "banana","apple", "cherry", "apple","kiwi"]
# while "apple" in fruits_with_duplicates:
#     fruits_with_duplicates.remove("apple")
# print(f"Fruit after remove: {fruits_with_duplicates}")

# grades = [85, 90, 78, 92, 88]
# third_grade = grades.pop(2)
# grades.append(third_grade)
# print(f"Grades after pop: {grades}")

# animals = ["cat", "dog", "rabbit", "hamster", "dog", "parrot"]
# first_dog_index = animals.index("dog")
# print(f"The first occurrence of 'dog is as index: {first_dog_index}")

# second_dog_index = animals.index("dog", first_dog_index + 1)
# print(f"The first occurrence of 'dog is as index: {second_dog_index}")

# thrird_dog_index = animals.index("dog", second_dog_index + 1)
# print(f"The first occurrence of 'dog is as index: {thrird_dog_index}")

# nesred_list = [[1, 2, 3,],[4, 5, 6], [7, 8, 9]]
# for sublist in nesred_list:
#     sublist.clear()
# print(f"Nested list after clear: {nesred_list}")'

# number = [4, 2, 3, 1, 5]
# number.sort()
# print(number)

# number = [1, 2, 3, 4, 5]
# number.reverse()
# print(number)

# heroes = ["Ironman", "Thor", "Hukl", "Superman","Spiderman"]
# h2 = ["Dr. strange", "Cpt.America", "Black Panther", "Ant Man"]

# heroes.insert(0 ,h2[0])
# print(heroes.index("Thor"))
# heroes.insert(heroes.index("Thor"),h2[1])
# print(heroes)
# heroes.remove("Superman")
# heroes.append("Ant Man")
# print(heroes)
# heroes.sort()
# print(heroes)
# heroes.reverse()
# print(heroes)
# newheroes = heroes
# newheroes[0] = "Wonder Women"
# print(heroes)
# copyheroes = [] + heroes
# copyheroes[0] = "Hanuman"
# print(heroes)
# print(copyheroes)

# data = list(range(100))
# sliced_data = data[10:51:5]
# print(f"Sliecd data {sliced_data}")

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(numbers[2:6])
# print(numbers[1:8:2])
# print(numbers[:4])
# print(numbers[6:])

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(numbers[-5:-1])
# print(numbers[::-1])

# ss = "Sammy Shark!"
# print(ss[4])
# print(ss[6:11])
# print(ss[:5])
# print(ss[7:])
# print(ss[-4:-1])
# print(ss[6:11])
# print(ss[6:11:1])
# print(ss[0:12:2])
# print(ss[0:12:4])
# print(ss[::4])
# print(ss[::-1])
# print(ss[::-2])

# even_numbers = [2, 4, 6, 8, 10]
# heroes = ["Ironman", "Thor", "Hulk", "Spiderman"]
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers[-5])
# numbers[8] = 99
# print(numbers)

# pluslist = heroes + even_numbers
# print(pluslist)
# print(len(numbers))

# numbers = [4, 2, 9, 1, 5, 6]

# length = len(numbers)
# print(f"Length of the list: {length}")

# total_sum = sum(numbers)
# print(f"Sum of all elements: {total_sum}")

# max_value = max(numbers)
# print(f"Maximum value: {max_value}")

# min_value = min(numbers)
# print(f"Minimum value: {min_value}")

# sorted_value = sorted(numbers)
# print(f"Sorted value: {sorted_value}")

# bool_list = [False,True,False]
# any_true = any(bool_list)
# print(f"Is any element True? {any_true}")

# all_true = all(bool_list)
# print(f"IAre all element True? {all_true}")

# string = "hello"
# char_list = list(string)
# print(f"List of characters: {char_list}")

# reversed_number = list(reversed(numbers))
# print(f"Reversed list: {reversed_number}")

# enumerated_number = list(enumerate(numbers))
# print(f"Enumerated list: {enumerated_number}")

# NUM_EMPLOYEE = 6

# def main():
#     hours = [0] * NUM_EMPLOYEE
#     for index in range(NUM_EMPLOYEE):
#         print("Enter the hours worked by employ",\
#             index + 1 , ": ", sep="", end="" )
#         hours[index] = float(input())
        
#     pay_rate = float(input("Enter the hourly pay rate:"))
    
#     for index in range(NUM_EMPLOYEE):
#         gross_pay = hours[index] * pay_rate
#         print("Gross pay for employee", index + 1, ":$",\
#             format(gross_pay,",.2f"),sep="")
        
# main()

# matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]

# matrix[0][1] = 10
# print(matrix)

# for row in matrix:
#     for element in row:
#         print(element, end=" ")
#     print()

# import random
# rows = 3
# cols = 4

# def main():
#     values = [
#         [0, 0, 0, 0],
#         [0, 0, 0, 0],
#         [0, 0, 0, 0]
#     ]
#     for r in range(rows):
#         for c in range(cols):
#             values[r][c] = random.randint(1,100)
#     print(values)
# main()

inventory = [["Apple",50,0.75],
             ["Banana",100,0.50],
             ["Orange", 75,0.80]
             ]
up_inven = []
inventory[1][1] = inventory[1][1] - 20
print(inventory)