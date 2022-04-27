def how_much_coffee(events):
    cups_of_coffee = 0

    if len(events) == 0: return 0

    for event in events:
        if event == 'cw':
            cups_of_coffee += 1
        elif event == 'CW':
            cups_of_coffee += 2
        elif event == 'cat':
            cups_of_coffee += 1
        elif event == 'CAT':
            cups_of_coffee += 2
        elif event == 'dog':
            cups_of_coffee += 1
        elif event == 'DOG':
            cups_of_coffee += 2
        elif event == 'movie':
            cups_of_coffee += 1
        else:
            cups_of_coffee += 0

    if cups_of_coffee > 3:
        print("You need extra sleep!!!")
        return "You need extra sleep"
    else:
        print(f'Drink {cups_of_coffee} cups of coffee')
        return cups_of_coffee




how_much_coffee([])# return 0
how_much_coffee(['cw'])# return 1 cups
how_much_coffee(['CW'])# return 2 cups
how_much_coffee(['cw','CAT'])# return 3 cups
how_much_coffee(['cw','CAT','DOG'])# return you need sleep