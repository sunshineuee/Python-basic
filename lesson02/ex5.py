list = [57.8, 46.51, 97, 6.9, 70.09]
list.sort()
for price in list:
    listprice = f"{price:2f}".split(".")
    print(f"{listprice[0]} руб {listprice[1][:2]} коп,", end = " ")

list1 = list.copy()
list1.sort(reverse=True)
print("\n")
print(" ".join(map(str, list1[:5])))