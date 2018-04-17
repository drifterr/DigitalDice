import math
import cryptography as crypto
import random as r


#'rolls' a dice with the provided number of sides but expanding the distubution givven by r.random (which goes from 0 to 1)
#to fill the desired space and then takes the ceiling to make the result start from '1'
def die(sides):
    if isinstance(sides, int):
        return (math.ceil((sides) * r.random()))
    #die can also take a tuple containing a name, and a list of canidate responses. this is handeled by recursivly calling die
    #and asking for a number the length of the array and that array object is returned after zero referencing it. 
    else:
        x,y = sides
        return y[die(len(y))-1]

def dieName(die):
    if isinstance(die, tuple):
        return die[0]
    else:
        return 'D' + str(die)

def isIntList(query):
    if not isinstance(query, list):
        return False
    else:
        for x in query:
            if not isinstance(x, int):
                return False
        return True