
import time
import threading

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            time.sleep(0.1)  # Пауза в 0.1 секунды
    print(f"Завершилась запись в файл {file_name}")

# Время начала выполнения
start_time = time.time()

# Вызов функций с заданными данными
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

# Время окончания выполнения
end_time = time.time()
print(f"Работа функций {end_time - start_time:.6f} секунд")

# Создание потоков для записи в файлы
threads = []
file_args = [
    (10, "example5.txt"),
    (30, "example6.txt"),
    (200, "example7.txt"),
    (100, "example8.txt")
]

# Время начала выполнения потоков
start_thread_time = time.time()

for args in file_args:
    thread = threading.Thread(target=write_words, args=args)
    threads.append(thread)
    thread.start()

# Ожидание завершения всех потоков
for thread in threads:
    thread.join()

# Время окончания выполнения потоков
end_thread_time = time.time()
print(f"Работа потоков {end_thread_time - start_thread_time:.6f} секунд")
