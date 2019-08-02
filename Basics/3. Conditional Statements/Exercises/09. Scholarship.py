import math

income_in_leva = float(input())
average_success = float(input())
mrz = float(input())
social_scholarship = 0.0
scholarship_for_excellent_results = 0.0

if income_in_leva < mrz and average_success >= 4.50:
    social_scholarship = float(0.35 * mrz)
if average_success >= 5.50:
    scholarship_for_excellent_results = float(25 * average_success)

if social_scholarship != 0.0 or scholarship_for_excellent_results != 0.0:
    if social_scholarship >= scholarship_for_excellent_results:
        print(f'You get a Social scholarship {math.ceil(social_scholarship)} BGN')
    else:
        print(f'You get a scholarship for excellent results {math.ceil(scholarship_for_excellent_results)} BGN')
else:
    print('You cannot get a scholarship!')
