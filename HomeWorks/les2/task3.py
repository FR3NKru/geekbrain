user_number = int(input('Введите целое число от 1 до 12: '))
month_list = ['Winter', 'Spring', 'Summer', 'Autumn']
if user_number > 0 and user_number < 3 or user_number == 12:
    print(month_list[0])
elif user_number >2 and user_number < 6:
    print(month_list[1])
elif user_number >6 and user_number < 9:
    print(month_list[2])
else:
    print(month_list[3])
month_dict = {
    1: 'Winter',2: 'Winter',12: 'Winter',
    3: 'Spring',4: 'Spring',5: 'Spring',
    6: 'Summer',7: 'Summer',8: 'Summer',
    9: 'Autumn',10: 'Autumn',11: 'Autumn'
}
user_number2 = int(input('Введите целое число от 1 до 12: '))
print(month_dict.get(user_number2))