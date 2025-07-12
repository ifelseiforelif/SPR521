# sum = 0
# while True: # вічний цикл
#     number = int(input("Enter number: "))
#     if number==0:
#         print("Bye")
#         break # завершує цикл
#     sum+=number
# print(f"Sum: {sum}")

# i = 0
# sum = 0
# while i<30:
#     if i%2!=0:
#         i+=1
#         sum+=i
#         continue
#     elif i%2==0:
#         print('\n',i)
#     i+=1

# i = 0
# while i < 10:
#     print(i)
#     if i == 3:
#         break
#     i += 1

# i = 0
# while i < 5:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

# import random
# sum = 0
# even = 0 #парні
# odd = 0 #непарні
# for i in range(5):
#     num =random.randint(-10,10)
#     if num%2==0:
#         even+=1
#     else:
#         odd+=1
#     print(num, end=' ') 
#     sum+=num # сума
# print("Sum: ", sum)
# print("Even: ", even)
# print("Odd: ", odd)
# import random
# print("Старт гри")
# while True:
#     choice = int(input(" Камінь ✊ - 1 \n Ножиці 🤞 - 2 \n Бумага ✋ - 3 \n Зробіть вибір: "))
#     if choice!=1 and choice!=2 and choice!=3:
#         print("Невірний вибір")
#     else:
#         #Гра починається
#         pc_choice = random.randint(1,4) # 1,2,3
#         print("Вибір PC: ")
#         print("Камінь ✊" if pc_choice==1 else ("Ножиці 🤞" if pc_choice==2 else "Бумага ✋"))
#         if choice==pc_choice:
            
#             print("Ничья")
#         elif (choice==1 and pc_choice==2) or (choice==2 and pc_choice==3) or (choice==3 and pc_choice==1):
#             print("Вітаю, Ви виграли")
#         else:
#             print("Ви програли")

# import random

# print("Start Game")
# pcw = 0
# plw = 0
# draw = 0
# games = 0
# userWish = "play"
# while userWish == "/play" or userWish == "play":
#     whatChoose = ["stone", "shears", "paper"]
#     choose = input("chose stone🪨, shears✂️ or paper📜 ").lower()
#     i = 0
#     choosePCConvert = ""
#     while i < 3:
#         if choose == whatChoose[i]:
#             print("Wait pc")
#             break
#         elif i == 2 and choose != whatChoose[i]:
#             print("Error")
#         else:
#             print("wait..")
#         i += 1
#     choosePC = random.randint(1, 3)
#     random.sample(["stone", "shears", "paper"])
#     if choosePC == 1:
#         choosePCConvert = "stone"
#     elif choosePC == 2:
#         choosePCConvert = "shears"
#     elif choosePC == 3:
#         choosePCConvert = "paper"
#     else:
#         print("error")
#     print("The game has begun")
#     games += 1
#     if choosePCConvert == choose:
#         print(f" Pc choose: {choosePCConvert}\n Player choose: {choose}\n DRAW😐")
#         draw += 1
#     elif choosePCConvert == whatChoose[0] and choose == whatChoose[1]:
#         print(f" Pc choose: {choosePCConvert}\n Player choose: {choose}\n You Lose☹️")
#         pcw += 1
#     elif choosePCConvert == whatChoose[1] and choose == whatChoose[2]:
#         print(f" Pc choose: {choosePCConvert}\n Player choose: {choose}\n You Lose☹️")
#         pcw += 1
#     elif choosePCConvert == whatChoose[2] and choose == whatChoose[0]:
#         print(f" Pc choose: {choosePCConvert}\n Player choose: {choose}\n You Lose☹️")
#         pcw += 1
#     elif choosePCConvert == whatChoose[2] and choose == whatChoose[1]:
#         print(f" Pc choose: {choosePCConvert}\n Player choose: {choose}\n You Won😁")
#         plw += 1
#     elif choosePCConvert == whatChoose[0] and choose == whatChoose[2]:
#         print(f" Pc choose: {choosePCConvert}\n Player choose: {choose}\n You Won😁")
#         plw += 1
#     elif choosePCConvert == whatChoose[1] and choose == whatChoose[0]:
#         print(f" Pc choose: {choosePCConvert}\n Player choose: {choose}\n You Won😁")
#         plw += 1
#     else:
#         print("Error")
#     userWish = input(f"Command:\n /stats - all stats\n /play - play again\n").lower()
#     if userWish == "play" and userWish == "/play":
#         continue
#     else:
#         print(f" You won: {plw}\n Pc won: {pcw}\n Draws: {draw}\n Games: {games}")

