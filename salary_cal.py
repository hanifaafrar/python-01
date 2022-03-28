print("""***Hi, Welcome!***
        ***The program starts***""")

def cal(rate, time):
    print('Your worked salary and hours are:', rate , time)

name = input('Enter Name: \n')
try:
    hour = int(input('Enter Hours: \n'))
    salary = int(input('Enter Salary: \n'))

except:
    print('Hi', name, 'Your entered value is wrong')
    print('&&&& please enter a numeric value &&&&')

cal(salary, hour)

if hour > 40:
    print(name,'Worked Overtime!')
    netsalary = salary * hour
    ot = (hour - 40) * (salary * 1.5)
    fullsalary = netsalary + ot
else:
    print(name, "worked Regulartime!")
    fullsalary = salary * hour



#Adding the market currency value
rs = 'USD'
print('Total Salary is', fullsalary,rs)