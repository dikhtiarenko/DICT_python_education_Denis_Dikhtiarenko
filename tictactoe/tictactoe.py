# Инициализация пустого поля (9 пустых клеток)
cells_list = [' ' for _ in range(9)]


def print_field(c):
    print("---------")
    print(f"| {c[0]} {c[1]} {c[2]} |")
    print(f"| {c[3]} {c[4]} {c[5]} |")
    print(f"| {c[6]} {c[7]} {c[8]} |")
    print("---------")


# Словарь для точного сопоставления координат (строка, столбец) и индексов списка
coord_map = {
    (1, 1): 6, (1, 2): 3, (1, 3): 0,
    (2, 1): 7, (2, 2): 4, (2, 3): 1,
    (3, 1): 8, (3, 2): 5, (3, 3): 2
}


def check_win(board, char):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    return any(board[a] == char and board[b] == char and board[z] == char for a, b, z in wins)


# Выводим начальное пустое поле
print_field(cells_list)

current_player = 'X'

while True:
    user_input = input("Enter the coordinates: ").split()

    # Проверка: введены ли ровно 2 значения и являются ли они цифрами
    if len(user_input) != 2 or not user_input[0].isdigit() or not user_input[1].isdigit():
        print("You should enter numbers!")
        continue

    row, col = int(user_input[0]), int(user_input[1])

    # Проверка диапазона от 1 до 3
    if row not in (1, 2, 3) or col not in (1, 2, 3):
        print("Coordinates should be from 1 to 3!")
        continue

    index = coord_map[(row, col)]

    # Проверка, занята ли ячейка
    if cells_list[index] != ' ':
        print("This cell is occupied! Choose another one!")
        continue

    # Делаем ход текущим игроком
    cells_list[index] = current_player
    print_field(cells_list)

    # Проверка состояния игры
    x_wins = check_win(cells_list, 'X')
    o_wins = check_win(cells_list, '0')
    empty_count = cells_list.count(' ')

    if x_wins:
        print("X wins")
        break
    elif o_wins:
        print("0 wins")
        break
    elif empty_count == 0:
        print("Draw")
        break

    # Смена игрока
    current_player = '0' if current_player == 'X' else 'X'