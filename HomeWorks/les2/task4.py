user_text = input('Введите несколько строк: ')
our_text = user_text.split()

for num, unit in enumerate(our_text, 1):
    print(num, unit[:10], end='\n')