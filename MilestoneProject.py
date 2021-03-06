from IPython.display import clear_output

p = [None, None, None, None, None, None, None, None, None, None]

#draw the board using format method
def DrawBoard():
    clear_output(False)
    print("{0:^8} | {1:^8} |{2:^8}".format(p[1],p[2],p[3]))
    print("{0:^8} | {1:^8} |{2:^8}".format(p[4],p[5],p[6]))
    print("{0:^8} | {1:^8} |{2:^8}".format(p[7],p[8],p[9]))

#lets draw the board using f strings instead of using format 
def DrawBoard2():
    clear_output(False)
    print(f"{p[1]:^8} | {p[2]:^8} |{p[3]:^8}")      #,(p[1],p[2],p[3]))
    print(f"{p[4]:^8} | {p[5]:^8} |{p[6]:^8}")      #,(p[4],p[5],p[6]))
    print(f"{p[7]:^8} | {p[8]:^8} |{p[9]:^8}")      #,(p[7],p[8],p[9]))

    
def Init():
    p[0] = "$"
    for i in range(10):
        p[i] = ""

def startGame():
    Init()
    print("game starts")
    DrawBoard2()
    movecount = 0
    player1 = "X"
    player2 = "O"
    currentMove = player1
    while movecount < 9: 
        num = int(input())
        p[num]=currentMove
        DrawBoard2()
        if IsWinner():
           break
        if(currentMove == player1):
            currentMove = player2
        else:
            currentMove = player1
        movecount+=1
    if IsWinner():
        print("{} Wins".format(currentMove))
    else:
        print("Draw")
       

def IsWinner():
    # we can use sets but maybe this will be faster 
    # to decide the winner we must have the X or O in sequence horizontal, vertical or diagonal
    # the following are the winning combinations
    if (p[1] == p[2] == p[3] !=""):
        return True
    elif(p[4] == p[5] == p[6] !=""):
        return True
    elif(p[7] == p[8] == p[9] !=""):
        return True
    if (p[1] == p[4] == p[7] !=""):
        return True
    elif(p[2] == p[5] == p[8] !=""):
        return True
    elif(p[3] == p[6] == p[9] !=""):
        return True
    elif(p[1] == p[5] == p[9] !=""):
        return True
    elif(p[3] == p[5] == p[7] !=""):
        return True
    else:
        return False



startGame()


