#declaring and formatting variable as float.
meter = float(input('Enter the value in meters: '))
centimeter = meter*100
milimeter = meter*1000
#presenting the result
print('Converted in centimeter: {:.2f}' .format(centimeter))
print('Converted in milimeter: {:.2f}' .format(milimeter))