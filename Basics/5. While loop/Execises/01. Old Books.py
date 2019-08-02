searched_book = input()
num_books = int(input())

count_checked_books = 0

while num_books > 0:
    book = input()
    if book == searched_book:
        print(f'You checked {count_checked_books} books and found it.')
        exit()
    count_checked_books += 1
    num_books -= 1

print('The book you search is not here!')
print(f'You checked {count_checked_books} books.')
