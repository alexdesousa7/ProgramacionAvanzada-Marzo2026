def update_stock(product: dict, sold_units: int):
    if not isinstance(product, dict):
        raise Exception('Estructura de producto incorrecta')
    
    if not isinstance(sold_units, int):
        raise Exception('Valor incorrecto')
        
    if product['current_stock'] < sold_units:
        raise Exception('No hay suficiente producto')
     
    product['current_stock'] -= sold_units
    
    return product
