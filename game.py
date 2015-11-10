import level1
import os
import sys
import random
import level2
import time

class game:
          fireball=[]
	  
	  level=1
          
          coins=[] #list of coins in a 2d array     
          for row in range(0,30,1) :
                  coins.append([])
          for row in range(0,30,1) :
                  for column in range(0,80,1) :
                         coins[row].append(" ")
                         
          game_board=[]  # a 2d array to represent the board of 30 * 80 initialized by blank 
          for row in range(0,30,1) :
                  game_board.append([])
          for row in range(0,30,1) :
                  for column in range(0,80,1) :
                         game_board[row].append(" ")


                  
            
          def printboard(self,player):       # print current staus of game_board
                os.system('clear')
                for row in range(29,-1,-1) :
                    for column in range(79,-1,-1) :
                        sys.stdout.write(str(self.game_board[row][column]))
                    print
                sys.stdout.write("Player Score: ")
                sys.stdout.write(str(player.score))
                print
                sys.stdout.write("Lives Left: ")
                sys.stdout.write(str(player.lives))
                print
                

          def setborder(self): # set the border os board
                for row in range(29,-1,-1) :
                  for column in range(79,-1,-1) :                
                      if row==0 or column==0 or row==29 or column==79:  # if the point is on the border print x
                           self.game_board[row][column]=("x")

                           
          def setfloor(self):
	      if self.level==1:
		      for row in range(29,-1,-1) :
		          counter=0
		          for column in range(79,-1,-1) :                
		             if row in level1.floor.height:   # if row is the floor
		                   if level1.floor.height.index(row)%2==0:
		                           counter=counter+1
		                           if counter < level1.length.length_floor :
		                                   self.game_board[row][column]=("x")
		                           else :
		                                   self.game_board[row][column]=(" ")
		                   else :
		                           counter=counter+1
		                           if counter > 79-level1.length.length_floor :
		                                   self.game_board[row][column]="x"
		                           else :
		                                   self.game_board[row][column]=(" ")

	      elif self.level==2: 
			for row in range(29,-1,-1) :
		          counter=0
		          for column in range(79,-1,-1) :                
		             if row in level2.floor.height:   # if row is the floor
		                   if level2.floor.height.index(row)%2==0:
		                           counter=counter+1
		                           if counter < level2.length.length_floor :
		                                   self.game_board[row][column]=("x")
		                           else :
		                                   self.game_board[row][column]=(" ")
		                   else :
		                           counter=counter+1
		                           if counter > 79-level2.length.length_floor :
		                                   self.game_board[row][column]="x"
		                           else :
		                                   self.game_board[row][column]=(" ")

          
                                           
          def  checkcoins(self,xcordinate,ycordinate):
              if self.coins[xcordinate][ycordinate]=="C":
                  return True
              else:
                  return False

                           
          def generatecoins(self):
             count=0
             while count<20:
                 xcordinate=random.randint(0,29)
                 ycordinate=random.randint(0,79)
                 if self.game_board[xcordinate][ycordinate]==" " and self.game_board[xcordinate-1][ycordinate]=="x":
                     count+=1
                     self.coins[xcordinate][ycordinate]="C"

                 
          def setcoins(self):
               for row in range(29,-1,-1) :
                  for column in range(79,-1,-1) :                
                      if self.coins[row][column]=="C" : # if the point is on the border print x
                           self.game_board[row][column]=("C")
                  

          def resetperson(self,person):
              self.game_board[person.xcordinate][person.ycordinate]=" "

    

          def setperson(self,person):
                if person.__class__.__name__=="player":
                    self.game_board[person.xcordinate][person.ycordinate]="P"
                elif person.__class__.__name__=="donkey":
                    self.game_board[person.xcordinate][person.ycordinate]="D"
                elif person.__class__.__name__=="princess":
                    self.game_board[person.xcordinate][person.ycordinate]="Q"

                              
          def setladders(self):
		  if self.level==1:
	                  for [row,column] in level1.stairs.cordinates :
        	                  self.game_board[row][column]="H"
  		  elif self.level==2:
			  for [row,column] in level2.stairs.cordinates :
        	                  self.game_board[row][column]="H"


          def setcage(self,princess):
              self.game_board[princess.xcordinate][princess.ycordinate+3]="x"
              self.game_board[princess.xcordinate][princess.ycordinate-7]="x"
              for i in range(princess.ycordinate-7,princess.ycordinate+4):
                  if self.game_board[princess.xcordinate-1][i]==" ":
                      self.game_board[princess.xcordinate-1][i]="x"

                      
       
                              
          def setboard(self,player1,donkey,princess):  #initially setting the board (the floor and the player.)
                self.setperson(player1)
                self.setperson(donkey)
                self.setperson(princess)
                self.setfloor()
                self.setladders()
                self.setborder()
                self.generatecoins()
                self.setcage(princess)
                self.setcoins()
                
    
          def checkwall(self,xcordinate,ycordinate):
              if self.game_board[xcordinate][ycordinate]=="x":
                  return True
              else :
                  return False

          def checkstairs(self,xcordinate,ycordinate):
	      if self.level==1:
		      if [xcordinate,ycordinate] in level1.stairs.cordinates:
		          return True
		      else:
		          return False
	      elif self.level==2:
		      if [xcordinate,ycordinate] in level2.stairs.cordinates:
		          return True
		      else:
		          return False


          def checkcrash(self,player,princess,donkey):
              if ([player.getxcordinate(),player.getycordinate()] in self.fireball) or (player.getxcordinate()==donkey.getxcordinate() and player.getxcordinate()==donkey.getycordinate()):
                  player.lives-=1
                  player.score-=25
                  player.xcordinate=1
                  player.ycordinate=77
                  print "You just lost a life !!!"
	      if player.lives==0:
		  print "Game Over...."
	          sys.exit()
	      if player.getxcordinate()==princess.getxcordinate() and player.getycordinate()==princess.getycordinate():
                  print "You Win....You will now enter level 2"
                  player.setxcordinate(1)
                  player.setycordinate(75)
                  time.sleep(2)
                  self.level+=1
                  player.score+=50
                  self.level=(self.level)%2
                  self.setborder()
                  self.setfloor()
                  self.setboard(player,donkey,princess)
                  self.setladders()

          def update(self,donkey,fireballs,player,princess):
                    donkey.movedonkey(self)
                    self.setladders()
                    self.setcoins()
                    fireballs.generate(donkey)
                    fireballs.reset()
                    fireballs.move(donkey)
                    fireballs.setf()
                    self.checkcrash(player,princess,donkey)

              
