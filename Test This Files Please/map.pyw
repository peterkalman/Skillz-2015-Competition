##Recieves a list of tuples which are locations and a list of movement
def ForwardMoving(list_of_our_pirates,list_of_movement):
    newlist=[]
    counter=0
    ## Adds the movement to the locations of the pirates and return a list of tuples.
    for i in list_of_our_pirates:                       
        temprow=i[0]
        tempcol=i[1]
        if list_of_movement[counter]=="n":
            temprow-=1
        else:
            if list_of_movement[counter]=="e":
                tempcol+=1
            else:
                if list_of_movement[counter]=="s":
                    temprow+=1
                else:
                    if list_of_movement[counter]=="w":
                        tempcol-=1
                    else:
                        if list_of_movement[counter]=="-":
                            ##do nothing ?
        temp=(temprow,tempcol)
        newlist.append(temp)
        counter+=1
    return newlist

    
