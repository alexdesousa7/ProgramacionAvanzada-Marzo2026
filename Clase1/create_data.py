def create_data():
    
    # Categories management:
    categories = [
        {"name": "Electronics", "description": "Devices and gadgets"},
        {"name": "Office", "description": "Office supplies and equipment"}
    ]

    # Tags management:
    tags = [
        {"name": "On Sale"},
        {"name": "New Arrival"},
        {"name": "Best Seller"}
    ]

    # Products management:
    products = [
        {"name": "Laptop", "sku": "SKU123", "price": 1200, "current_stock": 10, "categories": [categories[0]], "tags": [tags[1], tags[2]]},
        {"name": "Mouse", "sku": "SKU456", "price": 25, "current_stock": 100, "categories": [categories[0]], "tags": [tags[0]]},
        {"name": "Keyboard", "sku": "SKU789", "price": 50, "current_stock": 50, "categories": [categories[1]], "tags": [tags[2]]},
        {"name": "Monitor", "sku": "SKU101", "price": 300, "current_stock": 20, "categories": [categories[0]], "tags": []}
    ]

    # Inventory management
    inventory = {product["sku"]: product for product in products} # Comprehensions

    return categories, tags, products, inventory
