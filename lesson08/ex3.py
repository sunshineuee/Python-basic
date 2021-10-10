def decorator(funk):

    def type_logger(*args, **kwargs):
        with open('logger.txt', 'a', encoding='utf-8') as f:
            for arg in args:
                x_type = type(arg)
                x_type = str(x_type)
                f.write(f'{arg}: {x_type}\n')
            for kwarg in kwargs:
                x_type = type(kwarg)
                x_type = str(f'{kwarg}: {x_type}\n')
                f.write(x_type + '\n')

        equals = funk(*args, **kwargs)

        return equals

    return type_logger


@decorator
def calc_power(x, y=3):
    print(x ** y)
    return x, y


calc_power(5, 9)