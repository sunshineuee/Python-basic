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
    return initialize_numtranslater().get(num.lower())

print(num_translate("OnE"))