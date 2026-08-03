# def greet():
#     print("Hello, World")
    
# greet()

# def message ():
#     print("I am Attakon")
#     print("King of the Score")

# print("I have a message for you.")
# message()
# print("Goodbye")

# def main():
#     print("I have a message for you.")
#     message()
#     print("Goodbye")
    
# def message():
#     print("I am Attakon")
#     print("I Love U")
    
# main()

# def greet(name):
#     print(f"Hello, {name}!")
    
# greet("Alice")
# greet("Tom")

# def add(a, b):
#     return a + b
# result = add(5)
# print(result)

# def greet(name="World"):
#     print(f"Hello, {name}!")

# greet()
# greet("Alice")

# def sum_all(*args):
#     return sum(args)
# print(sum_all(1, 2, 3, 4, 5))

# def find_max(*args):
#     if not args:
#         return None
#     max_value = args[0]
#     for number in args:
#         if number > max_value:
#             max_value = number
#     return max_value
# result = find_max(3,5,7,2,8)
# print(f"The maximum value is: {result}")

# def print_all(*args):
#     for index, arg in enumerate(args):
#         print(f"Argument {index + 1}:{arg}")
# print_all("Python",3.8, True, [1,2,3], {"key":"value"})

# def display_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}:{value}")
# display_info(name="Alice", age=30, city="New York")

# def multiply(a, b):
#     return a*b
# result = multiply(4,5)
# print(result)

# def calculate_stats(numbers):
#     total_snm = sum(numbers)
#     average = total_snm / len(numbers)
#     maximum = max(numbers)
#     minimum = min(numbers)
#     return total_snm, average, maximum, minimum
# numbers = [5, 10, 15, 20, 25]
# total, avg, max_num, min_num = calculate_stats(numbers)

# print(f"Total Sum: {total}")
# print(f"Average: {avg}")
# print(f"Maximun: {max_num}")
# print(f"Minimun: {min_num}")

# def is_armstrong(num):
#     num_str = str(num)
#     digit = len(num_str)
#     result = 0
#     for i in num_str:
#         result += int(i) ** digit
#     return result == num
    
    
# print(is_armstrong(153)) 
# print(is_armstrong(9474))
# print(is_armstrong(123))


# def my_function():
#     locals_variable = "I'm inside the function"
#     print(locals_variable)
# my_function()

# global_variable = "I'm inside the function"
# def my_function():
#     print(global_variable)
# my_function()
# print(global_variable)

# import random

# HEADS = 1
# TAILS = 2
# TOSSES = 10
# def tosses_coin():
#     for toss in range(TOSSES):
#         if random.randint(HEADS, TAILS) == HEADS:
#             print("Heads")
#         else:
#             print("Tails")
# tosses_coin()

# counter = 0 

# def increment():
#     global counter
#     counter += 1 
# increment()
# increment()

# print(counter)

# import match_operations

# result_add = match_operations(10,5)
# result_subtract = match_operations(10,5)
# result_multiply = match_operations(10,5)
# result_divide = match_operations(10,5)

# print(f"Add: {result_add}")
# print(f"Sub: {result_subtract}")
# print(f"Multi: {result_multiply}")
# print(f"Divi: {result_divide}")

# def factorial(n):
#     if n == 0:
#         return 1 
#     else :
#         return n * factorial(n - 1)
# print(factorial(5))

# def fibonacci(n):
#     if n == 0 :
#         return 0 
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
# print(fibonacci(6))

# def factorial_iter(n):
#     result = 1
#     for i in range(2, n + 1):
#         result *= i
#     return result
# print(factorial_iter(5))

# def generate_primes(num):
#     for i in range num :
#         result = i*10
#         print(result)
    

# print(generate_primes(10))

# ******************************************