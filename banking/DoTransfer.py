def do_transfer(self):
    print(self.possible_accounts)
    transfer_from_account = []
    transfer_to_account = []
    balance_retrieval = """SELECT balance FROM card WHERE number = {}""".format(self.currently_logged_in)
    current_balance = self.cur.execute(balance_retrieval).fetchone()
    self.conn.commit()
    # print("current balance: {}".format(current_balance[0]))
    balance_from = int(current_balance[0])
    # print("Balance from: {}".format(balance_from))
    new_acc_balance = 0
    transfer_to = input("Transfer \n Enter card number: \n >")

    if self.luhnCheck(transfer_to):
        if transfer_to in self.possible_accounts:
            if transfer_to == self.currently_logged_in:
                print("You can't transfer money to the same account!")
            else:
                transfer_amount = int(input(("Enter how much money do you want to transfer: \n >")))
                if transfer_amount > balance_from:
                    print("Not enough money!")
                else:
                    balance_from -= transfer_amount
                    transfer_from_account = [(self.currently_logged_in, balance_from)]
                    new_acc_balance += transfer_amount
                    transfer_to_account = [(transfer_to, new_acc_balance)]
                    print("Success!")
                    # print(transfer_from_account)
                    # print(transfer_to_account)
                    transfer_from_update_query = """UPDATE card SET balance = ? WHERE number = ?"""
                    self.cur.executemany(transfer_from_update_query, transfer_from_account)
                    self.conn.commit()
                    transfer_to_update_query = """UPDATE card SET balance = ? WHERE number = ?"""
                    self.cur.executemany(transfer_to_update_query, transfer_to_account)
                    self.conn.commit()
        else:
            print("Such a card does not exist.")
    else:
        print("Probably you made a mistake in the card number. Please try again!")