# salary taxes system in  bangladesh
while True:
    try:
        monthly_income = int(input("Enter your monthly income for knowing how much tax you should pay in one year: "))
        taxable_income = monthly_income * 12
        if taxable_income <= 300000:
            print("You should pay 0% tax of your year income.")
        elif 300000 < taxable_income <= 400000:
            tax = taxable_income * 5 / 100
            print(f"You should pay tax: {tax}$ for your one year income: {taxable_income}")
        elif 400000 < taxable_income <= 700000:
            tax1 = taxable_income * 10 / 100
            print(f"You should pay tax: {tax1}$ for your one year income: {taxable_income}")
        elif 700000 < taxable_income <= 1100000:
            tax2 = taxable_income * 15 / 100
            print(f"You should pay tax: {tax2}$ for your one year income: {taxable_income}")
        elif 1100000 < taxable_income <= 1600000:
            tax3 = taxable_income * 20 / 100
            print(f"You should pay tax: {tax3}$ for your one year income: {taxable_income}")
        else:
            tax4 = taxable_income * 25 / 100
            print(f"You should pay tax: {tax4}$ for your one year income: {taxable_income}")
        break
    except ValueError:
        print("Enter the right keyword!")
