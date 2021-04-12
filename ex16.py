#declaring variable as string
city = str(input('Enter the name of your city: '))
#saving the split number 
splitCity = city.split()
#checking if "Santo" exists in the first name
print('Does your city name start with "Santo"? : ',('Santo') in splitCity[0].title())