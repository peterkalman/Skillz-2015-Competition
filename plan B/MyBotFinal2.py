def do_turn(game):
    notmyisl=game.not_my_islands()
    isl=game.islands()
    maximum=len(notmyisl)
    if maximum==0:
        return
    lists={}
    distances={}
    p=game.my_pirates()
    if game.get_turn<150 or maximum<3:
        for i in p:
            if not game.is_capturing(i):
                if i.id<maximum:
                    direction = game.get_directions(i, notmyisl[i.id])[0]
                    game.set_sail(i, direction)
                else:
                    direction = game.get_directions(i, notmyisl[0])[0]
                    game.set_sail(i, direction)
    else:
        for i in p:
            lists["l"+str(i.id)]=[]
            for j in notmyisl:
                distances[game.distance(i,j)]=j
                lists["l"+str(i.id)].append(game.distance(i,j))
            lists["l"+str(i.id)].sort()
        for i in p:
            if not game.is_capturing(i):
                if i.id<maximum:
                    direction = game.get_directions(i, distances[lists["l"+str(i.id)][0]])[0]
                    game.set_sail(i, direction)
                else:
                    direction = game.get_directions(i, distances[lists["l"+str(i.id)][0]])[0]
                    game.set_sail(i, direction)
