from math import trunc

while True:
    try:
        amount = float(input("Enter amount to convert: "))
        if amount <= 0:
            raise ValueError()
        break
    except ValueError:
        print("Please enter a valid number.")


currency = {
    "USD":{"EUR":.90, "CAD":1.10},
    "EUR":{"USD":1.1, "CAD":1.30},
    "CAD":{"EUR":.68, "USD":.80}
}

while True:
    try:
        source_cur=input("Enter source currency to convert (USD/EUR/CAD): ").upper()
        if source_cur not in currency.keys():
            raise ValueError()
        break
    except ValueError:
        print("Please enter a valid currency.")

while True:
    try:
        target_cur=input("Enter target currency to convert (USD/EUR/CAD): ").upper()
        if source_cur not in currency.keys():
            raise ValueError()
        break
    except ValueError:
        print("Please enter a valid currency.")

if source_cur==target_cur:
    calculation=amount
else:
    calculation= amount*currency[source_cur][target_cur]
                     
print(f"Your {source_cur} {amount} equals to  {target_cur} {calculation:.2f}")

