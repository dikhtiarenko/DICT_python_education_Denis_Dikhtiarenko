import random

# Запрос и проверка количества карандашей
while True:
    pencils_input = input("How many pencils would you like to use:\n> ")

    if not pencils_input.isdigit():
        print("The number of pencils should be numeric")
        continue

    pencils = int(pencils_input)

    if pencils <= 0:
        print("The number of pencils should be positive")
        continue

    break

# Игроки: John (человек) и Jack (бот)
player1 = "John"
player2 = "Jack"

while True:
    first_player = input(f"Who will be the first ({player1}, {player2}) :\n> ")
    if first_player == player1 or first_player == player2:
        break
    print(f"Choose between '{player1}' and '{player2}'")

current_player = first_player
next_player = player2 if current_player == player1 else player1

print("|" * pencils)

# Игровой цикл
while pencils > 0:
    print(f"{current_player}'s turn!")

    # Ход бота (Jack)
    if current_player == player2:
        # Стратегия бота
        if pencils == 1:
            take = 1
        elif pencils % 4 == 1:
            # Проигрышная позиция — берем случайное число (1, 2 или 3)
            take = random.randint(1, min(3, pencils))
        else:
            # Выигрышная позиция — оставляем сопернику остаток, кратный 4
            take = (pencils - 1) % 4
            if take == 0:
                take = 1

        print(take)

    # Ход человека (John)
    else:
        while True:
            take_input = input("> ")

            if take_input not in ['1', '2', '3']:
                print("Possible values: '1', '2' or '3'")
                continue

            take = int(take_input)

            if take > pencils:
                print("Too many pencils were taken")
                continue

            break

    # Уменьшаем количество карандашей
    pencils -= take

    # Если карандаши еще остались, выводим их и меняем игрока
    if pencils > 0:
        print("|" * pencils)
        current_player, next_player = next_player, current_player
    else:
        print(f"{next_player} won!")
        break