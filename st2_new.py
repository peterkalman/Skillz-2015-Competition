from perfect_defence import *
defence = perfect_defence()
class st2:
    def __init__(self):
        self.mandatory = None
        
    def get_rank(self,game,pirates):
        rank = 80
        return rank,pirates
    def can_i_attack_kraken(self,game,pirate):
        kra=game.get_kraken()
        if kra==None:
            return False
        if(game.get_kraken().state=="asleep"):
            if game.distance(kra.location,pirate.location)>kra.turns_left_in_state():
                return True
        else: return False
        
    def Move(self,game,remaining_pirates):
        
        sailing_pirates = []
        dir_list = []
        islands = game.not_my_islands()
        kraken=False## are we caring about the kraken
        for i in xrange(len(remaining_pirates)):
            if(len(islands)>0):
                
##                if(game.get_kraken().state=="asleep") and not Kraken:
##                    if game.get_karken().turns_left_in_state>4 or game.in_range(remaining_pirates[i],game.get_kraken()):
##                        best_move=self.Return_Shortest_Dist(game,remaining_pirates,game.get_kraken())
                    ##add to dir list pirate which is closest to kraken
                if not kraken:
                    if self.can_i_attack_kraken(game,remaining_pirates[i]):
                        
                        ##pirate = best_move[0]
                        ##island = best_move[1]
                        flag = pirate==game.get_my_cloaked()
                        directions = game.get_directions(remaining_pirates[i],game.get_kraken())
                        dir_list.append([directions,flag])
                        kraken=True
                    else:
                        best_move = self.Return_Shortest_Dist(game,remaining_pirates,islands)
                        pirate = best_move[0]
                        island = best_move[1]
                        flag = pirate==game.get_my_cloaked()
                        directions = game.get_directions(pirate,island)
                        dir_list.append([directions,flag])
                        islands.remove(island)
                else:
                    best_move = self.Return_Shortest_Dist(game,remaining_pirates,islands)
                    pirate = best_move[0]
                    island = best_move[1]
                    flag = pirate==game.get_my_cloaked()
                    directions = game.get_directions(pirate,island)
                    dir_list.append([directions,flag])
                    islands.remove(island)
                
            else:
                enemies=game.enemy_pirates()
                ##if game.get_kraken()!=None and game.get_kraken().state=="awake":
                ##    enemies.append(game.get_kraken())
                if(len(game.enemy_pirates())==0):
                    best_move = self.Return_Shortest_Dist(game,remaining_pirates,game.not_my_islands())
                    pirate = best_move[0]
                    island = best_move[1]
                    flag = pirate==game.get_my_cloaked()
                    directions = game.get_directions(pirate,island)
                    dir_list.append([directions,flag])
                else:
                    best_move = self.hunt_enemies(game,remaining_pirates)
                    pirate = best_move[0]
                    game.debug("pirate "+str(pirate)+" reporting, going to hunt some enemies...")
                    baddy = best_move[1]
                    flag = pirate==game.get_my_cloaked()
                    directions = game.get_directions(pirate,baddy)
                    dir_list.append([directions,flag])
            sailing_pirates.append(pirate)
            remaining_pirates.remove(pirate)
        dir_list = defence.get_directions(game,sailing_pirates,dir_list)

        for i in xrange(len(sailing_pirates)):
            game.set_sail(sailing_pirates[i],dir_list[i][0])
            if(sailing_pirates[i]!=game.get_my_cloaked() and dir_list[i][1]):
                game.cloak(sailing_pirates[i])
            elif(sailing_pirates[i]==game.get_my_cloaked() and dir_list[i][1]==False):
                game.reveal(sailing_pirates[i])
            

    def Return_Shortest_Dist(self,game,pirates,islands):
        if(len(islands)==0):
            if(game.get_my_cloaked()!=None):
                cloaked=game.get_my_cloaked()
                return [pirates[0],cloaked]
            if(pirates[0].id==0):
                index = 0
            else:
                i = pirates[0].id
                while(i>=len(game.islands())):
                    i=i-len(game.islands())
                if(i==0):
                    index=0
                else:
                    index = len(game.islands())%i
            return [pirates[0],game.islands()[index]]
        dist = []
        for pirate in pirates:
            for island in islands:
                d = game.distance(pirate,island)
                d = d/island.value
                dist.append(d)
        minIndex = dist.index(min(dist))
        pirate = pirates[minIndex/len(islands)]
        island = islands[minIndex%len(islands)]
        return [pirate,island]

    def hunt_enemies(self,game,pirates):
        dist=[]
        enemies = game.enemy_pirates()
        for pirate in pirates:
            for baddy in enemies:
                d = game.distance(pirate,baddy)
                if(self.check_if_on_island(game,baddy)):
                    d=d/2
                dist.append(d)
        minIndex = dist.index(min(dist))
        pirate = pirates[minIndex/len(enemies)]
        baddy = enemies[minIndex%len(enemies)]
        return [pirate,baddy]

    def check_if_on_island(self,game,pirate):
        for island in game.islands():
            if island.location==pirate.location:
                return True
        return False

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

##    def get_treasure_islands(self,game,islands):
##        treasure_islands=[]
##        for island in islands:
##            if island.value>1:
##                treasure_islands.append(island)
##        for island in treasure_islands:
##            islands.remove(island)
##        return treasure_islands
##
##    def get_value_of_islands(self,game,islands):
##        values = []
##        for island in islands:
##            values.append(island.value)
##        return values
