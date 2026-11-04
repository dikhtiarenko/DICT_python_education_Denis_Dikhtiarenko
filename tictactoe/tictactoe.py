cells = input("Enter cells: ")


# Функция для вывода игрового поля
def print_field(c):
    print("---------")
    print(f"| {c[0]} {c[1]} {c[2]} |")
    print(f"| {c[3]} {c[4]} {c[5]} |")
    print(f"| {c[6]} {c[7]} {c[8]} |")
    print("---------")


# Выводим начальное поле
print_field(cells)

# Превращаем строку в список, чтобы можно было менять символы
cells_list = list(cells)

# Словарь для перевода координат (строка, столбец) в индекс строки от 0 до 8
coord_map = {
    ('1', '3'): 0, ('2', '3'): 1, ('3', '3'): 2,
    ('1', '2'): 3, ('2', '2'): 4, ('3', '2'): 5,
    ('1', '1'): 6, ('2', '1'): 7, ('3', '1'): 8
}

while True:
    user_input = input("Enter the coordinates: ").split()

    # Проверка: введены ли ровно 2 значения и являются ли они числами
    if len(user_input) != 2 or not user_input[0].isdigit() or not user_input[1].isdigit():
        print("You should enter numbers!")
        continue

    row, col = user_input[0], user_input[1]

    # Проверка диапазона координат
    if row not in ('1', '2', '3') or col not in ('1', '2', '3'):
        print("Coordinates should be from 1 to 3!")
        continue

    index = coord_map[(row, col)]

    # Проверка, занята ли клетка
    if cells_list[index] != '_' and cells_list[index] != ' ':
        print("This cell is occupied! Choose another one!")
        continue

    # Делаем ход (ставим 'X')
    cells_list[index] = 'X'
    break

# Выводим обновленное поле
print_field("".join(cells_list))