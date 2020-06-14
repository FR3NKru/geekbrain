user_list = []
list_range = int(input('Введите количестно элементов списка: '))
i = 0
while i < list_range:
    user_list.append(input(f'Введите {i+1} элемент списка: '))
    i += 1
our_list = []
q = 0
while q+1 < len(user_list):
    if len(user_list) % 2 == 0:
        our_list.append(user_list[q+1])
        our_list.append(user_list[q])
        q += 2
    else:
        our_list.append(user_list[q + 1])
        our_list.append(user_list[q])
        q += 2
        if q+2 > len(user_list):
            our_list.append(user_list[-1])
print(our_list)
