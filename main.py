#Sukhnain Deol
#4/21/22
#2.6 TicTacToe Completed

#prints the numbered board and the one the game is played on
def print_key_n_board():
  print("\nKey\n\n" + board_display[0] + '|'+ board_display[1] + '|' + board_display[2] + '\n-----------\n' + board_display[3] + '|'+ board_display[4] + '|'+ board_display[5] + '\n-----------\n' + board_display[6] + '|'+ board_display[7] + '|'+ board_display[8] + '\n\nBoard\n\n' + board[0] + '|'+ board[1] + '|' + board[2] + '\n-----------\n' + board[3] + '|'+ board[4] + '|'+ board[5] + '\n-----------\n' + board[6] + '|'+ board[7] + '|'+ board[8])

#checks if any combination of 3 in a row or diagonal is on the board and declares the winner
def win_checker(x):
  if (board[0] == x and board[1] == x and board[2] == x) or (board[3] == x and board[4] == x and board[5] == x) or (board[6] == x and board[7] == x and board[8] == x) or (board[2] == x and board[5] == x and board[8] == x) or (board[1] == x and board[4] == x and board[7] == x) or (board[0] == x and board[3] == x and board[6] == x) or (board[0] == x and board[4] == x and board[8] == x) or (board[2] == x and board[4] == x and board[6] == x):
    print('\n' + x + ' wins.')
    global game_won 
    game_won = True
    
#declaring variables  

game_won = False

restart = True

placement_checker = 0

turn = 'X'

placement = None

turn_num = 0 

board_key = [' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ', ' 9 ']

board_display = [' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ', ' 9 ']

board = ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ']       

#start of game
print_key_n_board()

#stops the game once 9 turns are complete
while turn_num < 9 and restart == True:
  #checks if the input value is valid
  while placement_checker != 1:
    placement = input("\n Hello " + turn + ", what number do you want to place '" + turn + "' at?: ")
    if placement.isnumeric() == False or int(placement) > 9 or int(placement) < 1:
      print("\nInvalid Input")
    else: 
      placement_checker = 1

  placement = ' ' + placement + ' '
    #updates board value(s)
  if board[int(placement) - 1] != ' X ' and board[int(placement) - 1] != ' O ':
    board[board_key.index(placement)] = ' ' + turn + ' '
    board_display[board_key.index(placement)] = '   '

    print_key_n_board()
  
    turn_num = turn_num + 1

    win_checker(' ' + turn + ' ')
    
    #switches turns
    if turn == 'X':
      turn = 'O'
    else: 
      turn = 'X'
  else: 
    print("\nTile Occupied. please choose a different tile.")
      
  placement_checker = 0

  if game_won == True:
   break
