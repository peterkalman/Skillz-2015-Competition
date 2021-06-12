from defence1 import *

class st2:
    def __init__(self):
        self.x = 5

    def get_rank(self,game,pirates):
        
        rank=100
        ##If there is only one island reduce rank by 20 .
        if len(game.islands())==1:
            rank-=20
        return rank,pirates

    def Move(self,game, pirates):
        self.defence=defence1(game)
        islands = game.not_my_islands()
        remaining_pirates = pirates
        for i in xrange(len(pirates)):
            if(len(islands)>0):
                best_move = self.Return_Shortest_Dist(game,remaining_pirates,islands)
                pirate = best_move[0]
                island = best_move[1]
                direction = game.get_directions(pirate,island)
                possible_dir = self.defence.CheckIfInDanger(game,pirate)
                if(pirate == game.get_my_cloaked()):
                    not_crash_dir = self.defence.CheckIfCrash(game,pirate)
                    if(direction[0] in possible_dir):
                        game.reveal(pirate)
                        if(direction[0] in not_crash_dir):
                            game.set_sail(pirate, direction[0])
                    elif(len(direction)>1 and direction[1] in possible_dir):
                        game.reveal(pirate)
                        if(direction[1] in not_crash_dir):
                            game.set_sail(pirate, direction[1])
                    elif(direction[0] in not_crash_dir):
                        game.set_sail(pirate,direction[0])
                    elif(len(direction)>1 and direction[1] in not_crash_dir):
                        game.set_sail(pirate, direction[1])
                    elif(len(not_crash_dir)>0):
                        game.set_sail(pirate,not_crash_dir[0])
                else:
                    
                    if(direction[0] in possible_dir):
                        game.set_sail(pirate, direction[0])
                    elif(len(direction)>1 and direction[1] in possible_dir):
                        game.set_sail(pirate, direction[1])
                    elif(game.can_cloak()):
                        game.cloak(pirate)
                        game.set_sail(pirate,direction[0])
                    elif(len(possible_dir)>0):
                        game.set_sail(pirate,possible_dir[0])
                ##else:
                    ##pirate.cloak()
                    ##After dealing with returning the cloak pirate.
                remaining_pirates.remove(pirate)
                islands.remove(island)
            else:
                self.Sail_Default(game,remaining_pirates[0])
                remaining_pirates.remove(remaining_pirates[0])
                
            

    def Return_Shortest_Dist(self,game,pirates,islands):
        dist = []
        for pirate in pirates:
            for island in islands:
                dist.append(game.distance(pirate,island))
        minIndex = dist.index(min(dist))
        pirate = pirates[minIndex/len(islands)]
        island = islands[minIndex%len(islands)]
        return [pirate,island]

    def Sail_Default(self,game,pirate):
        dist = []
        islands = self.Get_Islands(game)
        if(len(islands)==0):
            islands = game.islands()
        for island in islands:
            dist.append(game.distance(pirate,island))
        index = dist.index(min(dist))
    ##if not(dist==0):
        direction = game.get_directions(pirate,islands[index])
        possible_dir = self.defence.CheckIfInDanger(game,pirate)
        if(direction[0] in possible_dir):
            game.set_sail(pirate, direction[0])
        elif(len(direction)>1 and direction[1] in possible_dir):
            game.set_sail(pirate, direction[1])
        elif(len(possible_dir)>0):
            game.set_sail(pirate,possible_dir[0])

    def Get_Islands(self,game):
        islands = game.not_my_islands()
        for island in game.my_islands():
            if island.team_capturing==game.ENEMY:
                islands.append(island)
        return islands

        
##    def ForwardMoving(self,pirate,movement_to_do):
##    ## Adds the movement to the locations of the pirates and return tuple.                      
##        temprow=pirate.location[0]
##        tempcol=pirate.location[1]
##        if movement_to_do[0]=="n":
##            temprow-=1
##        else:
##            if movement_to_do[0]=="e":
##                tempcol+=1
##            else:
##                if movement_to_do[0]=="s":
##                    temprow+=1
##                else:
##                    if movement_to_do[0]=="w":
##                        tempcol-=1
##                    ##else:
##                        ##if movement_to_do[0]=="-":
##                            ##do nothing ?
##        temp=(temprow,tempcol)
##        return temp
##    def Check_Threat(self,game, pirate, enemy):
##        directionList=['n','e','s','w','-']
##        for d in directionList:
##            temp = self.ForwardMoving(enemy,d)
##            if(game.in_range(temp,pirate)):
##                return True
##        return False
##
##    def Check_If_On_Island(self, game, pirate):
##        islands = game.islands()
##        for island in islands:
##            if(pirate.location==island.location):
##                return True
##        return False
##
##
##    def CheckIfInDanger(self,game,PirateToDefend):
##        directionList=['n','e','s','w','-']
##        DirectionListNotToGo=[]
##        ##We run a 'for' for enemy pirates that are alive
##        for direction in directionList:
##            dangers=int(0)
##            helpers=int(-1)
##            temp=self.ForwardMoving(PirateToDefend,direction)
##            ## We run a 'for' for all possible directions
##            for Enemy_Pirate in game.enemy_pirates():
##                if self.Check_Threat(game,temp,Enemy_Pirate) and not(self.Check_If_On_Island(game,Enemy_Pirate)):
##                    dangers+=1
##            for ally in game.my_pirates():
##                if(game.in_range(temp,ally) and not(self.Check_If_On_Island(game,ally))):
##                   helpers+=1
##            if(dangers>helpers and not(dangers==0)):
##                   DirectionListNotToGo.append(direction)
##        ##DirectionListNotToGo=list(set(DirectionListNotToGo))
##        game.debug("Pirate " + str(PirateToDefend))
##        game.debug("DirectionListNotToGo : "+str(DirectionListNotToGo))
##        for i in DirectionListNotToGo:
##            directionList.remove(i)
##        return directionList




        

        
    
        
        
