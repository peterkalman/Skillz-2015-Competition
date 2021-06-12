from perfect_defence import *
defence = perfect_defence()
class st2:
    def __init__(self):
        self.mandatory = None
        
    def get_rank(self,game,pirates):
        rank = 80
        return rank,pirates
        
    def Move(self,game,remaining_pirates):
        sailing_pirates = []
        dir_list = []
        islands = game.not_my_islands()
        secondery_islands = self.get_capturing_islands(game)
        for i in xrange(len(remaining_pirates)):
            if(len(islands)>0):
                best_move = self.Return_Shortest_Dist(game,remaining_pirates,islands)
                pirate = best_move[0]
                island = best_move[1]
                flag = pirate==game.get_my_cloaked()
                directions = game.get_directions(pirate,island)
                game.debug(str(directions))
                directions = self.FixDirections(game,directions,pirate,island)
                dir_list.append([directions,flag])
                islands.remove(island) 
            else:
                best_move = self.Return_Shortest_Dist(game,remaining_pirates,game.not_my_islands())
                pirate = best_move[0]
                island = best_move[1]
                flag = pirate==game.get_my_cloaked()
                directions = game.get_directions(pirate,island)
                directions = self.FixDirections(game,directions,pirate,island)
                dir_list.append([directions,flag])
            sailing_pirates.append(pirate)
            remaining_pirates.remove(pirate)
        dir_list = defence.get_directions(game,sailing_pirates,dir_list)
        game.debug("###################################")
        game.debug(sailing_pirates)
        game.debug(dir_list)
        for i in xrange(len(sailing_pirates)):

            ##game.debug("pirate "+str(sailing_pirates[i])+"going "+dir_list[i][0])## crashes here
            game.set_sail(sailing_pirates[i],dir_list[i][0])
            if(sailing_pirates[i]!=game.get_my_cloaked() and dir_list[i][1]):
                ##game.debug("cloaking " + str(sailing_pirates[i]))
                game.cloak(sailing_pirates[i])
            elif(sailing_pirates[i]==game.get_my_cloaked() and dir_list[i][1]==False):
                ##game.debug("revealing " + str(sailing_pirates[i]))
                game.reveal(sailing_pirates[i])
            

    def Return_Shortest_Dist(self,game,pirates,islands):
        if(len(islands)==0):
            if(game.get_my_cloaked()!=None):
                cloaked=game.get_my_cloaked()
                return [pirates[0],cloaked]
            if(len(game.my_islands())==0):
             ##   return [pirates[0],game.islands()[0]]
                index = len(game.not_my_islands()%pirates[0].id)
                return [pirates[0],game.not_my_islands()[index]]
            return [pirates[0],game.my_islands()[0]]
        dist = []
        for pirate in pirates:
            for island in islands:
                dist.append(game.distance(pirate,island))
        minIndex = dist.index(min(dist))
        pirate = pirates[minIndex/len(islands)]
        island = islands[minIndex%len(islands)]
        return [pirate,island]


    def get_capturing_islands(self,game):
        islands=[]
        for island in game.islands():
            if island.team_capturing==game.ENEMY:
                islands.append(island)
        return islands

    def copy(self,remaining_pirates):
        sailing_pirates = []
        for pirate in remaining_pirates:
            sailing_pirates.append(pirate)
        return sailing_pirates
    def FixDirections(self,game,directions,pir,island):
        dirs=directions## we save the direction in case we need it
        for dire in directions:## The basic function that checks if we go to a safe zone
            temp=self.ForwardMoving(pir,dire)
            if not game.is_passable(temp):
                directions.remove(dire)
        if len(directions)==0:## If we did go into the safe zone and we cant go anywhere else , for example when we go in straight line  and there is 
            directions=['n','e','s','w','-']
            directions=self.Remove_List_from_another_list(directions,dirs)## We remove all the bad directions because they dont bring us anywhere
            for dire in directions:
                temp=self.ForwardMoving(pir,dire)
                if not game.is_passable(temp):
                    directions.remove(dire)
            ## We if there are any new directions that we cannot go to , we remove them as well
            ## Now we have an array with all the possible movements that dont kill us.
            ## We have to find now what is the most efficent
            directions=self.Recieve_The_Shortest_Dist(game,directions,pir,island)
        return directions
    def Recieve_The_Shortest_Dist(self,game,directions,pir,island):
        dist=[]
        for dire in directions:
            temp=self.ForwardMoving(pir,dire)
            tempDist=game.distance(temp,island)## maybe island.location
            dist.append([temp,tempDist])
        maxdist=dist[0][1]
        maxdire=dist[0][0]
        for dis in dist:
            if dis[1]>maxdist:
                maxdist=dis[1]
                maxdire=dis[0]
        return [maxdire]
    def Remove_List_from_another_list(self,directions,directionsToRemove):
        for dire in directionsToRemove:
            directions.remove(dire)
        return directions
            
            
            
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
##                    else:
##                        if movement_to_do[0]=="-":
##                            do nothing ?
        temp=(temprow,tempcol)
        return temp
