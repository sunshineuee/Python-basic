list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i, word in enumerate(list):
    if word.replace("+","").replace("-","").isdigit():
        if word.isdigit():
            list[i] = f"'{int(word):02}'"
        else:
            list[i] = f"'{word[0]}{int(word[1:]):02}'"

print(" ".join(list))