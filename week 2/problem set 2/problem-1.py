def credit_card_balance(bal, air, mpr):
    for i in range(1, 13):
        payment = bal*mpr
        unpaid_bal = bal - payment
        interest = air/12 * unpaid_bal
        bal = unpaid_bal + interest
    return round(bal, 2)

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
outstanding_balance = credit_card_balance(balance, annualInterestRate, monthlyPaymentRate)
print("Remaining balance", outstanding_balance)
