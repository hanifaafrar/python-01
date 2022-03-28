print("""***Hi, Welcome!***
        ***The program starts***""")

name = input('Enter Name: \n')
try:
    hour = int(input('Enter Hours: \n'))
    salary = int(input('Enter Salary: \n'))

except:
    print('Hi', name, 'Your entered value is wrong')
    print('&&&& please enter a numeric value &&&&')

def cal(time, rate):
    print('Your worked salary and hours are:', rate , time)
    if time > 40:
        print(name, 'Worked Overtime!')
        netsalary = rate * time
        ot = (time - 40) * (rate * 1.5)
        fullsalary = netsalary + ot
    else:
        print(name, "worked Regulartime!")
        fullsalary = rate * time
    return print('Total Salary is', fullsalary, ' USD')


cal(salary, hour)
