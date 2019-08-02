destination = input()

while destination != 'End':
    min_budget = float(input())
    if min_budget == 0:
        print(f'Going to {destination}')
        break
    all_saved_money = 0
    while True:
        saved_money = float(input())
        all_saved_money += saved_money

        if all_saved_money >= min_budget:
            print(f'Going to {destination}!')
            break

    destination = input()
