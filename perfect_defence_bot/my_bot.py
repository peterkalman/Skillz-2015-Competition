from st1 import st1
from st2_new import st2
from st4 import st4
strategies=[st1(),st2(),st4()]
def Get_Max(ranks):
    maximum = ranks[0]
    for i in ranks:
        if i[0]>maximum[0]:
            maximum=i
    index = ranks.index(maximum)
    best_st = strategies[index]
    return best_st,maximum[1]
def do_turn(game):
    ranks=[]
    remaining_pirates=game.my_pirates()
    while len(remaining_pirates)!=0:
        for st in strategies:
            ranks.append(st.get_rank(game,remaining_pirates))
        best_st,pirates=Get_Max(ranks)
        best_st.Move(game,pirates)
        for pirate in pirates:
            remaining_pirates.remove(pirate)
            
            
