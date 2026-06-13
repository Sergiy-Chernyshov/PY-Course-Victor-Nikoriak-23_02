#Task1

def logger(func):
    def wrapper(*args, **kwargs):

        args_str = ", ".join(str(arg) for arg in args)

        print(f"{func.__name__} called with {args_str}")

        return func(*args, **kwargs)

    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

add(4, 5)
square_all(1, 2, 3)

print ("\n")

#Task2

def stop_words(words: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            for word in words:
                result = result.replace(word, "*")

            return result

        return wrapper

    return decorator


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

print(create_slogan("Sergiy"))

assert create_slogan("Sergiy") == "Sergiy drinks * in his brand new *!"


print ("\n")

#Task3

def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            value = args[0]

            if not isinstance(value, type_):
                print("Wrong type")
                return False

            if len(value) > max_length:
                print("Too long")
                return False

            for item in contains:
                if item not in value:
                    print(f"Missing required part: {item}")
                    return False

            return func(*args, **kwargs)

        return wrapper

    return decorator

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

print(create_slogan('johndoe05@gmail.com'))  # False (занадто довгий)
print(create_slogan('S@SH05'))  # правильний результат

assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'