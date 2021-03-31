#declaring and formatting variable as float.
real = float(input('Enter the amount of R$: '))
dolar = float(input('Enter the US$ price: '))
#presenting the conversion
print('R$ {:.2f} in US$: {:.2f}'.format(real,real/dolar))