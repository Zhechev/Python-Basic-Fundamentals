import math


def get_average(list_sizes):
    sum_size = sum(list_sizes)
    len_list_size = len(list_sizes)
    result = math.ceil(sum_size - (sum_size / len_list_size))

    return result


result = {}

while True:
    input_row = input()

    if input_row == 'Aggregate':
        break

    input_row = input_row.split(' ')
    region_name = input_row[0]
    region_size = int(input_row[1])

    if region_name in result:
        result[region_name].append(region_size)
    else:
        result[region_name] = []
        result[region_name].append(region_size)


for region in result:
    unique_region_sizes = sorted(set(result[region]), key=result[region].index)
    print(f"{region} -> {', '.join(list(map(str, unique_region_sizes)))} ({get_average(unique_region_sizes)})")



# import math
# result = {}
# biggest_elem = {}
#
# while True:
#     input_row = input()
#
#     if input_row == 'Aggregate':
#         break
#
#     input_row = input_row.split(' ')
#     region_name = input_row[0]
#     region_size = input_row[1]
#
#     if region_name in result:
#         if int(region_size) > int(biggest_elem[region_name]):
#             biggest_elem[region_name] = int(region_size)
#             result[region_name]['items'].append(region_size)
#             result[region_name]['count'] += 1
#             result[region_name]['sum'] += int(region_size)
#     else:
#         result[region_name] = {'count': 1, 'sum': int(region_size), 'items': [region_size]}
#         biggest_elem[region_name] = region_size
#
# for key, value in result.items():
#     items = ', '.join(value["items"])
#     sum = math.ceil(value['sum'] - (value['sum'] / value['count']))
#     print(f'{key} -> {items} ({sum})')
