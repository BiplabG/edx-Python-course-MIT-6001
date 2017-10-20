#balance = 3329
#annualInterestRate = 0.2

dyn_balance = balance
monthlyInterestRate = annualInterestRate / 12
lowerBound = balance / 12
upperBound = (balance * (1+monthlyInterestRate)**12)/12
fixedPayment = 0

while(abs(dyn_balance) > 0.01):
    dyn_balance = balance
    fixedPayment = 0.5*(lowerBound + upperBound)

    for i in range(1, 13):
        unpaidBalance = dyn_balance - fixedPayment
        interest = monthlyInterestRate * unpaidBalance
        dyn_balance = unpaidBalance + interest
    if (dyn_balance > 0):
        lowerBound = fixedPayment
    elif (dyn_balance < 0):
        upperBound = fixedPayment

print("Lowest Payment:", round(fixedPayment, 2)) 
