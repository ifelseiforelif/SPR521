print("Натисніть Enter, щоб додати 1 бал. Напишіть 'стоп', щоб вийти.")

score = 0  # Змінна для рахунку

while True:
    user_input = input("> ")  # Запит вводу

    if user_input == "стоп":
        # Користувач хоче вийти
        break
    else:
        # Збільшуємо рахунок на 1
        score = score + 1
        print("Рахунок:", score)

# Кінець гри
print("Гра завершена. Загальний рахунок:", score)
