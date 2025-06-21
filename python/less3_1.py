# totalPrice = 15 # camel case
# total_price = 15 # snake case
# PI = 3.14
# DAYS_OF_WEEK = 7
# total = 10 #реєстрозалежна мова
# Total = 10

# price = True
# count = True
# x = 3.4
# print(True+True*x)
# + - / // * % > < >= <= == = != and or

# int(8>9) 
# 5>4 and 2<1
# name = "Alex"
# name2 = "John"

# print("Welcome", name, "and", name2)
# print(f"Welcome {name} and {2+4}") #інтерполяція

# num1 = int(input("Enter num1: ")) #3
# num2 = int(input("Enter num2: ")) #8
# if num1>num2:
#     print(f"Max: {num1}")
# elif num1==num2:
#     print(f"Equal: {num1}={num2}")
# else:
#      print(f"Max: {num2}")

# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))
# num3 = int(input("Enter num3: "))
# if num1==num2==num3:
#     print(f"{num1}={num2}={num3}")
#     if num1==3:
#         print("num1=3") 
# else: 
#     if num1>num2 and num1>num3:
#         print(f"Max: {num1}")
#     elif num2>num1 and num2>num3:
#         print(f"Max: {num2}")
#     else:
#         print(f"Max: {num3}")
# max = num1
# if num2>max:
#     max = num2

# if num3>max:
#     max = num3

# print(f"Max:  {max}")

# 45  4  5

# number = int(input("enter number: "))
# if number>=10 and number<=99:
#     n1 = number//10
#     n2 = number%10
#     print(f"n1={n1}, n2={n2}")
# else:
#     print("error")

number = int(input("enter number: ")) # 345  3  4  5
if number>=100 and number<=999:
    n1 = number//100
    n2 = (number%100)//10
    n3 = number%10
    print(f"n1={n1}, n2={n2}, n3={n3}")
else:
    print("error")

# number = int(input("enter number: "))

# if number >= 100 and number <= 999:
#     temp = number%100

#     n1 = number//100
#     n2 = temp//10
#     n3 = temp%10
#     print(f"n1={n1}, n2={n2}, n3={n3}")
# else:
#     print("error")
