import random

class LuhnAlgorithm:

    def __init__(self):
        self.account_number = 0
        self.card_bin = '400000'
        self.card_string = None
        self.card_list = []

    def create_card_number(self):
        is_valid = False
        while is_valid ==False:
            self.card_string = self.generate_card_number()
            is_valid = self.number_validator()
        return self.card_number

    def generate_card_number(self):
        self.card_list = []
        self.account_number = int(random.randint(111111111, 999999999))
        self.card_number = self.card_bin + str(self.account_number) + '3'
        return self.card_number

    def number_validator(self):
        self.card_string = str(self.card_number)
        print(self.card_string[0])
        check_sum = 0
        count = 0
        """for i in str(self.card_string):
            self.card_list.append(self.card_string[i])
        for c in self.card_list:
            # print(check_sum)
            count +=1
            print('count: {} '.format(count))
            print('c: {} '.format(int(c)))
            print(('checksum: {}'.format(check_sum)))

            if count % 2 == 0:
                check_sum += int(c)
                #  check_sum += (2 * int(c) % 9)
            else:
                # check_sum += int(c)
                check_sum += (2 * int(c) % 9)
                #print('double: {} '.format(2 * int(c) % 9))
            #  print('checksum: {}'.format(check_sum))

        print(self.card_string[6:15])
        if check_sum % 10 == 0:
            print('correct checksum: {}'.format(check_sum))
            return True
        else:
           return False"""




new_luhn = LuhnAlgorithm()

print(new_luhn.create_card_number())
# new_luhn.create_card_number()