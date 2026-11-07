import requests

amount = float(input("Enter the amount of currency: "))
currency = input("Enter currency (USD, EUR, PLN): ").upper()

if currency == "USD" or currency == "EUR" or currency == "PLN":
    
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
    res = requests.get(url)
    rates = res.json()
    
    for item in rates:
        if item["cc"] == currency:
            print("NBU Rate:", item["rate"])
            print("Result in UAH:", amount * item["rate"])
            break
            
else:
    print("Unsupported currency!")