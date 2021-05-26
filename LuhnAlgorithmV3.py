import random

card_list = []
card_string = ''



def generating_number():
    valid_number = ''
    is_valid = False
    while is_valid == False:
        account_number = int(random.randint(111111111, 999999999))
        card_number = '400000' + str(account_number) + '3'
        is_valid = number_validator(str(card_number))
        #card_number = 4000009962825453
        #is_valid = number_validator(str(card_number))
    return card_number

def number_validator(number):
    check_sum = 0
    count = len(number)
    # print(len(number))
    for i in range(0, count, 1):
        # print('digit {} {}:'.format( i, number[i]))
        if i % 2 == 0:
            current = 2 * int(number[i])
            if current > 9:
                current = current - 9
            check_sum += current
        else:
            check_sum += int(number[i])
        # print('check_sum: {}'. format(check_sum))

    if check_sum % 10 == 0:
        print('valid')
        # return True
    else:
        print('invalid')
        # return False

card_string = generating_number()
print(card_string)

"""while count > 0:
        if count % 2 == 1:
            check_sum += ( 2 * int(number[count - 1])) % 9
        else:
            check_sum += int(number[count - 1])
        count -= 1
    print('check_sum: {}'. format(check_sum))
    print('Mod 10: {}'.format(check_sum % 10))"""