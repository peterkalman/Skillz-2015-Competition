class st2:
    def __init__(self):
        self.x=0
    def Move(self,game,pirates):
        for p in pirates:
            game.set_sail(p, 's')
    def get_rank(self,game,pirates):
        return 50,pirates
