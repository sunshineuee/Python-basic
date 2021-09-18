
def thesaurus_adv(*args):
    result = {}
    for fullname in args:
        name, family = fullname.split()
        result.setdefault(family[0], {}).setdefault(name[0], []).append(fullname)
    return result


print(thesaurus_adv("Ваня Петров", "Петя Иванов", "Вася Дубов", "Волан Де-Морт", "Федор Достоевский"))
