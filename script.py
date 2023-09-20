import os

# Определение текущей директории
cwd = os.getcwd()
print(cwd)

# Инициализация переменной для хранения общего количества строк
total_lines = 0

# Проход по всем файлам в текущей директории
for filename in os.listdir(cwd):
    if filename.endswith('.py'):
        # Открытие файла
        with open(filename, 'r', encoding='utf-8') as f:
            # Подсчет количества строк в файле
            file_lines = len(f.readlines())
            # Добавление количества строк в общее количество строк
            total_lines += file_lines
        # Закрытие файла

# Вывод общего количества строк
print(f'Всего строк: {total_lines}')
