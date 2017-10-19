def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    mid = int(len(aStr)/2) - 1
    if (len(aStr)==0):
        return False
    elif (len(aStr)==1):
        return (char==aStr)
    else:
        if(char == aStr[mid]):
            return True
        elif(char < aStr[mid]):
            return isIn(char, aStr[0: mid])
        else:
            return isIn(char, aStr[mid+1:])
