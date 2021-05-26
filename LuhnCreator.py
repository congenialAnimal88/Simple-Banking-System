import random

class LuhnCreator:

    def __init__(self):
        self.bin_string = "400000"
        self.card_string = None
        self.card_list = []
        self.createNumber()


    def createNumber(self):
        account_number = int(random.randint(100000000, 999999999))
        self.card_string = self.bin_string + str(account_number)
        self.card_list = list(self.card_string)
        self.card_list.append(self.checkNumber(self.card_list))


    def checkNumber(self, card_number):
        # print(len(card_number))
        digit_sum = 0
        for count, digit in enumerate(card_number):
            current_digit = int(digit)

            if count % 2 == 0:
                current_digit *= 2
                if current_digit > 9:
                    current_digit -= 9
            #print("adding: {}".format(current_digit))
            digit_sum += current_digit
        print(digit_sum)
        print(digit_sum % 10)
        check_sum = 10 - digit_sum % 10
        print("CheckSum digit: {}".format(check_sum))
        return check_sum





new_Luhn = LuhnCreator()