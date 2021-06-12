import math
def ABPruning(Tree,a,b,flag):
    if Tree.Next()==[]:
        return Tree.score
    if flag:
        for i in Tree.Next():
            a=math.max(a,ABPruning(i,a,b,False))
            if a>=b:
                break
        return a
    elif !flag:
        for i in Tree.Next():
            b=math.min(i,a,b,True)
            if a>=b:
                break
        return b
