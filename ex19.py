#declaring variable as string
name = str(input('Enter your name: '))
#saving the split name
splitName = name.split()
#presenting the first name
print('First name: ',splitName[0])
#presenting the last name
print('Last name: ',splitName[-1])