import my_bot
import math

def CheckEnemies(game,pirate,direction):
    evil_pirates = game.enemy_pirates()
    dangers = int(0)
    for baddy in evil_pirates:
        if(game.distance(pirate,baddy)<6):
            dangers = dangers + 1
            x =  pirate.location[1] - baddy.location[1] ##distance from pirate, horizon
            y =  pirate.location[0] - baddy.location[0] ##distance from pirate, vertical                                                                                                                
            if(math.fabs(x) > math.fabs(y)):
                if(x<0):
                    direction = 'w'
                else:
                    direction = 'e'
            else:
                if(y<0):
                    direction = 's'
                else:
                    direction = 'n'
    return dangers, direction
def CheckFriends(game, pirate, direction):
    helpers = int(0)
    pirates=game.my_pirates()
    for pirateFriend in pirates:
            x = pirate.location[1] - pirateFriend.location[1]
            y = pirate.location[0] - pirateFriend.location[0]
            if((direction=='w')and ((math.fabs(y)<4)and (x<0 and x>-3))):
                helpers = int(helpers) + 1
            if((direction=='e')and ((math.fabs(y)<4)and (x<3 and x>0))):
                helpers = int(helpers) + 1
            if((direction=='n')and ((math.fabs(x)<4)and (y>3 and y<0))):
                helpers = int(helpers) + 1
            if((direction=='s')and ((math.fabs(x)<4)and (y>0 and y<-3))):
                helpers = int(helpers) + 1
    return helpers
def Main_Defence(game, pirate, destination):
    dangers, direction = CheckEnemies(game, pirate,destination)
    helpers = CheckFriends(game, pirate, direction)
    game.debug("pirate going to "+direction)
    if(dangers < helpers):
        return destination
    else:
        return direction
    
