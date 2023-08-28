my_nime = input ("whatyour name?")
my_age =int(input('wath is your age?'))
print(f'my name is {my_nime}and i am{my_age}years old')

first_number = int(input('enter the first number:'))
second_number =int(input('enterthe secound number:'))

operation = input('enter the mathmatical operation:')

if operation=='+':
    print(first_number+second_number)
elif operation=='_':
    print(first_number-second_number)
elif operation=='*':
    print(first_number*second_number)
elif operation=='/':
    print(first_number/second_number)
else:
    print('the operation is not valid')

bus_capacity =30
inside_the_bus = int(input('how many people are on the bus?'))
outside_the_bus = int(input('how many people are outside the bus?'))
empty_seats =bus_capacity - inside_the_bus

if empty_seats>outside_the_bus:
    print('there are seats on the bus')
else:
    print('the bus is full')
