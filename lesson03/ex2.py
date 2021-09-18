def initialize_numtranslater():
    return {"zero"  : "ноль",
            "one"   : "один",
            "two"   : "два",
            "three" : "три",
            "four"  : "четыре",
            "five"  : "пять",
            "six"   : "шесть",
            "seven" : "семь",
            "eight" : "восемь",
            "nine"  : "девять",
            "ten"   : "десять"
            }
def num_translate(num):
    result = initialize_numtranslater().get(num.lower())
    if result != None and num[0].istitle():
        result = result.title()
    return result

print(num_translate("OnE"))