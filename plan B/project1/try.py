def IsItTheSame(locationtogo,locationnow):
    return locationtogo==locationnow
def do_turn(game):
    isl=game.islands()
    p=game.all_my_pirates()
    if game.get_turn()==1:
        game.set_sail(p[0], 's')
        game.set_sail(p[1], 's')
        game.set_sail(p[3], 'e')
        game.set_sail(p[4], 'e')
    elif game.get_turn()==2:
        game.set_sail(p[0], 'e')
        game.set_sail(p[4], 'n')
    elif game.get_turn()==3:
        game.set_sail(p[0], 'e')
    else:
        if len(p)%2==0:
            leader=p[len(p)/2-1]
        else:
            leader=p[len(p)/2]
        loc=isl[0].location
        if leader.turns_to_revive!=None:
            leader=p[leader.id-1]
        elif p[leader.id-1].turns_to_revive==None:
            x1=abs(loc[0]-leader.location[0])
            x2=abs(loc[0]-p[leader.id-1].location[0])
            if x2<x1:
                leader=p[leader.id-1]
        p.remove(leader)
        direction = game.get_directions(leader, isl[0])[0]
        game.set_sail(leader, direction)
        location=(loc[0]-1,loc[1])
        direction = game.get_directions(p[0], location)[0]
        game.set_sail(p[0], direction)
        location=(loc[0]+1,loc[1])
        direction = game.get_directions(p[3], location)[0]
        game.set_sail(p[3], direction)
        location=(loc[0],loc[1]-1)
        direction = game.get_directions(p[1], location)[0]
        game.set_sail(p[1], direction)
        location=(loc[0]+1,loc[1]-1)
        direction = game.get_directions(p[4], location)[0]
        game.set_sail(p[4], direction)

