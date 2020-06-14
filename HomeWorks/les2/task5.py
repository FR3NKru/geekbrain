user_number = int(input('Введите номер вашего рейтинга: '))
my_list = [10, 8, 7, 7, 5, 4, 2, 1]
num = 0
while True:
    if user_number >= my_list[num]:
        my_list.insert(num, user_number)
        break
    num += 1

print(my_list)
