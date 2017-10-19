#GCD using a recursion
def gcdRecur(a,b):
    """Input: integers a and b
        Output: GCD number."""
    if (b == 0):
        return a
    else:
        return gcdRecur(b, a%b)
a = int(input("Enter a:"))
b = int(input("Enter b:"))
gcd = gcdRecur(a,b)
print(gcd)
