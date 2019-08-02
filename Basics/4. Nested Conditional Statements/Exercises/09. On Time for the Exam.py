import math

hour_exam = int(input())
minute_exam = int(input())
hour_of_arrival = int(input())
minute_of_arrival = int(input())

exam_time = (hour_exam * 60) + minute_exam
arrival_time = (hour_of_arrival * 60) + minute_of_arrival

if arrival_time > exam_time:
    time_late = arrival_time - exam_time

    print('Late')
    if time_late >= 60:
        hours_late = time_late / 60
        minutes_late = int(time_late % 60)

        print(f'{math.floor(hours_late)}:{minutes_late if minutes_late >= 10 else str(minutes_late) + "0"} hours after the start')
    elif time_late <= 59:
        print(f'{time_late} minutes after the start')

elif arrival_time < exam_time:
    time_early = exam_time - arrival_time

    if 30 < time_early < 60:
        minutes_early = int(time_early % 60)

        print('Early')
        print(f'{minutes_early} minutes before the start')
    elif 30 < time_early >= 60:
        hours_early = time_early / 60
        minutes_early = int(time_early % 60)

        print('Early')
        print(f'{math.floor(hours_early)}:{minutes_early if minutes_early >= 10 else str(minutes_early) + "0"} hours before the start')
    elif time_early <= 30:
        print('On time')
        print(f'{time_early} minutes before the start')

elif arrival_time == exam_time:
    print("On time")

