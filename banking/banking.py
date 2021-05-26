import random
import sqlite3


class SimpleBankingSystemV2:

    def __init__(self):
        self.pin_number = 0
        self.account_number = None
        self.account_balance = 0
        self.card_db = None
        self.currently_logged_in = ""
        self.card_db_id = 1
        self.possible_accounts = []
        self.conn = sqlite3.connect('card.s3db')
        self.cur = self.conn.cursor()
        self.initiate_db_connection()
        self.user_interface()


    def initiate_db_connection(self):
        self.cur.execute('CREATE TABLE IF NOT EXISTS card (id INTEGER, number TEXT, pin TEXT, balance INTEGER)')
        self.conn.commit()

    def insert_record(self, id, account_number, pin_number, account_balance):
        sql_string = "INSERT INTO card VALUES ({}, {}, {}, {})".format(id, account_number,pin_number, account_balance)
        self.cur.execute(sql_string)
        self.conn.commit()

    def user_interface(self):
        while True:
            user_input = int(input("1. Create an account\n"
                                   "2. Log into acount\n"
                                   "0. Exit\n"
                                   ">>"))
            if user_input == 0:
                print("You have successfully logged out!")
                exit()
            elif user_input == 1:
                self.create_account()
            elif user_input == 2:
                self.log_in()

    def create_account(self):

        self.generate_number()
        self.account_balance = 0

        print("Your card has been created")
        print("Your card number:")
        print(self.account_number)
        print("Your card PIN:")
        print(self.pin_number)

    def log_in(self):

        user_login_acc = input("Enter your card number: \n >")
        user_login_PIN = input("Enter your PIN number: \n >")

        if user_login_acc == self.account_number \
                and user_login_PIN == str(self.pin_number):
            print("You have successfully logged in!")
            self.currently_logged_in = user_login_acc
            self.manage_account()
        else:
            print("Wrong card number or PIN!")

    def manage_account(self):

        while True:
            acc_management = int(input("1. Balance \n"
                                        "2. Add Income \n"
                                        "3. Do transfer\n"
                                        "4. Close account\n"
                                        "5.Log out \n"
                                        "0. Exit \n >"))
            if acc_management == 0:
                print("You have successfully logged out!")
                exit()
            elif acc_management == 1:
                self.show_balance()
            elif acc_management == 2:
                self.add_income()
            elif acc_management == 3:
                self.do_transfer()
            elif acc_management == 4:
                self.close_account()
            elif acc_management == 5:
                print("You have successfully logged out! \n")
                self.user_interface()

    def show_balance(self):
        print("Fetching Balance: {}".format(self.currently_logged_in))
        current_balance = 0
        balance_retrieval = """SELECT balance FROM card WHERE number = {}""".format(self.currently_logged_in)
        current_balance = self.cur.execute(balance_retrieval).fetchone()
        self.conn.commit()
        print(current_balance[0])

    def add_income(self):
        current_balance_retrieval = """SELECT balance from card WHERE number = {}""".format(self.currently_logged_in)
        current_balance_value = self.cur.execute(current_balance_retrieval).fetchone()
        self.conn.commit()

        current_balance = int(current_balance_value[0])
        income = int(input("Enter income: \n >"))
        new_balance = income + current_balance
        insertion_data = [(new_balance, self.currently_logged_in)]
        print(insertion_data)
        income_update_string = \
            "INSERT INTO card (balance) VALUES ({}) WHERE number = {}".format(income, self.currently_logged_in)

        print(income_update_string)
        #self.cur.execute("""UPDATE card SET balance = ? WHERE number = ?""")
        data_update_query = """UPDATE card SET balance = ? WHERE number = ?"""
        self.cur.executemany(data_update_query, insertion_data)
        self.conn.commit()
        print("Income was added!")

    def do_transfer(self):
        print(self.possible_accounts)
        transfer_from_account = []
        transfer_to_account = []
        balance_retrieval = """SELECT balance FROM card WHERE number = {}""".format(self.currently_logged_in)
        current_balance = self.cur.execute(balance_retrieval).fetchone()
        self.conn.commit()
        # print("current balance: {}".format(current_balance[0]))
        balance_from = int(current_balance[0])
        new_acc_balance = 0
        # print("Balance from: {}".format(balance_from))
        transfer_to = input("Transfer \n Enter card number: \n >")

        if not self.luhnCheck(transfer_to):
            print(transfer_to)
            print("Probably you made mistake in card number. Please try again!")

        elif transfer_to == self.currently_logged_in:
            print("You can't transfer money to the same account!")

        elif not self.account_exists(transfer_to):
            print("Such a card does not exist.")

        else:
            transfer_amount = int(input(("Enter how much money you want to transfer: \n >")))
            if transfer_amount > balance_from:
                print("Not enough money!")
            else:
                balance_from -= transfer_amount
                transfer_from_account = [(balance_from, self.currently_logged_in)]
                new_acc_balance += transfer_amount
                transfer_to_account = [(new_acc_balance, transfer_to)]
                print("Success!")
                # print(transfer_from_account)
                # print(transfer_to_account)
                transfer_from_update_query = """UPDATE card SET balance = ? WHERE number = ?"""
                self.cur.executemany(transfer_from_update_query, transfer_from_account)
                self.conn.commit()
                transfer_to_update_query = """UPDATE card SET balance = ? WHERE number = ?"""
                self.cur.executemany(transfer_to_update_query, transfer_to_account)
                self.conn.commit()


    def close_account(self):
        account_string = """ DELETE from card WHERE number = {}""".format(self.currently_logged_in)
        self.cur.execute(account_string)
        print("The account has been closed!")
        self.user_interface()


    def generate_number(self):
        current_card_account = []
        bank_string = "400000"
        distinct_segment = random.randint(111111111, 999999999)
        temp_account_number = bank_string + str(distinct_segment)
        number_string = list(temp_account_number)
        number_string = [int(i) for i in number_string]
        list_total = 0
        a = 0
        for i, res in enumerate(number_string):
            if i % 2 == 0:
                a = 2*res
                if a > 9:
                    a -=9
            else:
                a = res
            list_total += a

        if list_total % 10 == 0:
            check_sum_digit = 0
        else:
            check_sum_digit = 10 - (list_total % 10)

        self.account_number = temp_account_number + str(check_sum_digit)
        self.pin_number = random.randint(1111, 9999)
        current_card_account.append(self.card_db_id)
        current_card_account.append(self.account_number)
        current_card_account.append(self.pin_number)
        current_card_account.append(self.account_balance)
        self.possible_accounts.append(self.account_number)
        self.card_db_id += 1
        self.insert_record(current_card_account[0], current_card_account[1], current_card_account[2], current_card_account[3])
        # print(self.possible_accounts)

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
            #print("passed Luhn")
            return True
        else:
            return False
            #print("failed Luhn")

    def account_exists(self, account_number):
        if account_number in self.possible_accounts:
            return True
        else:
            return False

bank1 = SimpleBankingSystemV2()
