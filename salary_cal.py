print("""***Hi, Welcome!***
        ***The program starts***""")

name = input('Enter Name: \n')
hour = input('Enter Hours: \n')
salary = input ('Enter Salary: \n')

houri = int(hour)
salaryi = int(salary)

if houri > 40:
    print(name,'Worked Overtime!')
    netsalary = salaryi * houri
    ot = (houri - 40) * (salaryi * 1.5)
    fullsalary = netsalary + ot
else:
    print(name, "worked Regulartime!")
    fullsalary = salaryi * houri

print('Total Salary is', fullsalary)