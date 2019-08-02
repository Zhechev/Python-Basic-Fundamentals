num = float(input())
input_unit_type = str(input())
output_unit_type = str(input())
result = 0

if input_unit_type == 'mm':
    num /= 1000
elif input_unit_type == 'cm':
    num /= 100
elif input_unit_type == 'mi':
    num /= 0.000621371192
elif input_unit_type == 'in':
    num /= 39.3700787
elif input_unit_type == 'km':
    num /= 0.001
elif input_unit_type == 'ft':
    num /= 3.2808399
elif input_unit_type == 'yd':
    num /= 1.0936133

if output_unit_type == 'mm':
    num *= 1000
elif output_unit_type == 'cm':
    num *= 100
elif output_unit_type == 'mi':
    num *= 0.000621371192
elif output_unit_type == 'in':
    num *= 39.3700787
elif output_unit_type == 'km':
    num *= 0.001
elif output_unit_type == 'ft':
    num *= 3.2808399
elif output_unit_type == 'yd':
    num *= 1.0936133

print(f'{num:.3f}')
