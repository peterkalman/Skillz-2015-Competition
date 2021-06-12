class st3:
    def __init__(self):
        self.x = 5
        
    def get_rank(self,game,pirates):
        if(len(game.islands())==1):
            self.island = game.islands()[0]
            return 101, pirates
        else:
            return 0,pirates
    def Move(self,game,pirates):
        if(self.Check_Reformation(game)):
            base_loc = pirates[0].location
            base_x = int(base_loc[1])
            for pirate in pirates:
                location = pirate.location
                directions = game.get_directions(pirate,(location,base_x))
                game.set_sail(pirate, directions[0])
        elif(self.island.team_capturing!=game.ME):
            for pirate in pirates:
                game.set_sail(pirate,'w')
                
        

    def Check_Reformation(self,game):
        if(game.get_turn()<5):
           return True
        if(self.island.owner!=game.ME and self.island.team_capturing!=game.ME):
           loc = []
           for pirate in game.my_pirates():
               
               loc.append(pirate.location[1])
            
           loc = list(set(loc))
           if(loc[0] != loc[-1]):
               return True
        return False
               
           
        

    def Check_Spot(self,game,this_pirate,direction):
        dest = game.destination(this_pirate, direction)
        for pirate in game.my_pirates():
            if not(pirate==this_pirate) and pirate.location==dest:
                return True
        return False
    
    def Check_Formation(self,pirates):
        for i in xrange(len(pirates)):
            if(pirates[i].location!=self.formPosition[i]):
                return True
        return False
                    
