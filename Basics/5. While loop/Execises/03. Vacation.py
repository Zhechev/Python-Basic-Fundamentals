money_for_vacation = float(input())
money_on_hand = float(input())
days_spend_counter = 0
days_counter = 0

while days_spend_counter < 5:
    type_action = input()
    money = float(input())
    if type_action == 'spend':
        days_spend_counter += 1
        days_counter += 1

        if days_spend_counter == 5:
            print('You can\'t save the money.')
            print(days_counter)
            exit()

        if money >= money_on_hand:
            money_on_hand = 0
        else:
            money_on_hand -= money
    else:
        days_spend_counter = 0
        money_on_hand += money
        days_counter += 1
        if money_on_hand >= money_for_vacation:
            print(f'You saved the money for {days_counter} days.')
            break
