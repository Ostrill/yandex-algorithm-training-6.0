# Данные для чтения методом input()
input_data = iter([])


# Метод для установки значения строки для чтения
def set_input(text, skip_empty=True):
    global input_data, input_mode
    if not hasattr(text, '__next__'):
        if skip_empty:
            input_data = (line for line in str(text).split('\n') if line)
        else:
            input_data = (line for line in str(text).split('\n'))
    input_mode = 'str'


# Метод для чтения с клавиатуры, то есть стандартный input()
input_from_keyboard = input


# Метод для чтения из строки input_data
def input_from_string(*args, **kwargs):
    global input_data, input_mode
    try: 
        return next(input_data)
    except StopIteration:
        input_mode = 'kbd'
        return input(*args, **kwargs)


# Режим работы метода input() по умолчанию
input_mode = 'kbd'


# Метод input(), читающий с клавиатуры или строки
def input(*args, **kwargs):
    global input_mode
    if input_mode == 'str':
        return input_from_string(*args, **kwargs)
    else:
        return input_from_keyboard(*args, **kwargs)


# Ручное переключение режимов работы метода input()
def toggle_input_mode():
    global input_mode
    if input_mode == 'str':
        input_mode = 'kbd'
        print('Сейчас input() читает с клавиатуры')
    else:
        input_mode = 'str'
        print('Сейчас input() читает из строки input_data')


# Метод для установки содержимого input.txt
def set_file(text, skip_empty=True):
    with open('input.txt', 'w') as file:
        if skip_empty:
            text = '\n'.join(line for line in text.split('\n') if line)
        file.write(text)
