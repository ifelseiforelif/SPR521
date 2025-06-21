# d=float(input("Enter the diameter of the circle: "))
# choice = int(input("Enter 1 - Square, 2 - Perimetr: "))
# PI=3.14
# if choice==1:
#     s = (PI*(d**2))/4 # Задача 2
#     print(f"square:{s}")
# elif choice==2:
#     p = PI*d
#     print(f"perimeter:{p}")
# else:
#     print("Error")

#Унарні, бінарні, тернарний

# age = int(input("Enter age: "))
# result = "Yes" if age>=18 else "No"
# print("є доступ" if age>=18 else "немає доступа")

# if age>=18:
#     print("є доступ")
# else:
#     print("немає доступ")

# value = int(input("Enter number: "))
# result = "+" if value>0 else ("-" if value<0 else "0" )
# print(result)

# day = int(input("Enter day (1-7)"))
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case _:
#         print("Day not found")
        
# month = input("Enter month: ")
# match month:
#     case 'June'|'July'|'August':
#         print("Summer")
#     case 'September'|'October'|'November':
#         print('Autumn')
#     case _: #default case (else)
#         print('Month not found')
#Debugger практика цикли

# year = int(input("Enter year: "))
# if year%4==0 and (year%100!=0 or year%400==0):
#     print("Year is Leap")
# else:
#     print("Year is not leap")

#цикли
# i=10
# k=-5
# while i<20:
#     print(k)
#     k*=2
#     i=i+1 # i+=1

# 10 9 8 .... 0

i=30
while i>0:
    if i%3==0 and i%2==0:
        print(i, end='\t')
    i-=1                    

# t = 10
# t+=5 # t=t+5
# t*=5
# t/=5
# t-=5
