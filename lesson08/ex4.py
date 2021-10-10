def val_checker(is_valid):
    # Передаем саму функцию
    def wrapper(funk):
        # Передаем значения функции и проверяем их
        def dev_by_3(*args):
            if is_valid(*args):
                result = funk(*args)
                return result
            else:
                raise ValueError('Wrong value')
        return dev_by_3
    return wrapper


@val_checker(lambda x: x > 0)
def calc_cube(x):
    print(x ** 3)
    return x


calc_cube(-2)