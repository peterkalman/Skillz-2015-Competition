from defence import *
class st5:
    def __init__(self):
        self.mandatory = None
        self.defence = defence1()
    def get_rank(self,game,pirates):
        rank = 20
        if(len(game.islands())==1):
            rank=95
        return rank,pirates
        
    def Move(self,game,remaining_pirates):
        leader = remaining_pirates[0]
        if(self.check_if_reform(game)): ##situation = reform team!
            game.debug("reforming...")
            for pirate in remaining_pirates:
                directions = game.get_directions(pirate,leader)
                if(self.check_if_collision(game,pirate,directions[0])):
                    game.debug("pirate "+str(pirate.id)+" will collise if he'll go "+directions[0])
                    if(len(directions)>1 and self.check_if_collision(game,pirate,directions[1])):
                        game.debug("pirate "+str(pirate.id)+" will collise if he'll go "+directions[1])
                        direction='-'
                    else:
                        if(len(directions)>1):
                            direction = directions[1]
                        else:
                            direction='-'
                else:
                    direction = directions[0]
                game.set_sail(pirate,direction)
        elif(self.check_if_capturing(game) and game.islands()[0].owner!=game.ME): ##situation = capturing island
            pass
        elif(game.islands()[0].owner==game.ME): ##situation = the island is owned by me, now i shall protect it!
            protection_spot = list(game.islands()[0].location)
            protection_spot[1]+=3
            if not(self.check_if_someone_here(game,tuple(protection_spot))):
                directions = game.get_directions(leader,protection_spot)
                for pirate in remaining_pirates:
                    if(self.check_if_collision(game,pirate,directions[0])):
                        game.debug("pirate "+str(pirate.id)+" will collise if he'll go "+directions[0])
                        self.clear_way(game,self.check_who_collises(game,pirate,directions[0]))
                        direction = directions[0]
                    else:
                        direction = directions[0]
                    game.set_sail(pirate,direction)
        else:
            if(self.should_i_attack(game)):
                direction = self.get_dir(game,leader)
                for pirate in remaining_pirates:
                    game.set_sail(pirate,direction)

    def check_if_reform(self,game):
        pirates = game.my_pirates()
        max_pirates = game.all_my_pirates()
        if(len(pirates)<len(max_pirates)):
            return True
        for pirate in pirates:
            for ally in pirates:
                if(pirate!=ally):
                    if not(game.in_range(pirate,ally)):
                        return True
        return False

    def get_dir(self,game,leader):
        island = game.islands()[0]
        direction = game.get_directions(leader,island)[0]
        return direction

    def check_if_collision(self,game,pirate,direction):
        temp = self.defence.ForwardMoving(pirate,direction)
        pirates = game.my_pirates()
        for ally in pirates:
            if(ally!=pirate):
                if(temp==ally.location):
                    return True
        return False

    def check_if_capturing(self,game):
        island = game.islands()[0]
        for pirate in game.my_pirates():
            if(pirate.location==island.location):
                return True
        return False

    def check_who_collises(self,game,pirate,direction):
        temp = self.defence.ForwardMoving(pirate,direction)
        pirates = game.my_pirates()
        for ally in pirates:
            if(ally!=pirate):
                if(temp==ally.location):
                    return ally
        return None
        
    def clear_way(self,game,pirate):
        direction_list = ['n','e','s','w','-']
        for d in direction_list:
            if not(self.check_if_collision(game,pirate,d)):
                game.set_sail(pirate,d)
                return

    def check_if_someone_here(self,game,location):
        for pirate in game.my_pirates():
            if(pirate.location==location):
                return True
        return False

    def should_i_attack(self,game):
        if(game.islands()[0].team_capturing==game.ENEMY):
            return True
        if(game.get_turn()>400):
            return True
        if(len(game.enemy_pirates())<len(game.my_pirates())):
            return True
        if(game.islands()[0].owner==game.ENEMY):
            return True
        return False
    def find_protection_spot(self,game,from_what_side):
        ## From what side is a string that carries a meaning which side we have to defend
        ## There are 8 sides
        if not only_one_safezone():
            ## There are more than 1 safezones or maybe none
            ## we need to reform on the near the island
        else:
            closest_point=self.find_closest_location(game) ##V
            tempRow=closest_point[0]
            tempCol=closest_point[1]
            if from_what_side=="n":
                tempRow+=2
            if from_what_side=="ne":
                tempRow+=2
                tempCol-=2
            if from_what_side=="e":
                tempCol-=2
            if from_what_side=="se":
                tempCol-=2
                tempRow-=2
            if from_what_side=="s":
                tempRow-=2
            if from_what_side=="sw":
                tempCol+=2
                tempRow-=2
            if from_what_side=="w":
                tempCol+=2
            if from_what_side=="nw":
                tempCol+=2
                tempRow+=2
        return (tempRow,tempCol)
    def only_one_safezone(self,game):
        marked=[]
        for row in game.get_rows():
            for col in game.get_cols():
                temp=(row,col)
                if not game.is_passable(temp):
                    marked.append(temp)
        ## Now we have in marked , all the safezone blocks . we need to calculate the distances
        if not self.enemies_spawn_in_safezone(game,marked):## V ## If there are no safezones it takes care of it
            return False
        if self.Check_Spawn(game): ## X
    def find_closest_location(self,game):
        marked=[]
        closestDistance=game.get_cols() * game.get_rows()
        island=game.islands()[0]
        for row in game.get_rows():
            for col in game.get_cols():
                temp=(row,col)
                if not game.is_passable(temp):
                    marked.append(temp)
        for mark in marked:
            if game.distance(mark,island)<=closestDistance:
                closestDistance=game.distance(mark,island)
                closestLocation=mark
        return closestLocation
                            
                
                



    def enemies_spawn_in_safezone(self,game,marked):
        counter=0
        for pirates in game.all_enemy_pirates():
            for mark in marked:
                if mark==pirates:## we assume there cannot be more than one pirate spawning on the same block
                    counter+=1
        return counter == len(game.all_enemy_pirates())
        
    def Check_Spawn(self,game):## I wanted to recieve marked
    #############################mathematical solution