# rows = int(input("Enter rows: ")) #к-ть рядків
# cols = int(input("Enter cols: ")) #к-ть стовбців
# symbol = input("Enter symbol: ")
# i=0
# while i<rows:
#     j=0
#     while j<cols:
#         print(symbol, end=' ')
#         j+=1
#     print('\n')
#     i+=1

# print()
# for i in range(2,10):
#     for j in range(1,10):
#         print(f"{i}*{j}={i*j}")
#     print('\n\n')
# i=2
# while i<=9:
#     j=1
#     while j<=9:
#         print(f"{i}*{j}={i*j}")
#         j+=1
#     print('\n\n')
#     i+=1


# rows = int(input("Enter rows: ")) #к-ть рядків
# cols = int(input("Enter cols: ")) #к-ть стовбців

# for i in range(0,rows):
#     k=5
#     l=2
#     for j in range(0,cols):
#         if i%2==0: #парний рядок
#             print(k, end=' ')
#             k+=1
#         else: #непарний рядок
#             print(l, end=' ')
#             l+=3
#     print()

# size = int(input("Enter size: "))
# for i in range(0,size):
#     for j in range(0,size):
#         if i==j:
#             print(1, end=' ')
#         else:
#             print(0, end=' ')
#     print()

#Рядки str - string
# str1 = "Hello World"
# str2 = 'Hello World'
# str3 = """
#  hello
#     world
#     I like
#     python
# """

# str4 = input()
# print(str1,str2,str3, str4)

#print(int(input())*2)

# str = "Hello World!"
# index = int(input("Enter index: "))
# if index>=0 and index<=len(str)-1:
#     print(str[index])
# str = "He  ll  o World !"
# i=0
# count=0
# while i<len(str):
#     if str[i]==' ':
#         count+=1
#     i+=1
# print(count)

# print("hello   wo  rld".count("l"))

# import random
# rows = int(input("Enter rows: "))
# cols = int(input("Enter cols: "))
# for i in range(rows):
#   min_number=130
#   max_number=30
#   for j in range(cols):
#     number = random.randint(30,130)
#     print(number, end=' ')
#     if number>max_number:
#       max_number=number
#     if number<min_number:
#       min_number=number
#   print(f"min={min_number}, max={max_number}")  
#   print()

# 97 a
#ord
#chr

# for i in range(65,65+26):
#     print(chr(i), end = ' ')
# print(ord('a'))

# print("hello".upper()) # верхній
# print("HeLlo".lower()) #нижній реєстр

# mes = "python"
# mesReverse = ''
# i=len(mes)-1 # індекс останього елемента 
# while i>=0:
#     mesReverse+=mes[i]
#     i-=1
# print(mesReverse)


# print('3'.isalpha())
# print('h'.isdecimal())

# row = """
#              *
#             ***
#            *****
# """
# print(row)

# split join
# fruits = ["orange", "lemon", "orange"]
# str_fruits = ':'.join(fruits)
# print(str_fruits)

# colors = "yellow,green,black".split(',')
# print(colors[0])

# str2 = "HeLlo"
# small = 0
# big = 0
# for char in str2:
#     if char.isupper():
#         big+=1
#     if char.islower():
#         small+=1
# print(f"Small : {small}, Big: {big}")

# pip install module
# shdhd jfjfjS Sjfjf kkfjs sjfj
# "world".startswith('s') #False
# "world".startswith('w') #True
# "world".endswith('d') #True
# "world".endswith('q') #False
# Зробити рядок (речення) (слова через пробелы)
# Порахувати скільки слів рядка починаються з літери s
# реєстр неважливий
