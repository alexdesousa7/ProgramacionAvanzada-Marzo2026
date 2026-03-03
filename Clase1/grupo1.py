def check_stock(product: dict, requested_units: int) -> tuple[bool, int]:
    if not product.get("current_stock"): 
        raise Exception("No existe el atributo current_stock en el diccionario producto")
    if product["current_stock"] < 0 :
        raise Exception("El valor del atributo current_stock no puede ser negativo")
    has_enough_stock = product["current_stock"] >= requested_units
    units_to_provide = requested_units if has_enough_stock else product["current_stock"]
    return (has_enough_stock, units_to_provide)
