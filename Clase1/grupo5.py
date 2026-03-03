from grupo4 import process_orders
from grupo3 import show_inventory_report
from Clase1.create_data import create_data

categories, tags, products, inventory = create_data()

# Incoming orders:
orders = [
    {"order_id": "ORDER001", "items": {"SKU123": 2, "SKU456": 5}},
    {"order_id": "ORDER002", "items": {"SKU789": 3, "SKU101": 1}},
    {"order_id": "ORDER003", "items": {"SKU456": 10, "SKU101": 2}}
]

# Process orders:
process_orders(orders, inventory)

# Show inventory report after processing orders:
show_inventory_report(inventory)
