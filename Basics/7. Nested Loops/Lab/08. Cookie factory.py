batches_num = int(input())

bakes = 1
flour_flag = False
eggs_flag = False
sugar_flag = False

while bakes <= batches_num:
    while True:
        component = input()

        if component == 'Bake!':
            if flour_flag and eggs_flag and sugar_flag:
                print(f'Baking batch number {bakes}...')
                bakes += 1
                flour_flag = False
                eggs_flag = False
                sugar_flag = False
                break
            else:
                print('The batter should contain flour, eggs and sugar!')

        if component == 'flour':
            flour_flag = True
        elif component == 'eggs':
            eggs_flag = True
        elif component == 'sugar':
            sugar_flag = True
