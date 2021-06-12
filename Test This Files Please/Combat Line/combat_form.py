##This is for only One island, Needs  to be modified if wanted on other files.
class combat_form:
    def __init__(self,game):
        self.x=5
        
    def Return_Shortest_Dist(self,game,pirates,island):
        dist = []
        for pirate in pirates:
                dist.append(game.distance(pirate,island))
        minIndex = dist.index(min(dist))
        pirate = pirates[minIndex/len(islands)]
        return pirate
        
    ## This function Finds the Leader
    ## A leader is a pirate that leads the other pirates
    ## We define a leader as the closest Pirate to the Island
    def FindLeader(self,game):
        piratesAlive=game.my_pirates()
        islandToAttack=game.islands()[0]
        leaderPirate=self.Return_Shortest_Dist(game,piratesAlive,islandToAttack)
        return leaderPirate

    ## This function checks if all our pirates are alive
    ## if they are it returns True
    ## else it returns False
    def CheckIfAllAlive(self,game):
        if len(game.my_lost_pirates())==0:
            ##Everyone is alive
            return True
        ##Someone is dead :(
        return False
        
    ## This function tells the pirates what to do if not all of the crews are alive
    ## Such as tells ones to go back, or stay in place
    ## This will probably need Defence1 for staying alive.
    def StandBy(self,game,leaderPirate):

        



    ## This function tells all of the crew how to form so it will make
    ## efficient Combat.
    def TakeCombatForm(self,game):
        ##Movements_for_Pirates_to_do Will have the movement of each pirate to do
        ##according to its place in the list
        ## First Pirate is First Place , and so on
        leaderPirate=self.FindLeader(game)
        Movements_for_Pirates_to_do=[]
        direction_to_sail_for_leader=self.CheckWhichDirectionLeaderHasToSail(game,leaderPirate)
        if self.CheckIfAllAlive(game):
            Movements_for_Pirates_to_do=self.FormALine(game,leaderPirate,directionToSail):
        else:
            Movements_for_Pirates_to_do=self.StandBy(game,leaderPirate)
        return Movements_for_Pirates_to_do
        
    
    ## This function Forms virtualy around the leader Pirate
    ## A line
    ## Returns the best moves for each pirate
    def FormALine(self,game,leaderPirate,directionToSail):
        if self.CheckIfInLine(game,leaderPirate,directionToSail):
            ## If this is True it means we can move our pirates to the direction
            return [directionToSail]*len(game.all_my_pirates())
        else:
            
            ## We are supposed to move every pirate to its needed place
            ## The Leader is supposed to be in the middle
            ## If our crew is not in line ,The leader should take certain movements to help his crew regroup.
            ##For now its just staying in place
            list_of_pirates=game.all_my_pirates()
            ## The Leader Pirate moves independetly
            CreateLocations(self,game,leaderPirate,list_of_pirates,directionToSail)
            

        
    def CheckWhichDirectionLeaderHasToSail(self,game,leaderPirate):
        listOfDirections=get_directions(leaderPirate.location,game.islands().[0]
        ## The first one is ussually the best one
        return listOfDirections[0]

        ##Checks If the pirates are facing the needed direction and if they are in the right place.                                
    def CheckIfInLine(self,game,dire,pirates):
    if dire=="s" or dire=="n":
        line="Horizontal"
    elif dire=="e" or dire=="w":
        line="Vertical"
    list_of_row_locations=[]
    list_of_col_locations=[]
    for pirate in pirates:
        list_of_row_locations.append(pirate.location[0])
        list_of_col_locations.append(pirate.location[1])
        list_of_row_locations.sort()
        list_of_col_locations.sort()
    if line=="Horizontal":
        ## all rows are supposed to match
        ## and all cols are supposed to be with a 1 diffrence
        temp=list_of_row_locations[0]
        for row in list_of_row_locations:
            if temp!=row:
                return False
        temp=list_of_col_locations[0]-1
        for col in list_of_col_locations:
            temp+=1
            if temp!=col:
                return False
        return True
    elif line=="Vertical":
        ## all cols are supposed to match
        ## and all rows are supposed to be with a 1 diffrence
        temp=list_of_col_locations[0]
        for col in list_of_col_locations:
            if temp!=col:
                return False
        temp=list_of_row_locations[0]-1
        for row in list_of_row_locations:
            temp+=1
            if temp!=row:
                return False
        return True
                    
        
    def CreateLocations(self,game,Leader,PiratesWithLeader,dire):
##        if dire=="s" or dire=="n":
##            line="Horizontal"
##        elif dire=="e" or dire=="w":
##            line="Vertical"
##        list_of_row_locations=[]
##        list_of_col_locations=[]
##        amountOfPirates=len(PiratesWithLeader)
##        PiratesWithLeader.remove(Leader)
##        if amountOfPirates%2==1:
##            amountOnSide1=int(amountOfPirates/2)
##            amountOnSide2=int(amountOfPirates/2)
##            LocationsOnSide1=[]
##            LocationsOnside2=[]
##        ##if amountOfPirates%2==0:
##        leaderRow=Leader.location[0]
##        leaderCol=Leader.location[1]
##        if line=="Horizontal":
##            for i in amountOnSide1:
##                ## all rows are supposed to match
##                ## and all cols are supposed to be with a 1 diffrence
##                
    

                
            
            
        

           
