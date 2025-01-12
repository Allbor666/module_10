import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")

        while self.enemies > 0:
            time.sleep(1)  # Задержка в 1 секунду, имитирующая день сражения
            self.days += 1
            self.enemies -= self.power

            # Убедимся, что врагов не осталось меньше нуля
            remaining_enemies = max(self.enemies, 0)

            print(f"{self.name}, сражается {self.days} день(дня)..., осталось {remaining_enemies} воинов.")

        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


# Создание объектов рыцарей
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание окончания всех сражений
first_knight.join()
second_knight.join()

print("Все битвы закончились!")
