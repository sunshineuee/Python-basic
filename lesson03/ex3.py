def thesaurus(*args):
    result = {}
    for name in args:
        result.setdefault(name[0],[]).append(name)
    return result

print(thesaurus("Ваня","Петя","Вася","Волан-де-Морт"))