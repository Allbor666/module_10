import time
from multiprocessing import Pool

# Функция для чтения информации из файла
def read_info(name):
    all_data = []  # Локальный список для хранения данных
    try:
        with open(name, 'r') as file:  # Открываем файл для чтения
            while True:
                line = file.readline()  # Читаем строку
                if not line:  # Если строка пустая, выходим из цикла
                    break
                all_data.append(line.strip())  # Добавляем строку в список (убираем лишние пробелы)
    except FileNotFoundError:
        print(f"Файл {name} не найден.")  # Обработка ошибки отсутствия файла
    return all_data  # Возвращаем собранные данные

if __name__ == '__main__':
    # Список названий файлов
    filenames = [f'file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_time = time.time()  # Запись времени начала
    for filename in filenames:
        read_info(filename)  # Считываем информацию из файла
    linear_time = time.time() - start_time  # Расчет времени выполнения
    print(f"Линейное время выполнения: {linear_time:.6f} секунд")

    # Многопроцессный вызов
    start_time = time.time()  # Запись времени начала
    with Pool() as pool:  # Создаем пул процессов
        results = pool.map(read_info, filenames)  # Используем метод map для считывания файлов
    multi_process_time = time.time() - start_time  # Расчет времени выполнения
    print(f"Многопроцессное время выполнения: {multi_process_time:.6f} секунд")
