cells = input("Enter cells: ")

# Вывод игрового поля
print("---------")
print(f"| {cells[0]} {cells[1]} {cells[2]} |")
print(f"| {cells[3]} {cells[4]} {cells[5]} |")
print(f"| {cells[6]} {cells[7]} {cells[8]} |")
print("---------")

# Подсчет количества X, 0 и пустых клеток
x_count = cells.count('X')
o_count = cells.count('O')
empty_count = cells.count('_')

# Проверка возможных победных линий
def check_win(char):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # горизонтали
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # вертикали
        (0, 4, 8), (2, 4, 6)             # диагонали
    ]
    return any(cells[a] == char and cells[b] == char and cells[c] == char for a, b, c in wins)

x_wins = check_win('X')
o_wins = check_win('0')

# Логика определения состояния игры
if abs(x_count - o_count) >= 2 or (x_wins and o_wins):
    print("Impossible")
elif x_wins:
    print("X wins")
elif o_wins:
    print("0 wins")
elif empty_count > 0:
    print("Game not finished")
else:
    print("Draw")