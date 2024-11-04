# $\color{#EA5032}\text{🅨}$ Тренировки по алгоритмам 6.0

Здесь собраны решения всех всех домашних заданий с тренировок 6.0. Задачи сделаны на питоне, поэтому для удобства хранятся в виде ноутбуков. 

Для упрощения ввода используется кастомная функция `input()`, реализованная в модуле [utils/string_input.py](utils/string_input.py).

<details>
<summary>&nbsp;Подробнее про <code>input()</code></summary>
<blockquote></blockquote>
<blockquote>
    
Неудобно каждый раз вводить данные для тестов вручную с клавиатуры, особенно если они состоят из кучи длинных строк. Читать из файла тоже неудобно, потому что для этого надо в отдельном окне/вкладке держать еще и этот файл, нажимая <kbd>ctrl+s</kbd> каждый раз, когда в нем что-то поменяется.

Поэтому и был реализован кастомный `input()`. Он работает точно так же, как и встроенный, но читает не из стандартного ввода с клавиатуры, а из специальной строковой переменной. Соответственно, прежде чем считывать оттуда, необходимо записать в эту строковую переменную нужные строки с помощью `set_input()`. Например:
```Python
# Пишем сюда входные данные
set_input("""
5
1 2 3 4 5
""")

# Считываем их, как будто их вводят с клавиатуры
n = int(input())
array = list(map(int, input().split()))
```

В итоге можно через `set_input()` вставлять любые входные данные, а потом считывать их с помощью `input()`, как будто они вводятся с клавиатуры.

С помощью вызова функции `toggle_input_mode()` можно переключать режим работы функции `input()` (чтение с клавиатуры или чтение из строки).

P.S. Можно было сделать это и через перенаправление потока ввода, но в Jupyter ввод устроен иначе, и это так просто не сработает.

</blockquote>
</details>

## Навигация по задачам

<a href="homework_1.ipynb#B"><img src="images/1A.jpg"/></a>