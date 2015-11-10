import game
import level1
import level2
import person
import sys
import tty
import signal
import termios
import os
import time
import atexit
from select import select

class take_input():
    
    def __init__(self):
    
            # Save the terminal settings
            self.fd = sys.stdin.fileno()
            self.new_term = termios.tcgetattr(self.fd)
            self.old_term = termios.tcgetattr(self.fd)
    
            # New terminal setting unbuffered
            self.new_term[3] = (self.new_term[3] & ~termios.ICANON & ~termios.ECHO)
            termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.new_term)
    
            # Support normal-terminal reset at exit
            atexit.register(self.set_normal_term)
    
    
    def set_normal_term(self):
            termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.old_term)


    def getch(self):
            return sys.stdin.read(1)
                        
    def kbhit(self):
   
            dr,dw,de = select([sys.stdin], [], [], 0)
            return dr != []


 
if __name__=="__main__" :
    game1=game.game()
    kb=take_input()
    player1=person.player(1,77)
    donkey=person.donkey(25,75)
    fireballs=game.fireball()
    princess=person.princess(28,60)
    game1.setboard(player1,donkey,princess)
    game1.printboard(player1)
    while True:
        if kb.kbhit(): 
                x = kb.getch()
                game1.resetperson(player1)
                if ord(x)==100:
                    player1.moveright_player(game1)
                    player1.previous=1

                elif ord(x)==97:
                    player1.moveleft_player(game1)
                    player1.previous=2

                elif ord(x)==119:
                    player1.moveup_player(game1)

                elif ord(x)==115:
                    player1.movedown_player(game1)

                elif ord(x)==32:
                    if player1.previous==1:
                        player1.jumpright_player(donkey,fireballs,game1,princess)
                    else:
                        player1.jumpleft_player(donkey,fireballs,game1,princess)
                    
                elif ord(x)==113:
                    sys.exit()
                else :
                    pass
                game1.checkcrash(player1,princess,donkey)
                game1.update(donkey,fireballs,player1,princess)
                game1.setperson(player1)
                game1.printboard(player1)
        else :
                time.sleep(0.2)
                game1.checkcrash(player1,princess,donkey)
                game1.update(donkey,fireballs,player1,princess)
                game1.setperson(player1)
                game1.printboard(player1)
        
