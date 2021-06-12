
## You get to this function when we are sure that there are no enemy pirates and we have all of the islands

##        # initialize zones and create enemy_zone lists
##        for player, zone_data in enumerate(map_data['zones']):
##            self.zones[player] = self.get_zone_locations(zone_data[0], zone_data[1:])
##        #self.print_zone()


                                                                                ## Self Note
                                                                                ## The map starts from Top Left (0,0)
                                                                                ## End in (38,46)

                                                                                ##Top Pirates

                                                                                ##Pirate 0 => Row 1||Col 29
                                                                                ##Pirate 1 => Row 1||Col 31
                                                                                ##Pirate 2 => Row 1||Col 33
                                                                                ##Pirate 3 => Row 1||Col 35
                                                                                ##Pirate 4 => Row 1||Col 37

                                                                                ##Safe Zone is a figure
                                                                                ##Points
                                                                                ##(0,41)
                                                                                ##(5,41)
                                                                                ##(0,34)
                                                                                ##(5,34)

                                                                                ##Bottom Pirates

                                                                                ##Pirate 0 => Row 37||Col 9
                                                                                ##Pirate 1 => Row 37||Col 11
                                                                                ##Pirate 2 => Row 37||Col 13
                                                                                ##Pirate 3 => Row 37||Col 15
                                                                                ##Pirate 4 => Row 37||Col 17

                                                                                ##Safe Zone is a figure
                                                                                ##Points
                                                                                ##(38,5)
                                                                                ##(34,5)
                                                                                ##(38,12)
                                                                                ##(34,12)



Marked=[]
RowsSize=game.get_rows()
ColSize=game.get_cols()

def FoundMiddle(x,y):
    ans=(x+y)/2
    return int(ans)
## Needs an out function that finds the side at the start so we won't have problems later on.
##Returns The Cordinates of point to defend
##Side-> The Place the enemy starts from
def SearchForSafeZoneToGo(side):
    for i in xrange(RowSize-1):## I=ROW
        for j in xrange(ColSize-1):## J=COL
            my_location=(i,j)
            if not is_passable(my_location):
                Marked.append(my_location)

    ## First Value in marked is top_left location Marked[0]
                
    ## Last  value in marked is bottom_right location Marked[-1]
        FirstRow=Marked[0].[0]
        FirstCol=Marked[0].[1]
        LastRow=Marked[-1].[0]
        LastCol=Marked[-1].[1]
                
    if side=="top":
        new_loc=(LastRow+2,FindMiddle(FirstCol,LastCol))
    if side=="right":
        new_loc=(FindMiddle(FirstRow,LastRow),FirstCol-2)
    if side=="bottom":
        new_loc=(FirstRow+2,FindMiddle(FirstCol,LastCol))
    if side=="left":
        new_loc=(FindMiddle(FirstRow,LastRow),FirstCol+2)

        
    if side=="top_right":
        new_loc=(LastRow+2,FirstCol-2)
    if side=="top_left":
        new_loc=(LastRow+2,LastCol+2)
    if side=="bottom_left":
        new_loc=(FirstRow-2,LastCol+2)
    if side=="bottom_right":
        new_loc=(FirstRow-2,FirstCol-2)
    
    return new_loc ## The point to defend







                

            
