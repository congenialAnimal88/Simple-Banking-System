currently_logged_in = None

transfer_to = None
transfer_amount = None
possible_accounts = []


def do_transfer(self):

    current_balance = 0
    new_acc_balance = 0
    transfer_to = input("Transfer \n Enter card number: \n >")



    if transfer_to == currently_logged_in:
        print("Probably you made a mistake in the card number.  Please try again!")
    for acc in possible_accounts:
        if transfer_to == possible_accounts[acc]:
            transfer_amount = int(input(("Enter how much money you want to transfer: \n >")))
            if current_balance - transfer_amount > current_balance:
                print("Not enough money!")
            else:
                current_balance -= transfer_amount
                new_acc_balance += transfer_amount
                print("Success!")
        else:
            print("Such a card does not exist.")

def do_transfer_2(self):
    current_balance = 0
    new_acc_balance = 0
    transfer_to = input("Transfer \n Enter card number: \n >")
    # Luhn check first
    if not luhnCheck(transfer_to):
        print("Probably you made a mistake in the card number.  Please try again!")
    elif transfer_to == currently_logged_in:
        print("You can't transfer money to the same account!")
    elif not account_exists(transfer_to):
        print("Such a card does not exist.")
    else:
        transfer_amount = int(input(("Enter how much money you want to transfer: \n >")))
        if current_balance - transfer_amount > current_balance:
            print("Not enough money!")
        else:
            current_balance -= transfer_amount
            new_acc_balance += transfer_amount
            print("Success!")

def account_exists(self, account_number):
    for acc in possible_accounts:
        if account_number == possible_accounts[acc]:
            return True
        else:
            return False

def luhnCheck(self,account_number):
    number_string = list(account_number)
    # print(number_string)
    number_string = [int(i) for i in number_string]
    list_total = 0
    for i, res in enumerate(number_string):
        if i % 2 == 0:
            a = 2*res
            if a > 9:
                a -=9
        else:
            a = res
        list_total += a
    # print(list_total)
    if list_total % 10 == 0:
        print("passed Luhn")
        return True
    else:
        return False
    print("failed Luhn")
