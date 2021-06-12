##                                      IMPORT THIS
######################################################################################
##pirate= pirate Location
##movement_to_do=direction of pirate
def ForwardMoving(pirate,movement_to_do):
    ## Adds the movement to the locations of the pirates and return a list of tuples.                      
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

######################################################################################

class st3:
    def __init__(self):
        self.x=0
    def Move(self,game,pirates):
        for p in pirates:
            piratelocation=p.location
            game.debug(piratelocation)
            game.set_sail(p,self.DirectionToSail(game,piratelocation))
    def get_rank(self,game,pirates):
        return 60,pirates
    def DirectionToSail(self,game,p):
        DirectionPirateCanSail=self.CheckIfInDanger(game,p)
        ## READ PLEASE:

        
        ## I dont know exactly what direction we should move but I assume some later calculations have to be done

        
        return DirectionPirateCanSail[1]


    ##PirateToDefend - is the location of pirate we want to him to stay alive
    def CheckIfInDanger(self,game,PirateToDefend):
        directionList=['n','e','s','w','-']
        danger=False
        DirectionListNotToGo=[]
        ##We run a 'for' for enemy pirates that are alive
        for Enemy_Pirate in game.enemy_pirates():
            ## We run a 'for' for all possible directions
            for direction in directionList:
                ##we recieve from FORWARDMOVING a location with the movement done.
                temp=ForwardMoving(Enemy_Pirate,direction)
                ##PirateToDefend Is the pirate we check if he is in danger
                if game.in_range(PirateToDefend,Enemy_Pirate):
                    ##We save the directions we dont want to go there
                    DirectionListNotToGo.append(direction)
                    ##Danger is real
                    danger=True
        DirectionListNotToGo=list(set(DirectionListNotToGo))
        for i in DirectionListNotToGo:
            directionList.remove(i)
        ## If there is no danger we return a list with all of the directions availbable
        ## If there are dangerous directions we remove them from the availble directions
        return directionList
    

            
                    
                    
                
        
        

    
