salary=int(input("enterr the salary: "))
age=int(input("enterr the age: "))
if(salary>=20000 or age<=25):
    loan=int(input("enter the loan amount: "))
    if(loan<=50000):
        print("you are eligiblr for loan")
    else:
        print("maximum loan amount is the 50000")
else:
    print("you are not eligiblr for loan")