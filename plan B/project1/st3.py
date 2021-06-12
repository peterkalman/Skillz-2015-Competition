class st3:
    def __init__(self):
        self.x=0
    def Move(self,game,pirates):
        maximum=len(notmyisl)
        notmyisl=game.not_my_islands()
        for i in pirates:
            if not game.is_capturing(i):
                if i.id<maximum:
                    direction = game.get_directions(i, notmyisl[i.id])[0]
                    game.set_sail(i, direction)
                else:
                    direction = game.get_directions(i, notmyisl[0])[0]
                    game.set_sail(i, direction)
    def get_rank(self,game,pirates):
        rank=100
        maximum=len(notmyisl)
        if not game.get_turn<150 or not maximum<3:
            rank=0
        return rank,pirates
