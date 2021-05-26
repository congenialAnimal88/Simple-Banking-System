import random

account_details = dict()
user_input = None
new_card = None
main_menu_selected = True

card_number = '0'
pin_number = 0
card_bin = '400000'
account_number = '0'

def create_card():
    generating_number()
    generate_pin()
    account_details[get_number()] = get_pin()
    print('Your card number:\n{}\nYour card PIN: \n{}\n'.format(int(get_number()), get_pin()))
    main_menu()


def log_in_to_account( account_number, pin_number ):
    try:
        print(account_details[account_number])
        details_match = (int(account_details[account_number]) == int(pin_number))
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


def logged_out():
    print('You have successfully logged out!')
    print('')
    main_menu()

def generating_number():
    account_number = int(random.randint(111111111, 999999999))
    global card_number
    card_number = card_bin + str(account_number) + '1'

def get_number():
    return card_number

def generate_pin():
    global pin_number
    random_int = int(random.randint(1111, 9999))
    pin_number = random_int

def get_pin():
    return pin_number

# control loop for initial input
# cat cafes project for examples
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