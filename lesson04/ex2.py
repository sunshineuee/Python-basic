from requests import get, utils


def currency_rates(valute_code, content=None):
    if content is None:
        content = content_cbr()
    contentsplit = content.split(f"<CharCode>{valute_code}</CharCode>")
    if len(contentsplit) == 2:
        return float(contentsplit[1].split("<Value>")[1].split("</Value>")[0].replace(",", "."))
    else:
        return None


def content_cbr():
    response = get("http://www.cbr.ru/scripts/XML_daily.asp")
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    return content


if __name__ == "__main__":
    print(currency_rates("AMD"))
