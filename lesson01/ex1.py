t = int(input("длительность в секундах = "))

list_s = [24 * 60 * 60, 60 * 60, 60, 1]
list_names = ["дн", "ч", "мин", "c"]
result = ""
rest = t
for i in range(4):
    if t // list_s[i] > 0:
        result = f"{result} {str(rest // list_s[i])} {list_names[i]}"
        rest = rest % list_s[i]

print(result)
