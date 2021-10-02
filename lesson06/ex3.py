from json import dump
from itertools import zip_longest

with open('users.csv', 'r', encoding='utf-8') as users:
    with open('hobby.csv', 'r', encoding='utf-8') as hobby:
        if len(users.readlines()) >= len(hobby.readlines()):
            users.seek(0)
            hobby.seek(0)

            with open('dict.json', 'w', encoding='utf-8') as f:
                all_list = zip_longest((' '.join(us.split(',')) for us in users), hobby, fillvalue=None)
                dict_ = {str(el0).strip():str(el1).strip() for el0, el1 in all_list}
                dump(dict_, f, ensure_ascii=False, indent=4)
            print(dict_)
        else:
            exit(1)



