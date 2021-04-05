#declaring and formatting variable as float
salary = float(input('Enter the salary: '))
#desclaring 'new salary' as result of this operation.
newSalary = salary*1.15
#presenting formatted 'new salary'.
print('New salary, with a 15% increase: {:.2f} '.format(newSalary))