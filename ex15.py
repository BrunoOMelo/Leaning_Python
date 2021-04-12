#declaring variable as string
name = str(input('Enter your name: '))
#saving the split string 
splitName = name.split()
#changing all letters to uppercase
print('Uppercase: ',name.upper())
#changing all latters to lowercase
print('Lowercase: ',name.lower())
#counting the amount of letters
print('Amount of letters: ',len(name.replace(' ', '')))
#counting the amount of letters in first name
print('Number os letter in first name: ',len(splitName[0]))