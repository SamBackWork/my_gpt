import datetime
from utils import starts_with_datetime


def history_log(log):
    period_functions = {
        "1": lambda num: datetime.datetime.now() - datetime.timedelta(hours=num),
        "2": lambda num: datetime.datetime.now() - datetime.timedelta(days=num),
        "3": lambda num: datetime.datetime.now() - datetime.timedelta(weeks=num),
        "4": lambda num: datetime.datetime.now() - datetime.timedelta(days=num * 30),
    }
    period_names = {
        "1": "часов",
        "2": "дней",
        "3": "недель",
        "4": "месяцев",
    }
    print("Выберите период:\n1. Часы\n2. Дни\n3. Недели\n4. Месяцы")
    choice = input(">> ")
    if int(choice) not in range(1, 5):
        print("Неправильный выбор")
        return None
    try:
        num = int(input(f"Введите количество {period_names[choice]}: "))
        start_time = period_functions[choice](num).strftime("%Y-%m-%d %H:%M:%S")
        end_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("Start time:", start_time)
        print("End time:", end_time)
    except ValueError:
        print("Неправильный выбор")
        return None
    with open(log, 'r', encoding='utf-8') as f:
        print("Log file contents:")
        for line in f:
            if starts_with_datetime(line):
                last_valid_date = line[:19]
            if start_time <= last_valid_date <= end_time:
                print(line.strip())
