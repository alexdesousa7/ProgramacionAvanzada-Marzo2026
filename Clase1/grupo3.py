def show_inventory_report(inventory: dict) -> None:
    print("\nInventory Report:\n")
    for product in inventory.values():
        category_names = ", ".join([cat["name"] for cat in product["categories"]]) or "None"
        tag_names = ", ".join([tag["name"] for tag in product["tags"]]) or "None"
        print(f"Product: {product['name']} (SKU: {product['sku']}) - Price: ${product['price']:.2f}, Stock: {product['current_stock']}, Categories: [{category_names}], Tags: [{tag_names}]")
