from grupo1 import check_stock
from grupo2 import update_stock

def process_orders(orders: list[dict], inventory: dict) -> None:

    for order in orders:
        order_id = order["order_id"]
        items = order["items"]
        total = 0
        for sku, quantity in items.items():
            product = inventory.get(sku)
            if not product:
                print(f"Error: Product with SKU {sku} not found.")
                continue
            stock_ok, units = check_stock(product, quantity)
            if not stock_ok:
                print(f"Aviso: Insufficient stock for {product['name']}. Available: {product['current_stock']}, Requested: {quantity}")
                print("Proporciono los disponibles")
            # Update stock
            product = update_stock(product, units) # OLD: product["current_stock"] -= quantity
            total += product["price"] * units

        print(f"Order ID: {order_id} - Total: ${total:.2f} - Purchase Completed")