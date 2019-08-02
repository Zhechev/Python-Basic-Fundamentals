month = input()
num_nights = int(input())

if month == 'May' or month == 'October':
    studio_price_night = 50
    apartament_price_night = 65
    if num_nights > 14:
        studio_price_night -= studio_price_night * 0.30
        apartament_price_night -= apartament_price_night * 0.10
    elif num_nights > 7:
        studio_price_night -= studio_price_night * 0.05
    studio_price = studio_price_night * num_nights
    apartament_price = apartament_price_night * num_nights
elif month == 'June' or month == 'September':
    studio_price_night = 75.20
    apartament_price_night = 68.70

    if num_nights > 14:
        studio_price_night -= studio_price_night * 0.20
        apartament_price_night -= apartament_price_night * 0.10
    studio_price = studio_price_night * num_nights
    apartament_price = apartament_price_night * num_nights
else:
    apartament_price_night = 77
    if num_nights > 14:
        apartament_price_night -= apartament_price_night * 0.10
    studio_price = num_nights * 76
    apartament_price = apartament_price_night * num_nights


print(f'Apartment: {apartament_price:.2f} lv.')
print(f'Studio: {studio_price:.2f} lv.')
