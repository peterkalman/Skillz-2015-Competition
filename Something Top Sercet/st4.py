from perfect_defence import *
defence = perfect_defence()
class st4:
    def __init__(self):
        self.mandatory = None
        
    def get_rank(self,game,pirates):
        rank = 70
        if(len(game.enemy_islands())>len(game.my_islands())):
            rank = 90
        return rank,pirates
        
    def Move(self,game,remaining_pirates):
        sailing_pirates = []
        dir_list = []
        islands = game.enemy_islands()
        for i in xrange(len(remaining_pirates)):
            if(len(islands)>0):
                best_move = self.Return_Shortest_Dist(game,remaining_pirates,islands)
                pirate = best_move[0]
                island = best_move[1]
                flag = pirate==game.get_my_cloaked()
                directions = game.get_directions(pirate,island)
                dir_list.append([directions,flag])
                islands.remove(island) 
            else:
                best_move = self.Return_Shortest_Dist(game,remaining_pirates,game.not_my_islands())
                pirate = best_move[0]
                island = best_move[1]
                flag = pirate==game.get_my_cloaked()
                directions = game.get_directions(pirate,island)
                dir_list.append([directions,flag])
            sailing_pirates.append(pirate)
            remaining_pirates.remove(pirate)
        dir_list = defence.get_directions(game,sailing_pirates,dir_list)
        
        for i in xrange(len(sailing_pirates)):
            game.set_sail(sailing_pirates[i],dir_list[i][0])
            if(sailing_pirates[i]!=game.get_my_cloaked() and dir_list[i][1]):
                game.debug("cloaking " + str(sailing_pirates[i]))
                game.cloak(sailing_pirates[i])
            elif(sailing_pirates[i]==game.get_my_cloaked() and dir_list[i][1]==False):
                game.debug("revealing " + str(sailing_pirates[i]))
                game.reveal(sailing_pirates[i])
            

    def Return_Shortest_Dist(self,game,pirates,islands):
        if(len(islands)==0):
            if(len(game.my_islands)==0):
                return [pirates[0],game.islands()[0]]
            return [pirates[0],game.my_islands()[0]]
        dist = []
        for pirate in pirates:
            for island in islands:
                dist.append(game.distance(pirate,island))
        minIndex = dist.index(min(dist))
        pirate = pirates[minIndex/len(islands)]
        if(self.check_if_on_island(game,pirate)):
            return [pirate,pirate]
        island = islands[minIndex%len(islands)]
        return [pirate,island]

    def check_if_on_island(self,game,pirate):
        for island in game.islands():
            if(island==pirate):
                return True
        return False
    
    def copy(self,remaining_pirates):
        sailing_pirates = []
        for pirate in remaining_pirates:
            sailing_pirates.append(pirate)
        return sailing_pirates
