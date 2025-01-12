import threading
import random
import time


class Bank:
    def __init__(self):
        self.balance = 0  # Начальный баланс
        self.lock = threading.Lock()  # Блокировка для потоков

    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)  # Генерация случайного пополнения
            self.lock.acquire()  # Захватываем блокировку

            self.balance += amount
            print(f"Пополнение: {amount}. Баланс: {self.balance}")

            # Если баланс >= 500, обсудим освобождение блокировки
            if self.balance >= 500:
                if self.lock.locked():  # Только если замок заблокирован
                    print("Баланс >= 500, замок будет разблокирован")
                    self.lock.release()  # Освобождаем блокировку

            else:
                self.lock.release()  # Освобождаем блокировку если не достигли 500

            time.sleep(0.001)  # Задержка для имитации времени выполнения

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)  # Генерация случайного снятия
            print(f"Запрос на {amount}")

            self.lock.acquire()  # Захватываем блокировку

            if amount <= self.balance:
                self.balance -= amount
                print(f"Снятие: {amount}. Баланс: {self.balance}")
                self.lock.release()  # Освобождаем блокировку после успешного снятия
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.release()  # Освобождаем блокировку даже если средств недостаточно

            time.sleep(0.001)  # Задержка для имитации времени выполнения


# Создание объекта банка
bk = Bank()

# Создание потоков для выполнения методов deposit и take
th1 = threading.Thread(target=bk.deposit)  # Передаем объект Bank
th2 = threading.Thread(target=bk.take)  # Тот же объект для снятия

# Запуск потоков
th1.start()
th2.start()

# Ожидание завершения потоков
th1.join()
th2.join()

# Вывод итогового баланса
print(f'Итоговый баланс: {bk.balance}')
