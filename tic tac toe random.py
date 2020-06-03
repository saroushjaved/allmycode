
import random

c = 0
b_v = [0,1,2,3,4,5,6,7,8]

def avaliable_spots():
    cells =[]
    for i in range (len(b_v)):
        if str(b_v[i]).isdigit():
            cells.append(b_v[i])
    return cells 
             
def board():
    print(str(b_v[0]) +"  |  " + str(b_v[1])+ "  |  " + str(b_v[2]))
    print("---------------")
    print(str(b_v[3]) +"  |  " + str(b_v[4])+ "  |  " + str(b_v[5]))
    print("---------------")
    print(str(b_v[6]) +"  |  " + str(b_v[7])+ "  |  " + str(b_v[8]))

def player1_move():
    
    print()
    player_position = int(input( " Enter where you want to place X : " ) )
    if b_v[player_position] == "X" or b_v[player_position] == "O":
        print("Invalid Move")
        c = 0
        return c
    else:
        b_v[player_position] = "X"
        c = 1
        return c


def player_pos(cells):
    return random.randint(0,8)
       
def player2_move():

    player_position = player_pos(avaliable_spots())
    if b_v[player_position] == "X" or b_v[player_position] == "O":
            print("Invalid Move")
            c = 1
            return c
    else:
             b_v[player_position] = "O"
             c = 0
             return c


def playmove():
        global c
        if c == 0:
            c = player1_move()
        else:
         
            c = player2_move()

def win():

        winlis=[]
        winner = None 
               
        if b_v[0] == b_v[4] == b_v[8] :
                   print("Player " + b_v[0] + " IS WINNER ")
                   winchk = 1
                   winner = b_v[4]
                   
        elif b_v[2] == b_v[4] == b_v[6]:
                   print("Player " + b_v[2]  + " IS WINNER ")
                   winner = b_v[2]
                   winchk = 1
    
        elif b_v[0] == b_v[1] == b_v[2] == "X" or b_v[3] == b_v[4] == b_v[5] == "X" or b_v[6] == b_v[7] == b_v[8] == "X":

                print (" Player X is Winner")
                winner = "X"
                
      
        elif b_v[0] == b_v[1] == b_v[2] == "O" or b_v[3] == b_v[4] == b_v[5] == "O" or b_v[6] == b_v[7] == b_v[8] == "O":

                print (" Player O is Winner")
                winner = "O"
                
        elif b_v[0] == b_v[3] == b_v[6] =="X" or b_v[1] == b_v[4] == b_v[7] =="X" or b_v[3] == b_v[5] == b_v[8] == "X" :
                print (" Player X is Winner")
                winner = "X"
                winchk = 1
                
        elif b_v[0] == b_v[3] == b_v[6] =="O" or b_v[1] == b_v[4] == b_v[7] == "O" or b_v[3] == b_v[5] == b_v[8] == "O" :
                print (" Player O is Winner")
                winner = "O"
        else:
            winner = None 
                
    
        return winner
    
def draw():
    
    draw_chk = 0
    string_draw = "".join(str(b_v))

    cont= any(stri.isdigit() for stri in string_draw)

    if cont == True:
        pass
    else:
        print()
        print()
        print("Game is Drawn")
        drchk = 1

    return draw_chk



while True:
    
    drawcheck = draw()
    wincheck = win()
    board()

    if drawcheck == 0 and wincheck == None:       
            print()
            print()
            print()
            playmove()
            print()
            win()
            draw()     
    else:
        print()
        print("GAME IS OVER...HAVE FUN")
        break


    
    
