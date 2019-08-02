player_one_time = int(input())
player_two_time = int(input())
player_three_time = int(input())

time_in_seconds = player_one_time + player_two_time + player_three_time
minutes = int(time_in_seconds / 60)
seconds = time_in_seconds - minutes * 60

result = str(minutes) + ':' + (str(seconds) if seconds >= 10 else '0' + str(seconds))
print(result)
