ticboard = ['-','-','-',
          '-','-','-',
          '-','-','-']
          
game_still_occuring = True
winner = None 

player_cur = 'x' 

def print_board():
 print(board[0] + board[1] + board[2])
 print(board[3] + board[4] + board[5])
 print(board[6] + board[7] + board[8])
   
def play_the_game():
    print_board()
    
    while game_still_occuring
    
     turn(player_cur)
     check_over()
     flip()
    if winner == 'x' or winner == 'o':
        print( winner + "won!!") 
    elif winner == None:
        print("Tie!!")
        

def turn(player):
    print("it's " + player + "'s turn"
    pose = input("choose a position (pick only between 1-9)")
    
    valid = False
    while not valid:
    
     while position not in ["1","2","3","4","5","6","7","8","9"]
      pose = input("Choose a position from 1-9")
      
     pose = int(pose)-1
    
     if ticboard[pose]= '-':
      valid = True
     else:
      print("You can't go there, try another")
     
    ticboard[pose] = player
    
    print_board()
def check_over():
    check_win()
    check_tie()
    
def check_win():

     global winner
     row_win = check_rows()
     column_win = check_columns()
     diagonal_win = check_diagonals():
     if row_winner():
      winner = row_win
     elif column_winner:
      winner = column_win
     elif diagonal_winner:
      winner = diagonal_win
     else:
      winner = None
     return
def flip():
        global player_cur
        if player_cur == "x":
         player_cur = "o"
        elif player_cur == "o":
         player_cur = "x"
        
def check_tie():
    global game_still_occuring
    
    if "-" not in board:
        game_still_occuring=False
        return True
    else:
     return False 
def check_rows():
    global game_still_occuring
    row_1 = ticboard[0] == ticboard[1] == ticboard[2] != '-'
    row_2 = ticboard[3] == ticboard[4] == ticboard[5] != '-'
    row_3 = ticboard[6] == ticboard[7] == ticboard[8] != '-'
    if row_1 or row_2 or row_3:
        game_still_occuring = False
    if row_1:
     return board[0]
    elif row_2:
     return board[3]
    elif row_3:
     return board[6]
    else 
     return None
def check_columns():

    global game_still_occuring
    column_1 = ticboard[0] == ticboard[3] == ticboard[6] != '-'
    column_2 = ticboard[1] == ticboard[4] == ticboard[7] != '-'
    column_3 = ticboard[2] == ticboard[5] == ticboard[8] != '-'
    if column_1 or column_2 or column_3:
        game_still_occuring = False
    if column_1:
     return board[0]
    elif column_2:
     return board[1]
    elif column_3:
     return board[2]
    else:
     return None
def check_diagonals():
    global game_still_occuring
    diagonal_1 = ticboard[0] == ticboard[4] == ticboard[8] != '-'
    diagonal_2 = ticboard[2] == ticboard[4] == ticboard[6] != '-'
    if diagonal_1 or diagonal_2:
      game_still_occuring = False
    if diagonal_1:
     return board[0]
    elif diagonal_2:
     return board[2]
    else:
     return None
play_the_game()
    
    
