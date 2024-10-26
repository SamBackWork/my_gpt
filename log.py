import datetime


def history_log(log):
    print("Выберите период:")
    print("1. Часы")
    print("2. Дни")
    print("3. Недели")
    print("4. Месяцы")
    choice = input(">> ")
    if choice == "1":
        hours = int(input("Введите количество часов: "))
        start_time = datetime.datetime.now() - datetime.timedelta(hours=hours)
    elif choice == "2":
        days = int(input("Введите количество дней: "))
        start_time = datetime.datetime.now() - datetime.timedelta(days=days)
    elif choice == "3":
        weeks = int(input("Введите количество недель: "))
        start_time = datetime.datetime.now() - datetime.timedelta(weeks=weeks)
    elif choice == "4":
        months = int(input("Введите количество месяцев: "))
        start_time = datetime.datetime.now() - datetime.timedelta(days=months*30)
    else:
        print("Неправильный выбор")
        return None
    end_time = datetime.datetime.now()
    print("Start time:", start_time)
    print("End time:", end_time)
    with open(log, 'r', encoding='utf-8') as f:
        print("Log file contents:")
        for line in f:
            print(line.strip())
        f.seek(0)  # Сбросить указатель файла на начало файла
        for line in f:
            line = line.strip()  # Удалить пустые строки
            if not line:
                continue
            if not line[:10].isdigit():  # Проверяем, начинается ли строка с даты
                continue
            timestamp = datetime.datetime.strptime(line[:26], "%Y-%m-%d %H:%M:%S.%f")
            print("Timestamp:", timestamp)
            if start_time <= timestamp <= end_time:
                print("Found log entry within time range!")
                print(line)  # Выводим всю строку
                # Выводим следующую строку, если она является частью вопроса или ответа
                next_line = f.readline()
                while next_line and not next_line.startswith(
                        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")):
                    print(next_line.strip())  # Выводим всю строку
                    next_line = f.readline()