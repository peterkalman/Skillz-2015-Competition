class st1:
    def __init__(self):
        self.x=0
    def Move(self,game,pirates):
        for p in pirates:
            game.set_sail(p, 'n')
    def get_rank(self,game,pirates):
        return 25,pirates
