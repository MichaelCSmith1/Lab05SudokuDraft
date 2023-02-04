import json


def read_board(filename):

    # Read the file if it exists.
    try:
        file = open(filename, "r")
        board_text = file.read()
        board_json = json.loads(board_text)
        return board_json['board']

    except:
        print("Error reading file.")

def write_board(board):
    save_file = input("Enter a file to save the board to:")
    with open(save_file, 'w') as file:
        board_json = {}
        board_json['board'] = board
        board_text = json.dumps(board_json)
        file.write(board_text)

def display_boardTest(board):
    count = 1
    print("   A B C D E F G H I")
    for row in range(0, 9):
        if (row == 3 or row == 6):
            print("  -----+-----+-----")
        print(f"{count}  {board[row]}")
        count += 1

def parse_input(coordinate):
    for letter in coordinate:
        # if 'a' <= letter <= 'z':    
        # if 1 <= int(letter) <= 9:
        if letter == coordinate[0]:
            row = int(ord(letter.lower()) - 96) - 1
        else:
            column = int(letter) - 1
    return (row, column)

def play_round(board, game_playing):
    while game_playing == True:
        print("Specify a coordinate to edit or 'Q' to save and quit")
        coordinate = input("> ")
        if coordinate == 'Q' or coordinate == 'q':
            write_board(board)
            game_playing = False
        else:
            number = int(input(f"What number goes in {coordinate}? "))
            (row, column) = parse_input(coordinate)
            board[column][row] = number
            display_boardTest(board)

game_playing = True
filename = input("What board would you like to open: ")
board = read_board(filename)
display_boardTest(board)

play_round(board, game_playing)
    
   
