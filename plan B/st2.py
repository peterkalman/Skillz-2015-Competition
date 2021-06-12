class st2:
    def __init__(self):
        self.x = 5

    def get_rank(self,game,pirates):
        return 100,pirates

    def Move(self,game, pirates):
        islands = game.not_my_islands()
        remaining_pirates = pirates
        for i in xrange(len(pirates)):
            if(len(islands)>0):
                best_move = self.Return_Shortest_Dist(game,remaining_pirates,islands)
                pirate = best_move[0]
                island = best_move[1]
                direction = game.get_directions(pirate,island)
                possible_dir = self.CheckIfInDanger(game,pirate)
                if(direction[0] in possible_dir):
                    game.set_sail(pirate, direction[0])
                elif(len(direction)>1 and direction[1] in possible_dir):
                    game.set_sail(pirate, direction[1])
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
        islands = game.islands()
        for island in islands:
            dist.append(game.distance(pirate,island))
        index = dist.index(min(dist))
        if not(dist==0):
            direction = game.get_directions(pirate,islands[index])
            possible_dir = self.CheckIfInDanger(game,pirate)
            if(direction[0] in possible_dir):
                game.set_sail(pirate, direction[0])
            elif(len(direction)>1 and direction[1] in possible_dir):
                game.set_sail(pirate, direction[1])

        
    def ForwardMoving(self,pirate,movement_to_do):
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

    def CheckIfInDanger(self,game,PirateToDefend):
        directionList=['n','e','s','w','-']
        DirectionListNotToGo=[]
        ##We run a 'for' for enemy pirates that are alive
        for direction in directionList:
            dangers=int(0)
            helpers=int(-1)
            temp=self.ForwardMoving(PirateToDefend,direction)
            ## We run a 'for' for all possible directions
            for Enemy_Pirate in game.enemy_pirates():
                if self.Check_Threat(game,PirateToDefend,Enemy_Pirate) and not(self.Check_If_On_Island(game,Enemy_Pirate)):
                    dangers+=1
            for ally in game.my_pirates():
                if(game.in_range(temp,ally) and not(self.Check_If_On_Island(game,ally))):
                   helpers+=1
            if(dangers>helpers and not(dangers==0)):
                   DirectionListNotToGo.append(direction)
        DirectionListNotToGo=list(set(DirectionListNotToGo))
        for i in DirectionListNotToGo:
            directionList.remove(i)
        return directionList

    def Check_Threat(self,game, pirate, enemy):
        directionList=['n','e','s','w','-']
        for d in directionList:
            temp = self.ForwardMoving(enemy,d)
            if(game.in_range(temp,pirate)):
                return True
        return False

    def Check_If_On_Island(self, game, pirate):
        islands = game.islands()
        for island in islands:
            if(pirate.location==island.location):
                return True
        return False





        

        
    
        
        
