from bs4 import BeautifulSoup
import requests


def about():
    print("\n \t\tOnline Currency exchange ")
    print("Source from the https://www.xe.com/en website")
    print("1. For all Currencies exchange rate[1]")
    print("2. For an specific Currencies exchange rate[2]")


def all(key):
    page = requests.get("https://www.xe.com/en/currencytables/?from=USD")
    soup = BeautifulSoup(page.text, "html.parser")
    results = soup.find_all("tr",)
    if key is None:
        print(f"\n code \t\t currency\tunites_per_USD\tUSD_per_unites ")
        for x in range(1, len(results) - 9):
            data = results[x]
            code = data.find("a")
            currency = data.find_all("td")
            unites_per_USD = currency[2]
            USD_per_unites = currency[3]
            print(
                f" {code.text}\t\t{currency[1].text}\t{unites_per_USD.text}\t{USD_per_unites.text}"
            )
    else:
        print(f"\n code \t\t currency\t\tunites_per_USD\t\tUSD_per_unites ")
        for x in range(1, len(results) - 9):
            data = results[x]
            if data.find("a").text == key.strip().upper():
                code = data.find("a")
                currency = data.find_all("td")
                unites_per_USD = currency[2]
                USD_per_unites = currency[3]
                print(
                    f" {code.text}\t\t{currency[1].text}\t\t{unites_per_USD.text}\t\t{USD_per_unites.text}\n"
                )
                return 0


def exe(mode):
    if mode == 1:
        all(key=None)
    elif mode == 2:
        key = input("Enter the currency code or name : ")
        all(key=key)


about()
m = int(input(" Enter mode[1/2] : "))
exe(m)
