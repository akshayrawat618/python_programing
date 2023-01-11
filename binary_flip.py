str = "0001010111"

def flip(ch):
    return '1' if (ch == '0') else '0'

def getflipwithstartingcharacter(str, expected):
    flipcount = 0 
    for i in range(len(str)):
        if  (str[i] != expected ):
            flipcount += 1
        
        expected = flip(expected)
    return flipcount


    