##This file represents the pirate game and holds all the classes necessery for the miniMax Alpha Beta scan that we will
##preform later in order to identify what is the best move to be executed
import math

class MaxTree:
    
    def __init__(self,score):
        self.currentMap = None
        self.next = []
        self.score = int(score)
        
    def SetMap(self,currentMap):
        self.currentMap = currentMap
        self.score+=currentMap.Get_Points()
        
    def Explore(self,depth,game):
        ##depth must be int variable
        game.debug("1")
        if(depth > 0):
            game.debug("2")
            self.next=[]
            game.debug("3")
            ##'-' represents no movement during this round
            directions = ['n','e','s','w','-']
            game.debug("4")
            for d1 in directions:
                for d2 in directions:
                    for d3 in directions:
                        for d4 in directions:
                            for d5 in directions:
                                game.debug("5")
                                self.next.append(MinTree(self.score))
                                self.next[-1].SetMap(CreateNextMap(currentMap))
                                self.next[-1].currentMap.MoveMyPirates(d1,d2,d3,d4,d5)
                                game.debug("6")
                                self.next[-1].Explore(depth-1,game)
                                game.debug("7")
                                self.ReturnMap(d1,d2,d3,d4,d5)

    def GetNext(self):
        return self.next
    
    def GetMap(self):
        return self.currentMap

    def GetScore(self):
        return self.score

    def IncTree(self):
        for son in self.next:
            if(son==None):
                self.Explore(2)
            else:
                son.IncTree()
            
                                

class MinTree:
    
    def __init__(self,score):
        self.currentMap = None
        self.next = []
        self.score = score
        
    def SetMap(self,currentMap):
        self.currentMap = currentMap
        self.score+=currentMap.Get_Points()
        
    def Explore(self,depth,game):
        game.debug("!!")
        if(depth > 0):
            self.next=[]
            ##'-' represents no movement during this round
            directions = ['n','e','s','w','-']
            for d1 in directions:
                for d2 in directions:
                    for d3 in directions:
                        for d4 in directions:
                            for d5 in directions:
                                self.next.append(MaxTree(self.score))
                                self.next[-1].SetMap(self.currentMap)
                                self.next[-1].currentMap.MoveEnemyPirates(d1,d2,d3,d4,d5)
                                game.debug(str(depth-1))
                                self.next[-1].Explore(depth-1,game)
                                game.debug(str(depth-1))
                                self.ReturnMap(d1,d2,d3,d4,d5)
        else:
            game.debug("Depth is zero!!!")
            
            
    def GetNext(self):
        return self.next
    
    def GetMap(self):
        return self.currentMap

    def GetScore(self):
        return self.score

    def ReturnMap(self,d1,d2,d3,d4,d5):
        reverseDir = {'n':'s','e':'w','s':'n','w':'e','-':'-'}
        self.currentMap.MoveEnemyPirates(reverseDir[d1],reverseDir[d2],reverseDir[d3],reverseDir[d4],reverseDir[d5])

##the representive of a map 
class Map: 
    def __init__(self,limits,myPirates,enemyPirates,islands):
        self.limits = limits
        self.islands = islands
        self.myPirates = myPirates
        self.enemyPirates = enemyPirates
 
    def GetMyPirates(self):
        return self.myPirates

    def GetEnemyPirates(self):
        return self.enemyPirates
    
    def MoveMyPirates(self,d1,d2,d3,d4,d5):
        directions = [d1,d2,d3,d4,d5]
        for i in xrange(len(self.myPirates)):
            self.myPirates[i].Move(directions[i])
            self.IsMyPirateAlive(self.myPirates[i])
            for island in self.islands:
                if self.myPirates[i].GetLocation() == island.GetLocation():
                    island.IncreaseTurns(int(1))
                    
    def MoveEnemyPirates(self,d1,d2,d3,d4,d5):
        directions = [d1,d2,d3,d4,d5]
        for i in xrange(len(self.enemyPirates)):
            self.enemyPirates[i].Move(directions[i])
            self.IsMyPirateAlive(self.myPirates[i])
            for island in self.islands:
                if self.enemyPirates[i].GetLocation() == island.GetLocation():
                    island.IncreaseTurns(int(-1))
                    
    def IsMyPirateAlive(self,pirate):
        if(pirate.IsDrowned()):
            pirate.RoundPassed()
            return
        enemies = int(0)
        allies = int(-1)
        myLocation = pirate.GetLocation()
        for baddy in self.enemyPirates:
            if(baddy.IsDrowned()):
                continue
            enemyLocation = baddy.GetLocation()
            y = math.fabs(int(myLocation[0])-int(enemyLocation[0]))
            x = math.fabs(int(myLocation[1])-int(enemyLocation[1]))
            if(x<4 and y<4):
                if(y<2):
                    enemies+=1
                elif(x<3 and y<3):
                    enemies+=1
                elif(x<2):
                    enemies+=1
        for ally in self.myPirates:
            if(ally.IsDrowned()):
                continue
            allyLocation = ally.GetLocation()
            y = math.fabs(myLocation[0]-allyLocation[0])
            x = math.fabs(myLocation[1]-allyLocation[1])
            if(x<4 and y<4):
                if(y<2):
                    allies+=1
                elif(x<3 and y<3):
                    allies+=1
                elif(x<2):
                    allies+=1
        if(enemies >= allies):
            pirate.Drown()

    def IsEnemyPirateAlive(self,pirate):
        if(pirate.IsDrowned()):
            pirate.RoundPassed()
            return
        enemies = int(0)
        allies = int(-1)
        myLocation = pirate.GetLocation()
        for baddy in self.myPirates:
            if(baddy.IsDrowned()):
                continue
            enemyLocation = baddy.GetLocation()
            y = math.fabs(myLocation[0]-enemyLocation[0])
            x = math.fabs(myLocation[1]-enemyLocation[1])
            if(x<4 and y<4):
                if(y<2):
                    enemies+=1
                elif(x<3 and y<3):
                    enemies+=1
                elif(x<2):
                    enemies+=1
        for ally in self.enemyPirates:
            if(ally.IsDrowned()):
                continue
            allyLocation = ally.GetLocation()
            y = math.fabs(myLocation[0]-allyLocation[0])
            x = math.fabs(myLocation[1]-allyLocation[1])
            if(x<4 and y<4):
                if(y<2):
                    allies+=1
                elif(x<3 and y<3):
                    allies+=1
                elif(x<2):
                    allies+=1
        if(enemies >= allies):
            pirate.Drown()
        

                  
    def Get_Points(self):
        myCapturedIslands = int(0)
        enemyCapturedIslands = int(0)
        for island in self.islands:
            if island.GetOwner()==int(1):
                myCapturedIslands+=1
            elif island.GetOwner()==int(-1):
                enemyCapturedIslands+=1
        if(myCapturedIslands==0):
            myScore = int(0)
        else:
            myScore = math.pow(2,myCapturedIslands-1)
        if(enemyCapturedIslands==0):
            enemyScore = int(0)
        else:
            enemyScore = math.pow(2,enemyCapturedIslands-1)
        relativeScore = myScore - enemyScore
        return relativeScore
            

