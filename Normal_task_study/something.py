from functools import reduce

orders = [
    {"product": "Laptop", "price": 1200.00, "quantity": 2},
    {"product": "Mouse", "price": 25.50, "quantity": 5},
    {"product": "Keyboard", "price": 75.00, "quantity": 3},
    {"product": "Monitor", "price": 300.00, "quantity": 1},
    {"product": "USB Cable", "price": 10.00, "quantity": 10}
]

# Step 1: Calculate total price per order
order_totals = list(map(lambda order: {"product": order["product"], "total": order["price"] * order["quantity"]}, orders))

discounts = list(map(lambda disc: {"product": disc["product"], "total": disc["total"] * 0.9} if disc["total"] > 1000 else disc, order_totals))

small_orders = list(filter(lambda order2: order2["total"] < 300, order_totals))

biggest_order = reduce(lambda x,y: x if x["total"] > y["total"] else y, discounts)

print(order_totals)
print(discounts)
print(small_orders)
print(biggest_order)