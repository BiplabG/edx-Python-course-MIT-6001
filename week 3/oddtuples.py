aTup = (1, 2, 4, 6, 23, 45, 12)

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    l = len(aTup) + 1
    return aTup[0:l:2]
print(oddTuples(aTup))
