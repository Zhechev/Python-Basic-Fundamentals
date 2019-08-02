string = input()
unique_chars = {}

for i in range(0, len(string)):
    if string[i] not in unique_chars:
        unique_chars[string[i]] = {i}
    else:
        unique_chars[string[i]].add(i)

for char, indexes in unique_chars.items():
    print(f"{char}:{'/'.join(map(str, sorted(indexes)))}")
