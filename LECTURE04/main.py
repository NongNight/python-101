# sales = float(input("Enter the amonut of sales: "))
# comm_rate = float(input("Enter the commission rate: "))
# commission = sales * comm_rate
# print("The commission is $",format(commission,',.2f'))

# for num in [1,2,3,4,5]:
#     print(num)
# fruits = ["apple","banana","cherry"]
# for fruit in fruits:
#     print(fruit)

# for char in "Hello":
#     print(char)

# input_strinf = input("Enter a string: ")
# modified_string = ""
# vowels = "AEIOU"
# for char in input_strinf:
#     upper_char = char.upper()
#     if upper_char in vowels:
#         modified_string += "*"
#     else:
#         modified_string += upper_char
# print("Modified string:", modified_string)

# for i in range(5):
#     print(i)
# for i in range(3,10):
#     print(i)
# for i in range(1,11,2):
#     print(i)

# print("Number\tSquare")
# print("--------------")
# for number in range(1,11):
#     square = number**2
#     print(number,'\t',square)

# print("KPH\tMPH")
# print("--------------")
# for KPH in range(60,131,10):
#     MPH = KPH*0.6214
#     print(KPH,'\t%.2f' %MPH)
# print("MPH\tKPH")
# print("--------------")
# for MPH in range(60,131,10):
#     KPH = MPH *1.609344
#     print(MPH,'\t%.2f' %KPH)

# count = 0
# while count < 5:
#     print("Hello: ",count)
#     count += 1
    
# keep_going = "y"

# while keep_going == "y" :
#     sales = float(input("Enter the amount of sales: "))
#     comm_rate = float(input("Enter the commission rate: "))
#     commission = sales * comm_rate
#     print(f'The commission is ${commission:.2f}')
#     keep_going = input("Do you want to calculate another" + \
#         " commissin (Enter y for yes):")

# keep_going = "y"

# while keep_going == "y" :
#     sales = float(input("Enter the item's wholesale cost: "))
#     resale = sales * 2.5
#     print(f'Retail price ${resale:.2f}')
#     keep_going = input("Do you want to calculate another" + \
#         " commissin (Enter y for yes):")

# rows = int(input('How many rows: '))
# columns = int(input('How many columns: '))

# for star in range(rows * columns): 
#     if (star+1) % columns == 0 :
#         print('')
#     else:
#         print("*",end="")

# score = int(input("Enter a test score: "))

# while score < 0 or score > 100:
#     print("ERROR: The score cannnot br negative")
#     print("or greater than 100.")
#     score = int(input("Enter the correct score: "))

# for letter in "Attakon Jansanit":
#     if letter == "a" or letter == "k":
#         continue
#     print("Current Letter:",letter)
# for letter in "Attakon Jansanit":
#     if letter == "a" or letter == "k":
#         break
#     print("Current Letter:",letter)
# for letter in "Attakon Jansanit":
#     if letter == "a" or letter == "k":
#         pass
#     print("Current Letter:",letter)

# numbers = [6,5,3,8,4,2,5,4,11]
# sum=0
# for val in numbers:
#     sum += val 
#     print(sum)
# print("The sum is",sum)

# max = int(input("Enter yot range: "))
# total = 0.0
# print("This program calcullates the sum of")
# print(max,"number you will enter.")

# for counter in range(max):
#     number = int(input("Emter a number: "))
#     total = total + number
# print("The total is ",total)

# for i in range(1,3):
#     for j in range(2,5):
#         print(i,j)

# for i in range(4):
#     for j in range(i):
#         print(i,j)

# for hours in range(24):
#     for minutes in range(60):
#         for seconds in range(60):
#             print(hours,":",minutes,":",seconds)

rows = int(input('How many rows: '))

for star in range(100): 
    print(star+1, end=" ")
    if (star+1) % rows == 0:
        print('')