class fireball(game):
    
    
    def generate(self,donkey):
        if random.randint(1,30)==1:
            self.fireball.append([donkey.getxcordinate(),donkey.getycordinate()-3])


    def reset(self):
        for row in range(0,29):
            for column in range(0,79):
                if self.game_board[row][column]=="O":
                    self.game_board[row][column]=" "
        
            

    def setf(self):
        for [row,column] in self.fireball:
            self.game_board[row][column]="O"
        

    def move(self,donkey):
        for i in range(0,(len(self.fireball))):
            if self.fireball[i][0]==1:
                self.moveleftfire(self.fireball[i][0],self.fireball[i][1])
            elif self.fireball[i][0]==donkey.getxcordinate():
                if self.checkstairs(self.fireball[i][0]-1,self.fireball[i][1])==True and random.randint(1,2)==1:
                        self.movedownfire(self.fireball[i][0],self.fireball[i][1])
                else :
                        self.moverightfire(self.fireball[i][0],self.fireball[i][1])
            else:
                if self.checkstairs(self.fireball[i][0]-1,self.fireball[i][1]) and random.randint(1,2)==1:
                    self.movedownfire(self.fireball[i][0],self.fireball[i][1])
                if self.fireball[i][0]%2==0 :
                    self.moveleftfire(self.fireball[i][0],self.fireball[i][1])
                else :
                    self.moverightfire(self.fireball[i][0],self.fireball[i][1])
                

    def moveleft(self,xcordinate,ycordinate):
                for i in range(len(self.fireball)):
                    if self.fireball[i][0]==xcordinate and self.fireball[i][1]==ycordinate:
                        self.fireball[i][1]+=1;
                        return


    def moveright(self,xcordinate,ycordinate):
                for i in range(len(self.fireball)):
                    if self.fireball[i][0]==xcordinate and self.fireball[i][1]==ycordinate:       
                        self.fireball[i][1]-=1
                        return


    def movedown(self,xcordinate,ycordinate):
            for i in range(len(self.fireball)):
                    if self.fireball[i][0]==xcordinate and self.fireball[i][1]==ycordinate:
                        self.fireball[i][0]-=1
                        return


    def moveup(self,xcordinate,ycordinate):
                for i in range(len(self.fireball)):
                    if self.fireball[i][0]==xcordinate and self.fireball[i][1]==ycordinate:
                        self.fireball[i][1]+=1
                        return

    
    def moverightfire(self,xcordinate,ycordinate): 
            if self.checkwall(xcordinate-1,ycordinate-1)==False and self.checkstairs(xcordinate-1,ycordinate-1)==False:
                self.moveright(xcordinate,ycordinate)
                ycordinate-=1
                while self.checkwall(xcordinate-1,ycordinate)==False:
                    self.movedown(xcordinate,ycordinate)
                    xcordinate-=1
            elif self.checkwall(xcordinate,ycordinate-1):
                pass
            else :  
                self.moveright(xcordinate,ycordinate)
                ycordinate-=1


    def moveleftfire(self,xcordinate,ycordinate):
            if self.checkwall(xcordinate-1,ycordinate-1)==False and self.checkstairs(xcordinate-1,ycordinate-1)==False:
                self.moveleft(xcordinate,ycordinate)
                ycordinate+=1
                while self.checkwall(xcordinate-1,ycordinate)==False :
                    self.movedown(xcordinate,ycordinate)
                    xcordinate-=1
            elif  self.checkwall(xcordinate,ycordinate+1) :
                pass
            else:
                self.moveleft(xcordinate,ycordinate)
                ycordinate+=1
            
            


    def movedownfire(self,xcordinate,ycordinate):
                if self.checkstairs(xcordinate-1,ycordinate)==True:
                    self.movedown(xcordinate,ycordinate)
                
