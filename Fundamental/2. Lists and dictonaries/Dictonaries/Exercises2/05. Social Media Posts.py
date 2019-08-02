result = {}

while True:
    input_row = input()

    if input_row == 'drop the media':
        break

    input_parts = input_row.split(' ')
    command = input_parts[0]

    if command == 'post':
        post_name = input_parts[1]
        result[post_name] = {'likes': 0, 'dislikes': 0, 'comments': {}}
    elif command == 'like':
        post_name = input_parts[1]
        result[post_name]['likes'] += 1
    elif command == 'dislike':
        post_name = input_parts[1]
        result[post_name]['dislikes'] += 1
    elif command == 'comment':
        post_name = input_parts[1]
        commentar_name = input_parts[2]
        result[post_name]['comments'][commentar_name] = ' '.join(input_parts[3:])

for post, data in result.items():
    print(f"Post: {post} | Likes: {data['likes']} | Dislikes: {data['dislikes']}")
    print(f"Comments:")
    if not data['comments']:
        print(f"None")
    else:
        for author, comment in data['comments'].items():
            print(f"*  {author}: {comment}")
