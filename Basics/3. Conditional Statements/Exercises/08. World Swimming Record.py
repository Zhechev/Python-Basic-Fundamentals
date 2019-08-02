record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_swimming_one_meter = float(input())

time_needed = distance_in_meters * time_in_seconds_swimming_one_meter
time_needed += round((int((distance_in_meters / 15)) * 12.5), 2)


if time_needed >= record_in_seconds:
    result = time_needed - record_in_seconds
    print(f'No, he failed! He was {result:.2f} seconds slower.')
else:
    print(f'Yes, he succeeded! The new world record is {time_needed:.2f} seconds.')
