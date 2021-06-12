import defence
def Get_Nearest(game,pirate,islands):
    d={}
    l=[]
    for j in islands:
        d[game.distance(pirate,j)]=j
        l.append(game.distance(pirate,j))
    l.sort()
    game.debug(l)
    return d[l[0]]
def Move(game):
    plist=game.my_pirates()
    netural=game.neutral_islands()
    enemy=game.enemy_islands()
    for pirate in plist:
        if len(netural)!=0:
            near=Get_Nearest(game,pirate,netural)
            netural.remove(near)
        elif len(enemy)!=0:
            near=Get_Nearest(game,pirate,enemy)
            enemy.remove(near)
        else: return
        direction = game.get_directions(pirate, near)[0]
        game.set_sail(pirate, defence.Main_Defence(game,pirate,direction))
