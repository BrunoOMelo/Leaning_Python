#importing only one funciotion from library 
from random import shuffle
#declaring variables as string
n1 = str(input('Fist name: '))
n2 = str(input('Second name: '))
n3 = str(input('Third name: '))
n4 = str(input('Fourth name: '))
#creating a list with this variables
lista = [n1,n2,n3,n4]
#using 'shufle' for change the order of list
shuffle(lista)
print(lista)
