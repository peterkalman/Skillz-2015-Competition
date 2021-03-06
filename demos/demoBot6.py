# 2015.03.18 21:00:35 ???? ???? ???????
#Embedded file name: /home/amitayd/code/pirates/cyber-pirates/admin-tools/simulator/bots/python/Demo6.py
""" Demo 6 sends all pirates a time to conquer the closest island """

def do_turn(game):
    if len(game.not_my_islands()) == 0:
        return
    assigned_pirates = set()

    def find_nearest_pirate(island):
        pirates = filter(lambda p: not p.is_lost and p not in assigned_pirates, game.my_pirates())
        if len(pirates) == 0:
            return None
        return min(pirates, key=lambda p: game.distance(island, p))

    for island in game.not_my_islands():
        pirate = find_nearest_pirate(island)
        if pirate:
            directions = game.get_directions(pirate, island)
            assigned_pirates.add(pirate)
            game.set_sail(pirate, directions[0])

    for pirate in filter(lambda p: not p.is_lost and p not in assigned_pirates, game.my_pirates()):
        directions = game.get_directions(pirate, (game.rows / 2, game.cols / 2))
        game.set_sail(pirate, directions[0])
+++ okay decompyling demoBot6.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.03.18 21:00:35 ???? ???? ???????
