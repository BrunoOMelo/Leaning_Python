#declaring variable as string
phrase = str(input('Type a phrase: '))
#saving the phrase in lowercase
phrase = phrase.lower()
#presenting amount of lettters 'a' 
print('Amount of letters "a": ', phrase.count('a'))
#presenting the position of firt 'a'
print('Firt "A" in position: ', phrase.find('a'))
#presenting the position of last 'a' whith 'right find'
print('Last "A" in postion: ',phrase.rfind('a'))