##        sumrow=0
##        sumcol=0
##        if len(marked)%2==0:
##            center_row=marked[int(len(marked)/2)][0]
##            center_row=center_row+marked[int(len(marked)/2)+1][0]
##            center_row=float(center_row/2)
##            center_col=marked[int(len(marked)/2)][1]
##            center_col=center_col+marked[int(len(marked)/2)+1][1]
##            center_col=float(center_col/2)
##        else:
##            center_row=marked[int(len(marked)/2)][0]
##            center_col=marked[int(len(marked)/2)][1]
##        for mark in marked:
##            sumrow+=mark[0]
##            sumcol+=mark[1]
##        sumrow=float(sumrow/center_row)
##        sumcol=float(sumcol/center_row)
##        if sumrow!=
        #####################################
##        while len(marked)>1:
##            flag=False## we didnt prove that it is seperated spawn
##            mark=marked[int(len(marked)/2)]## we take from the middle
##            marked.remove(mark)## We remove it
##            for mar in marked:
##                if game.distance(mark,mar)==1:
##                    flag=True
##            
        #####################################Binary Search
##        ##islandmap1,islandmap2=self.create2maps(game)
##        islandmap=islandmap1+islandmap2
##        
##        first1=0
##        last1=int(len(islandmap)/2)-1
##        
##        first2=int(len(islandmap)/2)
##        last2=len(islandmap)-1
##        
##        found1=False
##        found2=False
##        
##        stop=False
##        dir=['s','w','n','e']
##        while not stop:
##            while first1<=last1 and not found1:
##                midpoint1= (first1+last1)//2
##                temp1=islandmap[midpoint]
##                if not game.is_passable(temp1):
##                    found1=True
##                else:
##                    if self.Is_There_Safe_Zone(game,midpoint1,last1,islandmap):##if there are no safezones we dont have to search between the current midpoint1 and last1
##                        ## There is a possibility that if it returns true , there maybe still  the other half might have a safezone
##                        if self.Is_There_Safe_Zone(game,first1,midpoint1-1,islandmap):
##                            ## Do something for 2 spots
##                        else:
##                            first1=midpoint+1
##                    else:
##                        last=midpoint=-1
##                
##        
##        def create2maps(self,game):
##            islandmap1=[]
##            islandmap2=[]
##            rows=game.get_rows()
##            cols=game.get_cols()
##            for row in xrange(int(rows/2)):
##                for col in xrange(cols):
##                    temp=(row,col)
##                    islandmap1.append(temp)
##            for int(row+rows/2) in xrange(rows):
##                for col in xrange(cols):
##                    temp=(row,col)
##                    islandmap1.append(temp)
##        
##        def Is_There_Safe_Zone(self,game,midpoint,last,islandmap):
##            for i in xrange(last-midpoint):
##                if not game.is_passable(islandmap[i+midpoint]):
##                    return True
##            return False
        ########################################### Normal Scan
##        islandmap=[]
##        for row in game.get_rows():
##            for col in game.get_cols():
##                temp=(row,col)
##                islandmap.append(temp)
##        foundFirst=False
##        ShouldQuit=False
##        rowMoving=game.get_cols()
##        colMoving=1
##        dir=['s','w','n','e']
##        index=0
##        while not foundFirst:## there must be one
##            if not game.is_passable(islandmap[index]):
##                foundFirst=True
##            else:
##                index+=1
##        foundLast=False
##        while index<(game.get_rows()*game.get_cols()-1):
##            if game.is_passable(islandmap[index+1]):
##                foundLast=True
##                lastIndex=index
##                index+=1
##            else:
##                index=index+1
##            if foundLast:
##                NextFound=0
##                if game.is_passable(islandmap[index+1]):
##                    nextFound+=1
##                    index+=1                    
##                else:
##                    foundLast=False
##                if not foundLast:
##                    if nextFound<=row:
##                        return False
##                            

                
                
            
        
        