##the representive of the Island class
class Island: 
    def __init__(self,y,x):
        self.x = x
        self.y = y
        ##0 = neutrel, 1 = mine, -1 = opponent's
        self.owner = int(0) 
        self.turns = int(0)
        self.teamCapturing = int(0)
        
    def GetLocation(self):
        return [self.x,self.y]
    
    def GetOwner(self):
        return self.owner
    
    def GetTurns(self):
        return self.turns
    
    def ChangeOwner(self, owner):
        self.owner = owner
        
    def GetTeamCapturing(self):
        return self.teamCapturing
    
    def SetTeamCapturing(self,newOwner):
        self.owner = newOwner
        
    def IncreaseTurns(self,player):
        if(self.turns==0):
            self.SetTeamCapturing(player)
        self.turns+=1
        if(self.turns == 20):
            self.owner+=player
            

 ##the representive of the Pirate class
class Pirate:
    def __init__(self,y,x,owner,startingLocation):
        self.location = [y,x]
        self.owner = owner
        self.isDrowned = False
        self.turnsToRevive = 0
        self.startingLocation = startingLocation
    def GetLocation(self):
        return self.location
    def Move(self,d):
        if(d!='-'):
            directionsList = {'w':[self.location[1]-1,self.location[0]],'e':[self.location[1]+1,self.location[0]],'n':[self.location[1],self.location[0]+1],'s':[self.location[1],self.location[0]-1]}
            if(directionsList[d][0] < 39 and directionsList[d][1] < 47):
                self.location = directionsList[d]
    def Drown(self):
        self.isDrowned = True
        self.turnsToRevive = int(60)
        self.location = self.startingLocation
    def RoundPassed(self):
        self.turnsToRevive-=1
        if(self.turnsToRevive==0):
            self.isDrowned = False
    def IsDrowned(self):
        return self.isDrowned
        

def GetIslands(game):
    newIslands = []
    islands = game.islands()
    for island in islands:
        y = island.location[0]
        x = island.location[1]
        newIslands.append(Island(y,x))
    return newIslands

def GetPirates(game,owner):
    newPirates = []
    if(owner==1):
        pirates = game.all_my_pirates()
    else:
        pirates = game.all_enemy_pirates()
    for pirate in pirates:
        y = pirate.location[0]
        x = pirate.location[1]
        startingLocation = pirate.initial_loc
        newPirates.append(Pirate(int(y),int(x),owner,startingLocation))
    return newPirates

def CreateMap(game):
    limits = [game.get_rows(),game.get_cols()]
    islands = GetIslands(game)
    myPirates = GetPirates(game,1)
    enemyPirates = GetPirates(game,-1)
    newMap = Map(limits,myPirates,enemyPirates,islands)
    return newMap

def CreateNextMap(currentMap):
    limits = currentMap.limits
    myPirates = currentMap.myPirates
    enemyPirates = currentMap.enemyPirates
    islands = currentMap.islands
    newMap = Map(limits, myPirates, enemyPirates, islands)
    


def do_turn(game):
    if(game.get_turn()==1):
        tree = MaxTree(0)
        tree.SetMap(CreateMap(game))
        tree.Explore(int(20),game) 
    game.debug("!!!!")








    
        
        
        
                            
                            
        
