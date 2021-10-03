import collections

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    dict_ = collections.Counter()
    for line in f:
        dict_[line.split()[0]] += 1
    print(f'{dict_.most_common(1)[0][0]}  - {dict_.most_common(1)[0][1]}')
