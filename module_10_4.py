import threading
import random
import time
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number  # Номер стола
        self.guest = None  # Гость за столом по умолчанию None


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name  # Имя гостя

    def run(self):
        wait_time = random.randint(3, 10)  # Случайное время ожидания (3-10 секунд)
        time.sleep(wait_time)  # Имитация времени, проведенного за столом


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()  # Очередь для гостей
        self.tables = tables  # Список столов в кафе

    def guest_arrival(self, *guests):
        for guest in guests:
            # Проверяем наличие свободных столов
            assigned = False
            for table in self.tables:
                if table.guest is None:  # Если стол свободен
                    table.guest = guest  # Назначаем сидеть гостя за стол
                    guest.start()  # Запускаем поток гостя
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    assigned = True
                    break

            if not assigned:  # Если столов больше нет
                self.queue.put(guest)  # Помещаем гостя в очередь
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        # Обслуживаем гостей, пока очередь не пуста или есть занятые столы
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None:  # Если за столом есть гость
                    guest = table.guest
                    if not guest.is_alive():  # Если гость закончил прием пищи
                        print(f"{guest.name} покушал(-а) и ушёл(ушла)")
                        print(f"Стол номер {table.number} свободен")
                        table.guest = None  # Освобождаем стол

                        # Проверяем, есть ли очередь гостей
                        if not self.queue.empty():
                            next_guest = self.queue.get()  # Берем следующего из очереди
                            table.guest = next_guest
                            next_guest.start()  # Запускаем поток нового гостя
                            print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
            time.sleep(1)  # Пауза между проверками


# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya',
    'Arman', 'Vitoria', 'Nikita', 'Galina', 'Pavel',
    'Ilya', 'Alexandra'
]

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()
