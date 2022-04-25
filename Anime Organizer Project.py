
guesses = 0
limit = 5
while guesses < limit:
    response = input('''Enter an anime Character to find the corresponding anime: 
    Kurumi
    Shido
    Rias
    Zero Two
    Takeru
    ''')
    guesses += 1
    if response == 'Kurumi':
        print('Date a Live')
    elif response == 'Shido':
        print('Date a Live')
    elif response == 'Rias':
        print('High School DxD')
    elif response == 'Zero Two':
        print('Darling in the Franxx')
    elif response == 'Takeru':
        print('Maken-Ki')
    elif response != 'Kurumi' or 'Shido' or 'Rias' or 'Zero Two' or 'Takeru':
        print('Please enter a name of an character')
else:
    print('You have used all your turns.')




    










