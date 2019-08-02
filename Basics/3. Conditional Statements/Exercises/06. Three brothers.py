import math
time_first_brother_alone = float(input())
time_second_brother_alone = float(input())
time_third_brother_alone = float(input())
dad_fishing_time = float(input())

common_time = 1 / ((1/time_first_brother_alone) + (1/time_second_brother_alone) + (1/time_third_brother_alone))
common_time_with_brake = common_time * 1.15

print(f'Cleaning time: {common_time_with_brake:.2f}')

if dad_fishing_time > common_time_with_brake:
    time_left = math.floor(dad_fishing_time - common_time_with_brake)
    print(f'Yes, there is a surprise - time left -> {time_left} hours.')
else:
    not_enough_time = math.ceil(common_time_with_brake - dad_fishing_time)
    print(f'No, there isn\'t a surprise - shortage of time -> {not_enough_time} hours.')
