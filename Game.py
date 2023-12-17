def description():
    print("Добро пожаловать в игру крестики-нолики")
    print('---------ПРАВИЛА ИГРЫ---------')
    print('1.Игроки ходят по очереди. Сначала X потом O')
    print('2.Побеждает тот у кого будет три в ряд')
    print("3.Формат ввода: \"x y\"")
    print('x - номер строки')
    print('y - номер столбца')

def playingField(field):
    print()
    print('   0 | 1 | 2 |')
    print("  --------------")
    for i, row in enumerate(field):
        row_str = f"{i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------")
    print()

def get_player_move():
    while True:
        move = input('   Ваш ход: ').split()
        if len(move) != 2:
            print("Введите две координаты!!")
            continue
        x, y = map(int, move)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Координаты вне диапазона!!")
            continue
        return x, y

def checkWin(field):
    win_combinations = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for comb in win_combinations:
        symb = []
        for c in comb:
            symb.append(field[c[1]][c[0]])
            if symb == ['X','X','X']:
                return True
            if symb == ['O','O','O']:
                return True
    return False
def make_move(field,x,y,symbol):
    if field[x][y] != " ":
        print("Клетка занята!!")
        return False
    field[x][y] = symbol
    return True

def TicTacToe():
    description() #Вызов функции с правилами игры
    field = [[" "] * 3 for i in range(3)] #Создаем поле из массивов
    count = 0 # <-- Это счетчик ходов
    while True:
        count += 1
        playingField(field)
        if count % 2 != 0:
            print("Ходит - Х")
        else:
            print("Хотит - О")
        x, y = get_player_move()
        if count % 2 != 0:
            symbol = "X"
        else:
            symbol = "O"
        if not make_move(field,x, y, symbol):
            count -= 1
            continue
        if checkWin(field):
            playingField(field)
            if count % 2 != 0:
                print("X - WIN")
            else:
                print("O - WIN")
            break
        if count == 9:
            playingField(field)
            print("Ничья")
            break
TicTacToe()



