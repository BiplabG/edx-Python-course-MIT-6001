import math #Math module imported for performing math operations
def polysum(n, s):
    """
    Input: n-number of sides and s-length of each side.
    returns the sum of area and square of perimeter
    """
    area = (0.25*n*s**2)/(math.tan(math.pi/n)) #Calculates area
    perimeter = n*s #Calculates perimeter
    sum = area + (perimeter**2) #Calculates sum
    return round(sum, 4)
