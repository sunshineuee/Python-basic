with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    result = []
    for line in f:
        new_line = line.split()
        result.append((new_line[0], new_line[5][1:], new_line[6]))
print(result)