from sys import argv

with open("bakery.csv", 'a', encoding='utf-8') as da:
    with open("bakery.csv", 'r', encoding='utf-8') as dr:
        if len(argv) > 1 and [i for i in argv[1:] if i.replace('.', '').isdigit()]:
            if round(float(argv[1]), 3) <= 99999.99:
                print(f'{round(float(argv[1]), 3):>010}', file=da)
            else:
                print("№ > 99 999,999")
        else:
            print(dr.read())
