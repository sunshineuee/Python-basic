list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = []

for word in list:
    if word.replace("+","").replace("-","").isdigit():
        if word.isdigit():
            result.append(f"'{int(word):02}'")
        else:
            result.append(f"'{word[0]}{int(word[1:]):02}'")
    else:
        result.append(word)
print(" ".join(result))