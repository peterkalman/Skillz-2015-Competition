class st4:
    def __init__(self):
        self.x=0
    def Move(self,game,pirates):
        distances={}
        lists={}
        maximum=len(notmyisl)
        notmyisl=game.not_my_islands()
        for i in pirates:
            lists["l"+str(i.id)]=[]
            for j in notmyisl:
                distances[game.distance(i,j)]=j
                lists["l"+str(i.id)].append(game.distance(i,j))
            lists["l"+str(i.id)].sort()
            if not game.is_capturing(i):
                if i.id<maximum:
                    direction = game.get_directions(i, distances[lists["l"+str(i.id)][0]])[0]
                    game.set_sail(i, direction)
                else:
                    direction = game.get_directions(i, distances[lists["l"+str(i.id)][0]])[0]
                    game.set_sail(i, direction)
    def get_rank(self,game,pirates):
        rank=100
        maximum=len(notmyisl)
        if game.get_turn<150 or maximum<3:
            rank=0
        return rank,pirates
    
