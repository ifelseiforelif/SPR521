# # print("Hello World", sep=" ", end="!\n")
# # print("Hello World", sep=" ", end="!\n")
# # print('Hello World',3,4,4.5, sep=" ", end="!\n")
# """
# Багатостроковий 
# коментар
# """


# # age = 22 # int (integer) - цілочисельна змінна
# # price = 45.7 # float - змінна дійсного типа
# # name = "Ivan" # str - рядок 
# # isSuccess = False # bool (True - 1, False - 0)

# # print("Вік: ", age)
# # age = age//5 # + - * /  //
# # print("Вік: ", age)

# # print("Ціна: ", price)
# # print("Імя: ", name)


# # ctrl /  

# # a = 25
# # a=a-5
# # print(a//10) #30
# # print(a) #20

# # print(2**3) # 2*2*2
# # print(10**2) # 10*10

# # print(10%4)
# # print(5%2) 
# # print(22%7)
# # print(11%3)

# # t = input("Введіть число: ")

# # print(t*2)

# # print("\033[31mHello\033[0m")
# # print("\033[32mWorld\033[0m")
# # print("\033[34mСиній текст\033[0m")

# # price = 3.4
# # print(type(price))
# # price = 4
# # print(type(price))
# # price = bool(1)
# # print(type(price))
# # print(price)
# # print(type(False)) #int
# # Створити 3 змінні. Кількість продуктів на складі, ціна продукта і
# #вага продукта.
# #Запити у користувача та вивести у консоль
# a = "Hello "
# b = "World"
# print(a+b) # Конкатенація - склейка рядків
# # Операнд
# # Оператор +, -, *, /, //, **, %, ==, !=, >, <, >=, <=, =
# # Вираз - це правильна сукупність операндів та операторів,
# #  яка призводить до результату та має тип даних

# #Перетворення типів
# # a = True
# # b = 10
# # c = 2.3
# # print(a+b+c)

# # a = 2
# # b = 3+2**2
# # print(2*2**2)

# print(3>=1) # True
# print(3<=1) # False
# print(3!=1) # True
# print(3==1) #False
# # Унарні, бінарні, тернарний
# # Схема бінарного оператора Операнд1 Оператор Операнд2
# #2+3   2-3   2*9  2>5 
# #Схема унарного оператор
# # Оператор Операнд
# # Операнд Оператор
# # -2
# # +3

# # print( ((3<2) and (4<7)) )


# print(not (True and False))
# a = True; 
# b = False; 
# print(True or False and not True)

#productName = None
# productName = input("Enter name: ")
# productPrice = float(input("Enter price: "))
# productCount = int(input("Enter count: "))

# Загальний результат по продукту Ім'яПродукта за кількість Кількість
#=result
#інтерполяція
# print(f"{1+9}")
# print(f"Загальний результат по продукту {productName} за кількість "
#       f"{productCount} = {productCount*productPrice}")



# name = input("Enter name: ")
# surname = input("Enter surname: ")
# print(name+" "+surname)
# print(f"Welcome, {name}  {surname}")
# print("Welcome, ", name,"  ",surname, sep="")


# price = float(input("enter price: "))
# count = input("enter count: ")
# print(price*count)
# print("Hello World")
# print("*"*20)
# print("Hello World")
#print("Hello "+"World")

# f = 2.3
# print(int(f))
# x = 0
# y = 0
# x = int(input("x: "))
# y = int(input("y: "))
# res = x*y
# print(res)
"""
Оператори: бінарні, унарні, тернарний
Оператори порівняння, логічні

"""
x = int(input("Enter x: "))
if x==2 or x==3:
    print("x = 2 or x = 3")
elif x==7 or x==10:
       print("x = 7 or x = 10")
else:
      print("not found")
# if x>0:
#     print("X>0")
# elif x==0:
#     print("x=0")
# else :
#     print("X<0")
# Створити програму, яка запитує зріст людини та якщо зріст меньше або дорівнює 140
# напишемо у консоль small
# якщо зріст >140 а меньше 155 напише middle
# інакше напишемо big