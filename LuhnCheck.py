import random

account_details = dict()
user_input = None
new_card = None
main_menu_selected = True

global card_number
card_number= 0
pin_number = 0
card_bin = '400000'
account_number = '0'
global card_string
card_string = None
card_list = []

def create_card():
    current_number = create_card_number()
    generate_pin()
    account_details[current_number] = pin_number
    print('Your card number:\n{}\nYour card PIN: \n{}\n'.format(current_number, pin_number))

    main_menu()

def generate_pin():
    global pin_number
    random_int = int(random.randint(1111, 9999))
    pin_number = random_int

# code to control creation of card number
def create_card_number():
    card_string = generating_number()
    is_valid = False
    while is_valid == False:
        #print('Pre Gen: {}'.format(card_string))
        card_string = generating_number()
        #print('checking: {}'.format(card_string))
        is_valid = number_validator(card_string)
    card_number = int(card_string)
    return card_number

# generates number according to specification for checking
def generating_number():
    global card_list
    card_list= []
    account_number = int(random.randint(111111111, 999999999))
    card_number = card_bin + str(account_number) + '3'
    card_string = str(card_number)
    # print(card_number)
    return card_number

# checks number meets specification
def number_validator(number):
    #print('created: {}'.format(number))
    # print('card string created: {}'.format(card_string))
    card_string = str(number)
    #print('validating: {}'.format(card_string))
    check_sum = 7
    for i in range(7, 15):
        card_list.append(card_string[i])
    for c in card_list:
        if int(c) % 2 == 0:
            check_sum += (2 * int(c)) % 9
        else:
            check_sum += int(c)
    if check_sum % 10 == 0:
        return True
    else:
        return False

# evaluate user login attempts
def log_in_to_account( account_number, pin_number ):
    try:
        details_match = (account_details[int(account_number)]) == int(pin_number)
        if details_match:
            print('You have successfully logged in!')
            account_menu()
        else:
            print('')
            print('Wrong card number or PIN!')
            print('')
            main_menu()
    except KeyError:
        print('')
        print('Wrong card number or PIN!')
        print('')
        main_menu()

def logged_out():
    print('You have successfully logged out!')
    print('')
    main_menu()

#control menu selections
def main_menu():
    print('1. Create an ccount')
    print('2. Log into account')
    print('0. Exit')
    print('>')
    global main_menu_selected
    main_menu_selected = True

def account_menu():
    print('Balance: 0')
    print('')
    print('1. Balance')
    print('2. Log out')
    print('0. Exit')
    print('>')
    global main_menu_selected
    main_menu_selected = False

# run application
main_menu()

while True:
    user_input = int(input())
    if user_input == 0:
        print('Goodbye.')
        exit()
    elif user_input == 1:
        print('Your card has been created')
        create_card()
    elif user_input == 2:
        if main_menu_selected == False:
            logged_out()
        else:
            account_number = input('Enter your card number:>')
            pin_number = input('Enter your PIN:>')
            log_in_to_account( account_number, pin_number )




