"""
    Determine las ventas con IVA para N ventas.
"""

PORCENTAJE_IVA = 16

productos = 0
precio_total = 0

while productos <= 5:
    precio = int(input("> Ingresa el precio del producto numero [{}]: ".format(productos)))
    precio_total = precio_total + precio
    productos = productos + 1
    aumento = precio_total * (PORCENTAJE_IVA / 100)
    precio_iva = precio_total + aumento
    
print(f"TOTAL: {precio_total} | IVA: {aumento} | TOTAL CON IVA: {precio_iva}")