from defence import *
defence = defence1()
class perfect_defence:
    def __init__(self):
        self.mandatory = None
        self.last_round_movement=['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-']
        self.reverse_dir = {'n':'s','s':'n','e':'w','w':'e','-':'-'}
        
    def get_directions(self,game,pirates,dir_list):
        locations = self.GetLocations(game,pirates)
        dir_to_pirate={}
        new_dir = []
        last_dir=dir_list
        can_cloak=game.can_cloak()
        while not(new_dir==last_dir):
            last_dir=new_dir
            for i in xrange(len(pirates)):
                index = pirates[i].id
                last_round_move = self.last_round_movement[index]
                allies_loc = self.get_allies_locations(i,locations)
                if(dir_list[i][1]):
                    flag = False
                    possible_dir = defence.CheckIfInDanger(game,pirates[i],allies_loc)
                    if(len(possible_dir)!=5):
                        flag = True
                    possible_dir = defence.CheckIfCrash(game,pirates[i])
                    temp = []
                    emergency = True
                    if(dir_list[i][0][0] in possible_dir):
                        temp.append(dir_list[i][0][0])
                        emergency = False
                    if(len(dir_list[i][0])>1 and dir_list[i][0][1] in possible_dir):
                        temp.append(dir_list[i][0][1])
                        emergency = False
                    if(emergency and len(possible_dir)>0):
                        if(self.reverse_dir[last_round_move] in possible_dir):
                            possible_dir.remove(self.reverse_dir[last_round_move])
                            possible_dir.append(self.reverse_dir[last_round_move])
                        temp.append(possible_dir[0])
                    elif(emergency):
                        ##game.debug("pirate " + str(pirates[i]) + " has no options left")
                        flag=True
                        temp.append('-')
                else:
                    possible_dir = defence.CheckIfInDanger(game,pirates[i],allies_loc)
                    temp = []
                    flag = False
                    emergency = True
                    if(dir_list[i][0][0] in possible_dir):
                        temp.append(dir_list[i][0][0])
                        emergency = False
                    if(len(dir_list[i][0])>1 and dir_list[i][0][1] in possible_dir):
                        temp.append(dir_list[i][0][1])
                        emergency = False
                    if(emergency):
                        if(can_cloak):
                            can_cloak=False
                            flag = True
                            temp.append(dir_list[i][0][0])
                        elif(len(possible_dir)>0):
                            if(last_round_move in possible_dir):
                                possible_dir.remove(last_round_move)
                                possible_dir.append(last_round_move)
                            temp.append(possible_dir[0])
                        else:
                            temp.append('-')
                self.last_round_movement[index]=temp[0]
                new_dir.append([tuple(temp),flag])
                locations[i] = defence.ForwardMoving(pirates[i],temp[0])
        for direction in new_dir:     
            direction[0] = direction[0][0]
        return new_dir

    def GetLocations(self,game,pirates):
        locations = []
        for pirate in pirates:
            locations.append(pirate.location)
        return locations

    def get_allies_locations(self,i,locations):
        if(locations[i] == locations[-1]):
            return locations[:i]
        return locations[:i] + locations[i+1:]
