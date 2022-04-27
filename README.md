## How much coffee

# Description
Everybody know that you passed to much time awake during night time...
Your task here is to define how much coffee you need to stay awake after your night. You will have to complete a function that takes an array of events in arguments, according to this list you will return the number of coffee you need to stay awake during the day time. Note: If the count exceed 3 please return 'You need extra sleep'.

# Test cases
test.assert_equals(how_much_coffee([]), 0)
test.assert_equals(how_much_coffee(['cw']), 1)
test.assert_equals(how_much_coffee(['CW']), 2)
test.assert_equals(how_much_coffee(['cw','CAT']), 3)
test.assert_equals(how_much_coffee(['cw','CAT','DOG']), 'You need extra sleep')
test.assert_equals(how_much_coffee(['cw','CAT', 'cw=others'])
