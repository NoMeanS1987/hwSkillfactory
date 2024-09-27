field = [1, 2, 3, 4, 5, 6, 7, 8, 9]

winlines = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]

i = 0
moves = list()
def showfield():
    print(field[0], end=" ")
    print(field[1], end=" ")
    print(field[2])

    print(field[3], end=" ")
    print(field[4], end=" ")
    print(field[5])

    print(field[6], end=" ")
    print(field[7], end=" ")
    print(field[8])


def motion(move, symbol):
    ind = field.index(move)
    field[ind] = symbol


def get_result():
    win = ""

    for i in winlines:
        if field[i[0]] == "X" and field[i[1]] == "X" and field[i[2]] == "X":
            win = "X"
        if field[i[0]] == "O" and field[i[1]] == "O" and field[i[2]] == "O":
            win = "O"

    return win


game_over = False
game = True

while game_over == False:

    showfield()

    if game == True:
        symbol = "X"
        move = input("Игрок 1, ваш ход: ")
        while move.isdigit() == False:
            print('Принимаем только целые значения от 1 до 9')
            move = input("Игрок 1, ваш ход: ")
        move = int(move)
        while move > 9 or move <= 0:
            print('Не попали по полю!')
            move = input("Игрок 1, ваш ход: ")
        if move in moves:
            print('Клетка занята')
            move = input("Игрок 1, ваш ход: ")
        moves.append(move)

    else:
        symbol = "0"
        move = input("Игрок 2, ваш ход: ")
        while move.isdigit() == False:
            print('Принимаем только целые значения от 1 до 9')
            move = input("Игрок 2, ваш ход: ")
        move = int(move)
        while move > 9 or move <= 0:
            print('Не попали по полю!')
            move = input("Игрок 2ad, ваш ход: ")
        if move in moves:
            print('Клетка занята')
            move = input("Игрок 2, ваш ход: ")
        moves.append(move)

    motion(move, symbol)
    win = get_result()
    if win != "":
        game_over = True
    else:
        game_over = False

    i=i+1
    if i==9:
        print('Ничья!')
        win = 'дружба'
        break

    game = not (game)


showfield()
print("Победил", win)

