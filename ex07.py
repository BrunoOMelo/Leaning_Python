#declaring and formatting multiples variables as float.
n1 = float(input('Type the first note: '))
n2 = float(input('Type the second note: '))
#declaring "m" as average between "n1" an "n2".
m = (n1 + n2)/2
#formatting the output for the user.
print('Your average: {:.2f}' .format(m))
#declaring parameters for the output.
if(m >= 6):
    print('You were approved!')
elif(m == 5):
    print('You are recovery.')
else:
    print('You were not approved')

