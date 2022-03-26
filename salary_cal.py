print("""***Hi, Welcome!***
        ***The program starts***""")

name = input('Enter Name: \n')
hour = input('Enter Hours: \n')
salary = input ('Enter Salary: \n')

try:
    houri = int(hour)
    salaryi = int(salary)

except:
    print('Hi', name, 'Your entered value is wrong')
    print('&&&&please enter a numeric valuve&&&&')


if houri > 40:
    print(name,'Worked Overtime!')
    netsalary = salaryi * houri
    ot = (houri - 40) * (salaryi * 1.5)
    fullsalary = netsalary + ot
else:
    print(name, "worked Regulartime!")
    fullsalary = salaryi * houri


#Adding the market currency value
rs = 'USD'
print('Total Salary is', fullsalary,rs)