from defence import *
import math
class st5:
    def __init__(self):
        self.mandatory = None
        self.defence = defence1()
    def get_rank(self,game,pirates):
        rank = 20
        if(len(game.islands())==1 and self.check_if_close_together(game)):
            rank=95
        return rank,pirates
        
    def Move(self,game,remaining_pirates):
        leader = remaining_pirates[0]
        if(self.should_i_attack(game)):
            direction = self.get_dir(game,leader)
            self.move_pirates(game,direction)
        elif(self.check_if_capturing(game) and game.islands()[0].owner!=game.ME): ##situation = capturing island
            pass
        elif(self.check_if_reform(game)): ##situation = reform team!
            game.debug("reforming...")
            if(len(game.my_pirates())==len(game.all_my_pirates())):
                leader_loc = leader.location
            else:
                leader_loc = self.get_reforming_position(game,leader)
            self.reform(game,leader_loc)
##            for pirate in remaining_pirates:
##                directions = game.get_directions(pirate,leader_loc)
##                if(self.check_if_collision(game,pirate,directions[0])):
##                    game.debug("pirate "+str(pirate.id)+" will collise if he'll go "+directions[0])
##                    if(len(directions)>1 and self.check_if_collision(game,pirate,directions[1])):
##                        game.debug("pirate "+str(pirate.id)+" will collise if he'll go "+directions[1])
##                        direction='-'
##                    else:
##                        if(len(directions)>1):
##                            direction = directions[1]
##                        else:
##                            direction='-'
##                else:
##                    direction = directions[0]
##                game.set_sail(pirate,direction)

        elif(game.islands()[0].owner==game.ME): ##situation = the island is owned by me, now i shall protect it!
            protection_spot = list(game.islands()[0].location)
            protection_spot[0]+=3
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
            pass

    def get_reforming_position(self,game,leader):
        leader_loc = list(leader.initial_loc)
        new_x = (leader_loc[1] + game.islands()[0].location[1])/2
        leader_loc[1] = new_x
        return leader_loc

    def reform(self,game,leader):
        locations = self.get_locations(game)
        pirates = game.my_pirates()
        while(len(pirates)>0):
            index = 0
            flag=True
            while(flag):
                game.debug("index is "+str(index))
                game.debug("pirates are "+str(pirates))
                directions = game.get_directions(pirates[index],leader)
                if(len(directions)>1):
                    option = game.my_pirates().index(pirates[index])%2
                else:
                    option = 0
                direction = directions[option]
                if(self.check_if_collision_2(game,pirates[index],direction,locations)):
                    disturbing_pirate = self.check_who_collises(game,pirates[index],direction)
                    if(disturbing_pirate in pirates):
                        index = pirates.index(disturbing_pirate)
                    else:
                        pirates.remove(pirates[index])
                        flag=False
                else:
                    game.set_sail(pirates[index],direction)
                    temp = temp = self.defence.ForwardMoving(pirates[index],direction)
                    pirate_index = game.my_pirates().index(pirates[index])
                    locations[pirate_index] = temp
                    pirates.remove(pirates[index])
                    flag=False

    def move_pirates(self,game,direction):
        locations = self.get_locations(game)
        pirates = game.my_pirates()
        while(len(pirates)>0):
            index = 0
            flag=True
            while(flag):
                game.debug("index is "+str(index))
                game.debug("pirates are "+str(pirates))
                if(self.check_if_collision_2(game,pirates[index],direction,locations)):
                    disturbing_pirate = self.check_who_collises(game,pirates[index],direction)
                    if(disturbing_pirate in pirates):
                        index = pirates.index(disturbing_pirate)
                    else:
                        pirates.remove(pirates[index])
                        flag=False
                else:
                    game.set_sail(pirates[index],direction)
                    temp = temp = self.defence.ForwardMoving(pirates[index],direction)
                    pirate_index = game.my_pirates().index(pirates[index])
                    locations[pirate_index] = temp
                    pirates.remove(pirates[index])
                    flag=False
                    
    def get_locations(self,game):
        locations = []
        for pirate in game.my_pirates():
            locations.append(pirate.location)
        return locations

    def check_if_collision_2(self,game,pirate,direction,locations): ##like the first function but it works on list of locations
        temp = self.defence.ForwardMoving(pirate,direction)
        for location in locations:
            if(temp==location):
                return True
##        lost_pirates = game.my_lost_pirates()
##        initial_locs = []
##        for pirate in lost_pirates:
##            if(temp==pirate.initial_loc):
##                return True
        return False
        

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
        if(game.islands()[0].owner==game.ME or game.islands()[0].team_capturing==game.ME):
            return False
        if(game.islands()[0].team_capturing==game.ENEMY and len(game.enemy_pirates())-1<len(game.my_pirates())):
            return True
        if(game.get_turn()>400 and game.get_my_score()==0 and game.get_enemy_score()==0):
            return True
        if(len(game.enemy_pirates())<len(game.my_pirates())):
            return True
        if(game.islands()[0].owner==game.ENEMY and not len(game.enemy_pirates())>len(game.my_pirates()) and not self.check_if_reform(game)):
            return True
        return False

    def check_if_close_together(self,game):
        x_values = []
        y_values = []
        pirates = game.my_pirates()
        for pirate in pirates:
            y_values.append(pirate.initial_loc[0])
            x_values.append(pirate.initial_loc[1])
        x_values = list(set(x_values))
        y_values = list(set(y_values))
        if(math.fabs(x_values[0]-x_values[-1])<7 and math.fabs(y_values[0]-y_values[-1])<7):
            return True
        return False
