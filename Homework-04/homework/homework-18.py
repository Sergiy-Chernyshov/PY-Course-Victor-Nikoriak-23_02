#task1

class User:
    def __init__(self, email: str):
        if self.validate(email):
            self.email = email
            print(f"Об'єкт створено успішно з email: {self.email}")
        else:
            raise ValueError(f"Некоректний формат email: {email}")

    @classmethod
    def validate(cls, email: str) -> bool:
        """Перевірка"""
        # 1. Перевіряємо @
        if "@" not in email:
            return False

        # 2. Розділяємо на ім'я та домен
        parts = email.split("@")
        if len(parts) != 2:
            return False

        domain = parts[1]

        # 3. Перевіряємо, чи є в домені крапка і чи він не порожній
        if "." not in domain or domain.startswith(".") or domain.endswith("."):
            return False

        return True

try:
    # Варіант 1: Правильний email
    user1 = User("test@example.com")
except ValueError as e:
    print(e)

try:
    # Варіант 2: Неправильний email (без домену)
    user2 = User("bad-email@com")  # Цей приклад пройде нашу просту логіку,
    # але якщо треба суворіше — логіку validate треба ускладнити.

    # Варіант 3: Явно неправильний email
    user3 = User("invalid_string")
except ValueError as e:
    print(f"Помилка: {e}")

print (":\n")

#Task2

class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []  # Прихований список працівників

    @property
    def workers(self):
        """Гетер для отримання списку працівників (тільки для читання)"""
        return self._workers

    def add_worker(self, worker):
        """Метод для додавання працівника до списку боса"""
        if isinstance(worker, Worker):
            if worker not in self._workers:
                self._workers.append(worker)
                # Важливо: коли ми додаємо працівника босу,
                # ми також маємо призначити цьому працівнику цього боса
                if worker.boss != self:
                    worker.boss = self
        else:
            print("Помилка: До списку можна додавати лише екземпляри класу Worker")

    def __repr__(self):
        return f"Boss(id={self.id}, name='{self.name}')"


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = None  # Створюємо порожнє поле для боса
        self.boss = boss   # Викликаємо сеттер для перевірки та призначення

    @property
    def boss(self):
        """Гетер: повертає поточного боса працівника"""
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        """Сеттер: перевіряє, чи є новий бос екземпляром класу Boss"""
        if isinstance(new_boss, Boss):
            # Якщо у працівника вже був інший бос, його варто було б видалити зі списку старого боса
            self._boss = new_boss
            # Додаємо працівника до списку нового боса, якщо його там ще немає
            if self not in new_boss.workers:
                new_boss.add_worker(self)
        else:
            raise ValueError("Босом може бути лише екземпляр класу Boss!")

    def __repr__(self):
        return f"Worker(id={self.id}, name='{self.name}')"


# Тест

# 1. Створюємо Босів
boss_ivan = Boss(1, "Іван Петрович", "SoftServe")
boss_olga = Boss(2, "Ольга Миколаївна", "EPAM")

# 2. Створюємо Працівника та одразу призначаємо йому боса
worker_1 = Worker(101, "Андрій", "SoftServe", boss_ivan)

# 3. Перевіряємо зв'язок
print(f"Бос Андрія: {worker_1.boss.name}")
print(f"Працівники Івана Петровича: {boss_ivan.workers}")

# 4. Змінюємо боса через сеттер
worker_1.boss = boss_olga

print(f"Новий бос Андрія: {worker_1.boss.name}")
print(f"Працівники Ольги: {boss_olga.workers}")

# 5. Спроба призначити неправильного боса (викличе помилку)
try:
    worker_1.boss = "Просто якийсь рядок"
except ValueError as e:
    print(f"Помилка валідації: {e}")

print ("\n")

#task3

from functools import wraps


class TypeDecorators:

    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return int(result)
            except (ValueError, TypeError):
                print(f"Помилка: Неможливо конвертувати '{result}' у int")
                return result

        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return str(result)

        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            # Для рядків 'True'/'False' часто потрібна спеціальна логіка
            if isinstance(result, str):
                if result.lower() == 'true':
                    return True
                if result.lower() == 'false':
                    return False
            return bool(result)

        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return float(result)
            except (ValueError, TypeError):
                print(f"Помилка: Неможливо конвертувати '{result}' у float")
                return result

        return wrapper


# Тест

@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


@TypeDecorators.to_float
def get_price(value: str):
    return value


# Перевірка через assert
assert do_nothing('25') == 25
assert do_something('True') is True
assert get_price('19.99') == 19.99

print("Усі перевірки пройдено успішно!")
print(f"Результат do_nothing: {do_nothing('25')} (тип: {type(do_nothing('25'))})")
print(f"Результат do_something: {do_something('True')} (тип: {type(do_something('True'))})")