# Строка для чтения методом input()
input_data = ''


# Метод для установки значения строки для чтения
def set_input(text):
    global input_data
    input_data = text


# Метод для чтения с клавиатуры, то есть стандартный input()
input_from_keyboard = input


# Метод для чтения из строки input_data
def input_from_string(*args, **kwargs):
    global input_data
    if isinstance(input_data, str):
        input_data = [line for line in input_data.split('\n') if line]
        input_data = input_data.__iter__()
    return next(input_data)


# Текущий режим работы метода input()
input_mode = 'str'


# Метод input(), читающий с клавиатуры или строки
def input(*args, **kwargs):
    global input_mode
    if input_mode == 'str':
        return input_from_string(*args, **kwargs)
    else:
        return input_from_keyboard(*args, **kwargs)


# Переключение режимов работы метода input()
def toggle_input_mode():
    global input_mode
    if input_mode == 'str':
        input_mode = 'kbd'
        print('Сейчас input() читает с клавиатуры')
    else:
        input_mode = 'str'
        print('Сейчас input() читает из строки input_data')