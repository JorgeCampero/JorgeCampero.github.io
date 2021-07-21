try:
    Loan_Amount = float(input("\nPlease enter the amount desired ($1,000.00 to $10,000.00): $"))
except ValueError:
    Loan_Amount = float(input("\nInvalid amount, please enter the amount desired ($1,000.00 to $10,000.00): $"))

try:
    Number_Of_Instalments = int(input("\nPlease enter the number of instalments (3,6,9,12): "))
except ValueError:
    Number_Of_Instalments = int(input("\nPlease enter the number of instalments (3,6,9,12): "))
    

while Loan_Amount <1000.00:
        Loan_Amount = float(input("\nInvalid amount, please enter the amount desired ($1,000.00 to $10,000.00): $"))

while Loan_Amount >10000.00:
    Loan_Amount = float(input("\nInvalid amount, please enter the amount desired ($1,000.00 to $10,000.00): $"))

while Number_Of_Instalments not in [3,6,9,12]:
       Number_Of_Instalments = int(input("\nInvalid instalment, please enter the number of instalments (3,6,9,12): "))

if Loan_Amount <=4999.99:
    Interest = Loan_Amount * 0.10
    Instalment = (Loan_Amount + Interest)/Number_Of_Instalments

else:
    Loan_Amount > 5000.00
    Interest = Loan_Amount * 0.08
    Instalment = (Loan_Amount + Interest)/Number_Of_Instalments

Total_Due = Loan_Amount+Interest


print ("\nThe amount to be paid per instalment is: $",round(Instalment,2),", and the total due is: $",round(Total_Due,2))