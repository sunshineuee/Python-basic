n = int(input("введите процент: "))
if n > 10 and n < 20
    p = "процентов"
elif n % 10 == 1:
    p = "процент"
elif n % 10 >= 2 and n % 10 <= 4:
    p = "процента"
else:
    p = "процентов"

print(f"{n} {p}")
