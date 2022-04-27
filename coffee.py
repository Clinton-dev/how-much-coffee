def how_much_coffee(events):
    counter = 0

    for event in events:
        if event == 'cw':
            counter += 1
        elif event == 'CW':
            counter += 2
        elif event == 'cat':
            counter += 1
        elif event == 'CAT':
            counter += 2
        elif event == 'dog':
            counter += 1
        elif event == 'DOG':
            counter += 2
        elif event == 'movie':
            counter += 1
        else:
            counter += 0

    if counter > 3:
        print("You need extra sleep!!!")
    else:
        print(f'Drink {counter} cups of coffee')


how_much_coffee([])# return 0
how_much_coffee(['cw'])# return 1 cups
how_much_coffee(['CW'])# return 2 cups
how_much_coffee(['cw','CAT'])# return 3 cups
how_much_coffee(['cw','CAT','DOG'])# return you need sleep