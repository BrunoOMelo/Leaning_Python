from random import shuffle
n1 = str(input('Fist name: '))
n2 = str(input('Second name: '))
n3 = str(input('Third name: '))
n4 = str(input('Fourth name: '))
lista = [n1,n2,n3,n4]
shuffle(lista)
print(lista)
