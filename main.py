# STONE PAPER SCICOR
import getpass
Apoint = int(0)
Bpoint = int(0)
turns = int(7)
choices = ['stone','paper','scicor']
while turns > 0:
    i=1
    p1 = getpass.getpass("Player.1. Stone , paper , scicor : ").lower()
    p2 = getpass.getpass("Player.2. Stone , paper , scicor : ").lower()
    while p1 not in choices or p2 not in choices:
        p1 = getpass.getpass("Player.1. Stone , paper , scicor : ").lower()
        p2 = getpass.getpass("Player.2. Stone , paper , scicor : ").lower()
    else:
        if p1==p2:
                print("Its a tie !")
                print(f'Current score is {Apoint} - {Bpoint }')
        elif (p1=='stone' and p2=='scicor') or  ( p1=='paper' and p2 == 'stone') or ( p1=='scicor' and p2=='paper') :
                print(f" Player 1 is winner of turn {i} ")
                Apoint = Apoint + 1
                print(f'Current score is {Apoint} - {Bpoint }')
        else:
                print(f" Player 2 is winner of turn {i} ")
                Bpoint = Bpoint + 1  
                print(f'Current score is {Apoint} - {Bpoint }')
        if Apoint > Bpoint:
                print('Player 1 is winner')
        else:
                print('Player 2 is winner')   
        i=+1
        turns = turns-1
        
