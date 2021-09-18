list = [57.8, 46.51, 97, 6.9, 70.09]

for price in list:
    listprice = f"{price:2f}".split(".")
    print(f"{listprice[0]} руб {listprice[1][:2]} коп")