import level1 # imports height and floor of each floor
import game# imports main file containing board and the coordinates 
import sys
import random
import time

class person:
        xcordinate=1
        ycordinate=1

        def setxcordinate(self,x):
                self.xcordinate=x

        def setycordinate(self,y):
                self.ycordinate=y

        def getxcordinate(self):
                return self.xcordinate

        def getycordinate(self):
                return self.ycordinate
        
        def moveleft(self):
                self.setycordinate(self.getycordinate()+1)

        def moveright(self):
                self.setycordinate(self.getycordinate()-1)

        def movedown(self):
                self.setxcordinate(self.getxcordinate()-1)

        def moveup(self):
                self.setxcordinate(self.getxcordinate()+1)

class donkey(person):

        def __init__(self,xcordinate,ycordinate):
                self.xcordinate=xcordinate
                self.ycordinate=ycordinate
        
        def movedonkey(self,game):
                game.resetperson(self)
                if random.randint(1,2)==1:
                        self.moveleft()
                        if game.checkwall(self.getxcordinate(),self.getycordinate()):
                                self.moveright()
                else:
                        self.moveright()
                        if game.checkwall(self.getxcordinate()-1,self.getycordinate())==False:
                                self.moveleft()
                game.setcoins()
                game.setperson(self)
                                
        
class player(person):
        

        def __init__(self,xcordinate,ycordinate):
                self.xcordinate=xcordinate
                self.ycordinate=ycordinate
                self.lives=3
                self.score=0
                self.previous=1
        
	def checkair(self,game):
		game.resetperson(self)
                while game.game_board[self.getxcordinate()-1][self.getycordinate()]==" ":
                    self.setxcordinate(self.getxcordinate()-1)


        def moveright_player(self,game):
            game.resetperson(self)
            if game.checkwall(self.getxcordinate(),self.getycordinate()-1):
                pass
            else :
                self.moveright()
		game.setperson(self)
		self.checkair(game)
		game.resetperson(self)
            if game.checkcoins(self.getxcordinate(),self.getycordinate()):
                    game.coins[self.getxcordinate()][self.getycordinate()]=" "
                    self.score+=5
                    game.setcoins()

            

        def moveleft_player(self,game):
            game.resetperson(self)
            if  game.checkwall(self.getxcordinate(),self.getycordinate()+1) :
                pass
            else:	
                self.moveleft()
		game.setperson(self)
		game.printboard(self)
		self.checkair(game)
		game.resetperson(self)	
            if game.checkcoins(self.getxcordinate(),self.getycordinate()):
                    game.coins[self.getxcordinate()][self.getycordinate()]=" "
                    self.score+=5
                    game.setcoins()

            

        def moveup_player(self,game):
                if game.checkstairs(self.getxcordinate(),self.getycordinate()):
                        self.moveup()



        def movedown_player(self,game):
                if game.checkstairs(self.xcordinate-1,self.ycordinate)==True:
                        game.resetperson(self)
                        self.movedown()

        
        def jumpright_player(self,donkey,fireballs,game,princess):
                for i in range(1,3):
		        game.resetperson(self)
			if game.checkwall(self.getxcordinate()+1,self.getycordinate()-1):
				self.checkair(game)
				break	
		        self.setxcordinate(self.getxcordinate()+1)
		        self.setycordinate(self.getycordinate()-1)
		        game.update(donkey,fireballs,self,princess)
		        game.setperson(self)
		        game.printboard(self)
		        time.sleep(0.1)
                game.resetperson(self)
		if game.checkwall(self.getxcordinate()-1,self.getycordinate()-1):
			self.checkair(game)
			game.update(donkey,fireballs,self,princess)
			return 
                self.setxcordinate(self.getxcordinate()-1)
                self.setycordinate(self.getycordinate()-1)
                game.update(donkey,fireballs,self,princess)
                game.setperson(self)
                game.printboard(self)
                time.sleep(0.1)
                game.resetperson(self)
		if game.checkwall(self.getxcordinate()-1,self.getycordinate()-1):
			self.checkair(game)
			game.update(donkey,fireballs,self,princess)
			return
                self.setxcordinate(self.getxcordinate()-1)
                self.setycordinate(self.getycordinate()-1)
		self.checkair(game)
                game.update(donkey,fireballs,self,princess)
                game.setperson(self)
        

        def jumpleft_player(self,donkey,fireballs,game,princess): # 4step 
		for i in range(1,3):
		        game.resetperson(self)
			if game.checkwall(self.getxcordinate()+1,self.getycordinate()+1):
				self.checkair(game)
				break	
		        self.setxcordinate(self.getxcordinate()+1)
		        self.setycordinate(self.getycordinate()+1)
		        game.update(donkey,fireballs,self,princess)
		        game.setperson(self)
		        game.printboard(self)
		        time.sleep(0.1)
                game.resetperson(self)
		if game.checkwall(self.getxcordinate()-1,self.getycordinate()+1):
			self.checkair(game)
			game.update(donkey,fireballs,self,princess)
			return 
                self.setxcordinate(self.getxcordinate()-1)
                self.setycordinate(self.getycordinate()+1)
                game.update(donkey,fireballs,self,princess)
                game.setperson(self)
                game.printboard(self)
                time.sleep(0.1)
                game.resetperson(self)
		if game.checkwall(self.getxcordinate()-1,self.getycordinate()-1):
			self.checkair(game)
			game.update(donkey,fireballs,self,princess)
			return
                self.setxcordinate(self.getxcordinate()-1)
                self.setycordinate(self.getycordinate()+1)
		self.checkair(game)
                game.update(donkey,fireballs,self,princess)
                game.setperson(self)

                
class princess(person):

        def __init__(self,xcordinate,ycordinate):
                self.xcordinate=xcordinate
                self.ycordinate=ycordinate
