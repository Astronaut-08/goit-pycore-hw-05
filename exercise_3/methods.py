'''Тут зібрані всі функції для роботи з лог файлом'''

def parse_log_line(line: str) -> dict:
    '''Приймає рядрок файлу і повертає словник значень з рядка'''
    # розбиваємо наш рядок по пробілах на 3 індекси (4 частини)
    parse_line = line.split(' ', 3)
    result = { # присвоюємо значення кожному ключу з робитого рядка
        'date': parse_line[0],
        'time': parse_line[1],
        'level': parse_line[2],
        'message': parse_line[3]
    }
    return result

def load_logs(file_path: str) -> list:
    '''загружає файл і парсить рядки за допомогою попередньо створеної функції'''
    result = list()
    with open(file_path, 'r', encoding='utf-8') as file:
        # проходимось по кожному рядку окремо і парсимо його як нам треба
        for line in file.readlines():
            result.append(parse_log_line(line))
    return result

def filter_logs_by_level(logs: list, level:str) -> list:
    '''Фільтрує і виводить певні логи, отримує на вхід список з функції
    load_logs і фільтр слово, наприклад ERROR'''
    # використовуємо функці filter яка приймає в себе фукнцію як ключ фільтрації
    filtred_logs = filter(lambda x: x['level'] == level.upper(), logs)
    return list(filtred_logs)

def count_logs_by_level(logs: list) -> dict:
    '''Отримує список логів із функції load_logs та підбиває їх статистику'''
    result = {log.get('level'): 0 for log in logs} # робимо dict comprehention з наших рівнів
    for log in logs: # підбиваємо підсумок по кількості кожного рівня
        result[log['level']] += 1
    return result

def display_log_counts(counts: dict):
    '''Форматує та виводить результати в читабельній формі'''
    # в цьому блоці ми зробили шапку нашого виклику в консоль
    print('Рівень логування | Кількість')
    print('-----------------|----------')
    for key, value in counts.items():
    # тут ми пройшлись по словнику і вивели кожен елемент з певним відступом
        print(f'{key:<17}|{value}')
