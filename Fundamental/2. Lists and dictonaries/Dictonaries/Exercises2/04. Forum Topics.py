result = {}

while True:
    input_row = input()

    if input_row == 'filter':
        filter_tags = input().split(', ')

        for post, tags in result.items():
            flag = all(elem in tags for elem in filter_tags)

            if flag:
                print(f"{post} | #{', #'.join(tags)}")

        break

    input_parts = input_row.split(' -> ')
    topic = input_parts[0]
    tags = input_parts[1].split(', ')

    if topic not in result:
        result[topic] = tags
    else:
        for tag in tags:
            if tag not in result[topic]:
                result[topic].append(tag)