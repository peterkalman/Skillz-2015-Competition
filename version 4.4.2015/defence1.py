class defence1:
    def __init__(self,game):
        self.limit_rows=game.get_rows()
        self.limit_cols=game.get_cols()
        
        
    def ForwardMoving(self,pirate,movement_to_do):
    ## Adds the movement to the locations of the pirates and return tuple.                      
        temprow=pirate.location[0]
        tempcol=pirate.location[1]
        if movement_to_do[0]=="n":
            temprow-=1
        else:
            if movement_to_do[0]=="e":
                tempcol+=1
            else:
                if movement_to_do[0]=="s":
                    temprow+=1
                else:
                    if movement_to_do[0]=="w":
                        tempcol-=1
                    ##else:
                        ##if movement_to_do[0]=="-":
                            ##do nothing ?
        temp=(temprow,tempcol)
        return temp
    def Check_Threat(self,game, pirate, enemy):
        directionList=['n','e','s','w','-']
        for d in directionList:
            temp = self.ForwardMoving(enemy,d)
            if(game.in_range(temp,pirate)):
                return True
        return False

    def Check_If_Useless(self, game, pirate):
        if(pirate == game.get_my_cloaked()):
            game.debug("This pirate is cloaked yo!")
            return True
        islands = game.islands()
        for island in islands:
            if(pirate.location==island.location):
                return True
        return False


    def CheckIfInDanger(self,game,PirateToDefend):
        directionList=['n','e','s','w','-']
        DirectionListNotToGo=[]
        ##We run a 'for' for enemy pirates that are alive
        for direction in directionList:
            dangers=int(0)
            helpers=int(0)
            temp=self.ForwardMoving(PirateToDefend,direction)
            if temp[0]<self.limit_rows and temp[1]<self.limit_cols:
                    
                ## We run a 'for' for all possible directions
                for Enemy_Pirate in game.enemy_pirates():
                    if self.Check_Threat(game,temp,Enemy_Pirate) and not(self.Check_If_Useless(game,Enemy_Pirate)):
                        dangers+=1
                for ally in game.my_pirates():
                    if(ally!=PirateToDefend):
                        if(game.in_range(temp,ally) and not(self.Check_If_Useless(game,ally))):
                           helpers+=1
                if(dangers>helpers):
                       DirectionListNotToGo.append(direction)
            else:
                DirectionListNotToGo.append(direction)
        ##DirectionListNotToGo=list(set(DirectionListNotToGo))
        for i in DirectionListNotToGo:
            directionList.remove(i)
        return directionList

    def CheckIfCrash(self,game,PirateToDefend):
        directionList=['n','e','s','w','-']
        DirectionListNotToGo=[]
        for direction in directionList:
            temp=self.ForwardMoving(PirateToDefend,direction)
            crash = False
            if temp[0]<self.limit_rows and temp[1]<self.limit_cols:
                for Enemy_Pirate in game.enemy_pirates():
                    for d2 in directionList:
                        temp2 = self.ForwardMoving(Enemy_Pirate,d2)
                        if(temp2 == temp):
                            crash = True
                if(crash):
                       DirectionListNotToGo.append(direction)
            else:
                DirectionListNotToGo.append(direction)
        for i in DirectionListNotToGo:
            directionList.remove(i)
        return directionList

        

        
    
        
        
