import random

class CreditCard:

    def __init__(self):
        self.card_number = '0'
        self.pin_number = 0
        self.card_bin = '453217'
        self.account_number = '0'


    def generating_number(self):
        self.account_number = int(random.randint(111111111, 999999999))
        self.card_number = self.card_bin + str(self.account_number) + '1'

    def get_number(self):
        return self.card_number

    def generate_pin(self):
        random_int = int(random.randint(1111, 9999))
        self.pin_number = random_int

    def get_pin(self):
        return self.pin_number

