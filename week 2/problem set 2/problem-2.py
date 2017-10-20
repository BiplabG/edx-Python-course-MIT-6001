#balance = 3329
#annualInterestRate = 0.2

dyn_balance = balance
monthlyInterestRate = annualInterestRate / 12
fixedPayment = 0
while(dyn_balance > 0):
    dyn_balance = balance
    fixedPayment += 10

    for i in range(1, 13):
        unpaidBalance = dyn_balance - fixedPayment
        interest = monthlyInterestRate * unpaidBalance
        dyn_balance = unpaidBalance + interest

print("Lowest Payment:", fixedPayment) 
