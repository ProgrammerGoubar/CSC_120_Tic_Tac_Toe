ticboard = [['-','-','-'],
          ['-','-','-'],
          ['-','-','-']]
          
game_still_occuring = True
winner = None 

current_player = 'x' 

def print_board():
 for row in ticboard:
 print(row)
   
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
    pose = input("choose a position (pick only between 1-9)")
    pose = int(pose)-1
    
    ticboard[pose]= 'x'
    
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
      winner = row_win()
     elif column_winner:
      winner = column_win()
     elif diagonal_winner:
      winner = diagonal_win()
     return
     
def check_tie():

    return
def check_rows():
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
    return
def check_columns():
    return
def check_diagonals():
    return
play_the_game()
    
    
