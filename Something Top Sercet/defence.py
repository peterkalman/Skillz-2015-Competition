class defence1:
    def __init__(self):
        self.mandatory = None
        
        
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
        ##pirate might be a tuple of location and not a real pirate object
        if(pirate == game.get_my_cloaked()):
            ("This pirate is cloaked yo!")
            return True
        islands = game.islands()
        if(type(pirate)==tuple):
            for island in islands:
                if(pirate==island.location):
                    return True
            return False
        else:
            for island in islands:
                if(pirate.location==island.location):
                    return True
            return False
            


    def CheckIfInDanger(self,game,PirateToDefend,allies_loc):
        ##allies loc = a list of all allies locations
        ##game.debug("pirate "+str(PirateToDefend)+" allies_loc="+str(allies_loc))
        directionList=['n','e','s','w','-']
        DirectionListNotToGo=[]
        ##We run a 'for' for enemy pirates that are alive
        for direction in directionList:
            dangers=int(0)
            helpers=int(0)
            temp=self.ForwardMoving(PirateToDefend,direction)
            if game.is_passable(temp):
                for Enemy_Pirate in game.enemy_pirates():
                    if self.Check_Threat(game,temp,Enemy_Pirate) and not(self.Check_If_Useless(game,Enemy_Pirate)):
                        dangers+=1
                for ally in allies_loc:
                    if(game.in_range(temp,ally) and not(self.Check_If_Useless(game,ally))):
                       helpers+=1
                ##game.debug("temp = "+str(temp)+" ,dangers= "+str(dangers)+" helpers="+str(helpers))
                if(dangers>helpers):
                       DirectionListNotToGo.append(direction)
            else:
                DirectionListNotToGo.append(direction)
        ##DirectionListNotToGo=list(set(DirectionListNotToGo))
        for i in DirectionListNotToGo:
            directionList.remove(i)
        
        ##game.debug("directions list for pirate "+str(PirateToDefend)+ " is "+str(directionList))
        return directionList

    def CheckIfCrash(self,game,PirateToDefend):
        directionList=['n','e','s','w','-']
        DirectionListNotToGo=[]
        for direction in directionList:
            temp=self.ForwardMoving(PirateToDefend,direction)
            crash = False
            if game.is_passable(temp):
                if(self.check_crash(game,temp)):
                       DirectionListNotToGo.append(direction)
            else:
                DirectionListNotToGo.append(direction)
        for i in DirectionListNotToGo:
            directionList.remove(i)
        return directionList

    def check_crash(self,game, temp):
        directionList=['n','e','s','w','-']
        for Enemy_Pirate in game.enemy_pirates():
            for d2 in directionList:
                temp2 = self.ForwardMoving(Enemy_Pirate,d2)
                if(temp2 == temp):
                    return True
        return False
        

        

        
    
        
        
