'''Парсинг логов'''
import pprint
# Поиск ошибок и сохранение в текстовый файл
errors = []

with open('Log_parsing\generated_logs.txt', 'r', encoding='utf-8') as file:
    for string in file:
        if 'ERROR' in string:
            errors.append(string)


# Количество типов ошибок
print('Всего типов ошибок найдено: ', len(set(errors)))


if errors:

    # Создание/открытие файла и помещение в него найденных ошибок
    with open('Log_parsing\errors.txt', 'w', encoding='utf-8') as f:
        for error in errors:
            f.write(error.strip() + '\n')
        print('Ошибки успешно записаны в файл errors.txt')

else:
    print('Ошибок не найдено.')

not_connect = []
database = []
# Поиск ошибок связанных с потерей соединения с сервером и ошибок с базой данных
with open('Log_parsing\errors.txt', 'r', encoding='utf-8') as file:
    for report in file:
        if 'Connection lost to server' in report:
            not_connect.append(report)
        elif 'Database write failed' in report:
            database.append(report)
pprint.pprint(not_connect)
pprint.pprint(database)
