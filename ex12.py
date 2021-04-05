#declaring and formatting variable as float.
value = float(input('Enter the product value: '))
#declaring 'new value' as result of this operation.
newValue = value - (value * 0.05)
#presenting the new value.
print('This product with 5% off: {:.2f}'.format(newValue))