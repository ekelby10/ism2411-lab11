print("--- Excercise 1 ---")
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

print("--- Excercise 2 ---")
customer["phone"] = "813-555-0142"

print(customer)
customer["tier"] = "silver"

print(customer)
del customer["email"]
print(customer)

print("--- Excercise 3 ---")

print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError as error:
    print(f"KeyError Caught: {error}")

print("--- Excercise 4 ---")
for key, value in customer.items():
    print(f"{key}: {value}")

for item in customer:
    print(item)

print("--- Excercise 5 ---")
tier_discounts ={"bronze": 0,
                 "silver": 0.05,
                 "gold": 0.10,
                 "platinum": 0.15}
purchase = 200
discount = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount)

print(f"Tier: {customer['tier']}")
print(f"Discount: {discount *100:.0f}%")
print(f"Final Price: {final_price:.2f}")

print("---Excercise 6 ---")
customer = [
    {"name": "Bob", "tier": "silver", "ytd_spend": 3200},
    {"name": "Carol", "tier": "gold", "ytd_spend": 8750},
    {"name": "David", "tier": "bronze", "ytd_spend": 450},
]

for record in customer:
    rate = tier_discounts.get(record["tier"], 0)
    discount = 300 * rate
    final_price = 300 - discount
    print(f"{record['name']} ({record['tier']}): ${discount:.2f} discount on $300 purchase")

    print("---Excercise 7 ---")
    catalog = {
        "Widget A": {"price": 9.99, "stock": 150},
        "Gadget C": {"price": 49.99, "stock": 8}
    }

for product, details in catalog.items():
    print(f"LOW STOCK: {product} - Only {details['stock']} left in stock!")

print("---Excercise 8 ---")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "East", "amount": 200},
]
sales_by_region = {}
for sale in transactions:
    region = sale["region"]
    sales_by_region[region] = sales_by_region.get(region, 0) + sale["amount"]
    print(sales_by_region)

for region in sorted(sales_by_region):
    print(f"{region}: {sales_by_region[region]}")
print("---Reflection---")
## 1. I use bracket notation when a key should always exist because it raises an error if data is missing. I use .get() when a key might be missing because it safely returns a default value instead of crashing the program.
# 2. Building a summary dictionary is similar to using PivotTables or COUNTIF/SUMIF formulas in Excel because both summarize data by category. Python is more useful for large datasets because it can automate the process and handle much more data with less manual work.
