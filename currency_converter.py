def get_amount():
    while True:
        try:
            amount = float(input("Enter amount to convert: "))
            if amount <= 0:
                raise ValueError()
            return amount
        except ValueError:
            print("Please enter a valid number.")


exchange_rates = {
    "USD":{"EUR":.90, "CAD":1.10},
    "EUR":{"USD":1.1, "CAD":1.30},
    "CAD":{"EUR":.68, "USD":.80}
}

def get_currency(label):
    while True:
        try:
            currency=input(f"Enter {label} currency to convert (USD/EUR/CAD): ").upper()
            if currency not in exchange_rates.keys():
                raise ValueError()
            return currency
        except ValueError:
            print("Please enter a valid currency.")

def calculate_currency(amount, source_cur, target_cur):
    if source_cur==target_cur:
        return amount

    return amount * exchange_rates[source_cur][target_cur]


def main():
    amount = get_amount()
    source_cur=get_currency("Source")
    target_cur=get_currency("Target")
    converted_amount=calculate_currency(amount, source_cur, target_cur)
    print(f"converted currency:  {source_cur} {amount} equals to  {target_cur} {converted_amount}")

if __name__ == "__main__":
    main()