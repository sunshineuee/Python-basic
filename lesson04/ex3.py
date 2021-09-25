import ex2
from datetime import date


def currency_rates(valute_code):
    content = ex2.content_cbr()
    date = date_cbr(content)
    return date, ex2.currency_rates(valute_code, content)


def date_cbr(content):
    content_date = content[len('<?xml version="1.0" encoding="windows-1251"?><ValCurs Date="'):len(
        '<?xml version="1.0" encoding="windows-1251"?><ValCurs Date="25.09.2021')].split(".")
    return date(year=int(content_date[2]), month=int(content_date[1]), day=int(content_date[0]))


if __name__ == "__main__":
    print(currency_rates("AMD"))
