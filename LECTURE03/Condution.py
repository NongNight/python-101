#อายุ---------------------------------------------
# age = int(input("อายุของคุณคือเท่าไหร่:"))
# if age >= 18 :
#     print("คุณแก่แล้ว")

#เกรด--------------------------------------------
# score = int(input("กรอกคะแนนของคุณ: "))
# if score >= 80 and score <=100 :
#     print("เกรดของคุณคือ A")
# elif score >= 70 :
#     print("เกรดของคุณคือ B")
# elif score >= 60 :
#     print("เกรดของคุณคือ C")
# elif score >= 50 :
#     print("เกรดของคุณคือ D")
# elif score <= 49 and score >= 0 :
#     print("เกรดของคุณคือ F")
# else :
#     print("คุณกรอกข้อมูลไม่ถูกต้อง")

#ค่าเฉลี่ยคะแนน-------------------------------------
# score1 = int(input("Enter the score test 1:"))
# score2 = int(input("Enter the score test 2:"))
# score3 = int(input("Enter the score test 3:"))

# average = (score1 + score2 + score3) / 3
# print(average)
# if average > 95 and average <= 100:
#     print("Congtatulation")
#     print("That is a great average")
# else : 
#     print("That is a great Error")

#ขนาดบริษัท-----------------------------------------
# num_employees = int(input("Enter the number of employees:"))

# if num_employees >= 1 and num_employees <=50 :
#     print("This is a small company")
# elif num_employees > 50 and  num_employees < 250:
#     print("This is a medium company")
# elif num_employees >= 250 :
#     print("This is a large company")
# else:
#     print("This is Error")

#หาอักระ
# inchar = input("Input one character:")
# if inchar >= 'A' and inchar <='Z':
#      print("You in put Upper Case Letter" , inchar)
# elif inchar >= 'a' and inchar <='z':
#     print("You in put Lower Case Letter" , inchar)
# elif inchar >= '0' and inchar <='9':
#     print("You in put Number" , inchar)
# else : 
#     print("It's not a letter or number.", inchar)

#คิด
# # num = float(input("Enter a number: "))
# # if num > 0 :
# #     print("Positive number")
# # elif num == 0:
# #     print("Zero")
# # else:
# #     print("Nedative number")
    
# num = float(input("Enter a number:"))
# if num >= 0:
#     if num == 0 :
#         print("Zero")
#     else:
#         print("Positive number")
# else:
#     print("Nedative number")

# #operators
# x = 10 
# y = 20
# print(x==y) #F
# print(x!=y) #T
# print(x>y)  #F
# print(x<y)  #T
# print(x>=y) #F
# print(x<=y) #F

# s1 = "Sun"
# s2 = "Sun"

# if s1 == s2:
#     print(f'"{s1}"and"{s2}"are equal.')
# else:
#     print(f'"{s1}" and "{s2}" are not equal.')
    
# if s1 < s2:
#     print(f'"{s1}"come before "{s2}"in lexicographical order')
# elif s1 < s2 :
#     print(f'"{s1}" come after "{s2}" are not equal.')
    
# if s1 == s2:
#     print(f'"{s1}"and"{s2}"are equal.')
# else:
#     print(f'"{s1}" and "{s2}" are not equal.')

# x = 10 
# y = 20
# z = 30
# if x < y and y < z :
#     print("x is less than y and y is less than z.")
    
# if x < y or y > z :
#     print("Either x is less than y or y is greater than z.")

# if not (x > y):
#     print("x is not greater than y.")

# a = [1,2,3]
# b = a
# c = [1,2,3,]
# d = [1,2,3,]
# print(a is b)
# print(a is c)
# print(a is d)
# print(a == c)
# print(a == d)

# fruits = ["apple", "banana", "chrerry"]
# print("banana" in fruits)
# print("orange" in fruits)

# print("grape" not in fruits)
# print("apple" not in fruits)

# sentence = "The quick brown fox junps over the lazy bog"

# print("fox" in sentence)
# print("cat"not in sentence)

# age = int(input("อายุเท่าไหร่: "))
# income = int(input("เงินเดือนเท่าไหร่: "))
# if age >=18 and age <=65 and income > 3000:
#     print("You are eligible for the loan")
# else:
#     print("You are not eligible for the loan")

hour = int(input("H: "))
rage = int(input("R: "))

if hour<=40:
    sum = hour*rage
    print("s = ",sum)

elif hour>40:
    ot=hour-40
    s=ot*(1.5*rage)
    n = (rage*40)+s
    print("n: ",n)



















