'''Скрипт повинен вміти читати лог-файл, переданий як аргумент командного рядка, і виводити
статистику за рівнями логування наприклад, INFO, ERROR, DEBUG. Також користувач може вказати
рівень логування як другий аргумент командного рядка, щоб отримати всі записи цього рівня.'''

import sys
from pathlib import Path
# імпортуємо наші функції поіменно щоб уникнути конфлікту
from methods import load_logs, filter_logs_by_level, count_logs_by_level, display_log_counts

user_input = sys.argv

def main():
    '''Головна програма яка виконує весь код і може бути запущена тільки з цього файлу'''
    our_path = None
    detail_log = None
# спочатку перевіряємо введення з консолі на кількість аргументів, щоб розуміти з чим працювати
    if len(user_input) == 2:
        our_path = Path(user_input[-1])
    elif len(user_input) == 3:
        our_path = Path(user_input[1])
        detail_log = user_input[-1]
    else:
        print('Невірна кількість аргументів')
        return # обов'язково треба вбити функцію, інкше код буде виконуватись далі і викине помилку
# тут ми проводимо ще одну перевірку, а саме на наявність файлу чи його суфікс
    if our_path.is_file() and our_path.suffix == '.log':
        display_log_counts(count_logs_by_level(load_logs(our_path)))
    else:
        print('Неправильний формат файлу чи невірна директорія')
# ця частина виконується тільки якщо detail_log не None, а це визначає найперша перевірка
    if detail_log:
        print(f'\nДеталі логів для рівня "{detail_log.upper()}":')
        for log in filter_logs_by_level(load_logs(our_path), detail_log):
            print(f'{log['date']} {log['time']} - {log['message'].strip()}')

# контрольна перевірка чи запускається саме цей файл, інакше код не буде виконаний
if __name__ == '__main__':
    main()
