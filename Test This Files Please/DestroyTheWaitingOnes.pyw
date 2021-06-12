## Function that when we finish capturing an island
## we check in the radius of 3->6 (if it is below 3 it will be combat radius)
## If there is an enemy , if there is we check if we can kill him , if we can kill him
## we kill him,else we do not sacrafice our ship
## !!!We asume that the enemy will wait for us to finish capturing and then take our island!!!

## Function CheckRadius
## Recieves Locations of enemy pirates and island
## Enemy Pirates are in 1 list while the island is constant.

##Returns list with the enemy pirates that are in the radius
##if there are no pirates return an empty list.



def CheckRadius (list_of_enemy_pirates,myisland):
    distance1=[]
    for enemy_pirates in list_of_enemy_pirates:
        if game.distance(enemy_pirates,myisland)<=5:
            distance1.append(enemy_pirates)
    return distance

## Function Surprise
## Recieves List of Enemies , my island and my pirate.
## Returns the direction to sail To destroy enemyPirates
## returns 'NoDanger' if after finishing capturing there are no enemies
## returns 'RegualrTurn' if we were not capturing for longer then 1 turn
## returns 'BeingCaptured' If we are capturing at the moment the island
def Surprise (list_of_enemy_pirates,myisland,myPirate):
        if (myisland.team_capturing==ME):
            if myisland.turns_being_captured>2:
                if myisland.turns_being_captured==capture_turns:
                    dist=CheckRadius(list_of_enemy_pirates,myisland)
                    if len(dist)!=0:
                        ## THERE IS DANGER!
                        return CheckWhereToSail(myPirate,enemyPirateToDestroy)
                        ## outside of this function Before you set sail.
                        ## CHECK IF YOU CAN WIN the Enemy.
                    else:
                        ##No Danger :)
                        return "NoDanger"
                return "BeingCaptured"
        return "RegularTurn"

## The function Name speaks for itself
def CheckWhereToSail(myPirate,enemyPirateToDestroy):
    l1=game.get_directions(myPirate,enemyPirateToDestroy)
    return l1[0]
