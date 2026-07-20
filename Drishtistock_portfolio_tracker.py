# ==========================================
# Project : Stock Portfolio Tracker
# Developed By : Drishti Soni
# Internship : CodeAlpha Python Internship
# ==========================================

# Predefined stock prices
stock_prices = {
    "TCS": 3500,
    "INFY": 1600,
    "RELIANCE": 2900,
    "HDFC": 1700,
    "WIPRO": 550,
    "ITC": 450,
    "SBIN": 900,
    "TATASTEEL": 180
}

portfolio = {}

print("=" * 50)
print("      STOCK PORTFOLIO TRACKER")
print("=" * 50)
print("Developed By : Drishti Soni")
print("CodeAlpha Python Internship")
print("=" * 50)

while True:
    print("\nAvailable Stocks:")
    for stock, price in stock_prices.items():
        print(f"{stock} : ₹{price}")

    stock_name = input("\nEnter Stock Name (or type 'done'): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("❌ Stock not available.")
        continue

    try:
        quantity = int(input("Enter Quantity: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

print("\n" + "=" * 50)
print("YOUR PORTFOLIO")
print("=" * 50)

total = 0

for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    total += value
    print(f"{stock} | Qty: {quantity} | Value: ₹{value}")

print("-" * 50)
print(f"Total Investment Value : ₹{total}")
print("=" * 50)

# Save to file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio\n")
    file.write("Developed By : Drishti Soni\n\n")
    for stock, quantity in portfolio.items():
        value = stock_prices[stock] * quantity
        file.write(f"{stock} | Qty: {quantity} | Value: ₹{value}\n")
    file.write(f"\nTotal Investment : ₹{total}")

print("\n✅ Portfolio saved as portfolio.txt")
print("Thank you for using Stock Portfolio Tracker!")
