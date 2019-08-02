import math
steps_num = int(input())
dancers_num = int(input())
days_for_studying = int(input())

steps_per_day_procent = math.ceil(((steps_num / days_for_studying) / steps_num) * 100)
procent_steps_per_dancer = steps_per_day_procent / dancers_num

if steps_per_day_procent <= 13:
    print(f'Yes, they will succeed in that goal! {procent_steps_per_dancer:.2f}%.')
else:
    print(f'No, they will not succeed in that goal! Required {procent_steps_per_dancer:.2f}% steps to be learned per day.')
