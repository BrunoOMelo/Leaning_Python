##declaring and formatting variable as float.
height = float(input('Type the height of the wall: '))
width = float(input('Type the width of the wall:'))
area = height*width
#presenting the amount of liter needed
print('Amount of liters of paint needed to paint the wall (talking into account that one liter yields 2 square meters): {:.2f}' .format(area/2))
