game = "_" * 9
rows = [[i for i in game[n:n + 3]] for n in range(0, 7, 3)]


def print_game(table):
    print("---------")
    for i in range(3):
        print(f"| {table[i][0]} {table[i][1]} {table[i][2]} |")
    print("---------")


def validate_winner(table):
    cols = [[r[i] for r in table] for i in range(3)]
    diagonal = [[table[i][i] for i in range(3)]]
    back_diagonal = [[table[i][2 - i] for i in range(3)]]

    matrix = table + cols + diagonal + back_diagonal
    count_x = sum([r.count("X") for r in table])
    count_o = sum([r.count("O") for r in table])
    x_game = ["X", "X", "X"]
    o_game = ["O", "O", "O"]
    x_wins = x_game in matrix
    o_wins = o_game in matrix
    if abs(count_x - count_o) > 1 or (x_wins and o_wins):
        print("Impossible")
    elif x_wins:
        print("X wins")
        return True
    elif o_wins:
        print("O wins")
        return True
    elif (count_o + count_x) == 9:
        print("Draw")
        return True
    return False




print_game(rows)

input_valid = False
players = ["O", "X"]
turn = True
while not input_valid:
    try:
        x, y = [int(n) for n in input().split()]
        if not (1 <= x <= 3) or not (1 <= y <= 3):
            print("Coordinates should be from 1 to 3!")
            continue
        if rows[x - 1][y - 1] != '_':
            print("This cell is occupied! Choose another one!")
            continue

        rows[x - 1][y - 1] = players[turn]
        turn = not turn
        print_game(rows)
        if validate_winner(rows):
            input_valid = True
    except ValueError:
        print("You should enter numbers!")


