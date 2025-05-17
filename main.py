plantilla_producto = {
    "id": None,
    "nombre": "",
    "precio": 0,
    "cantidad": 0
}

productos_base: dict[int, dict] = {
    1: {**plantilla_producto, "id": 1, "nombre": "Lay's", "precio": 1000, "cantidad": 5},
    2: {**plantilla_producto, "id": 2, "nombre": "Doritos", "precio": 1500, "cantidad": 5},
    3: {**plantilla_producto, "id": 3, "nombre": "Choclitos", "precio": 500, "cantidad": 5},
    4: {**plantilla_producto, "id": 4, "nombre": "Cheetos", "precio": 900, "cantidad": 5},
    5: {**plantilla_producto, "id": 5, "nombre": "Mani", "precio": 500, "cantidad": 5},
    6: {**plantilla_producto, "id": 6, "nombre": "Mani Moto", "precio": 700, "cantidad": 5},
    7: {**plantilla_producto, "id": 7, "nombre": "Mani con pasas", "precio": 600, "cantidad": 5},
    8: {**plantilla_producto, "id": 8, "nombre": "Mani Mixto", "precio": 800, "cantidad": 5},
    9: {**plantilla_producto, "id": 9, "nombre": "Gala", "precio": 1000, "cantidad": 5},
    10: {**plantilla_producto, "id": 10, "nombre": "Chocorramo", "precio": 1200, "cantidad": 5},
    11: {**plantilla_producto, "id": 11, "nombre": "Gansito", "precio": 900, "cantidad": 5},
    12: {**plantilla_producto, "id": 12, "nombre": "Browni", "precio": 2500, "cantidad": 5},
    13: {**plantilla_producto, "id": 13, "nombre": "Pepsi", "precio": 1500, "cantidad": 5},
    14: {**plantilla_producto, "id": 14, "nombre": "Manzana", "precio": 1500, "cantidad": 5},
    15: {**plantilla_producto, "id": 15, "nombre": "Colombiana", "precio": 1500, "cantidad": 5},
    16: {**plantilla_producto, "id": 16, "nombre": "Uva", "precio": 1500, "cantidad": 5},

}
productos = productos_base.copy()


def leer_entero(prompt: str, minimo: int = None, maximo: int = None) -> int:
    while True:
        try:
            valor = int(input(prompt))
            if (minimo is not None and valor < minimo) or (maximo is not None and valor > maximo):
                print("Número fuera de rango. Intenta de nuevo.")
            else:
                return valor
        except ValueError:
            print("Entrada no válida. Debes ingresar un número entero.")

def mostrar_menu() -> int:
    print("\n===== MENÚ DE OPCIONES =====")
    print("1. Registrar orden")
    print("2. Ver fila")
    print("3. Ver estadísticas")
    print("4. Reiniciar datos")
    print("5. Salir")
    print("============================\n")
    return leer_entero("Seleccione una opción (1-5): ", minimo=1, maximo=5)

def mostrar_inventario(solo_nombre: bool = False):
    print("\n===== INVENTARIO =====")
    for producto in productos.values():  
        if solo_nombre:
            print(f"ID: {producto['id']}, Nombre: {producto['nombre']}")
        else:
            print(f"ID: {producto['id']}, Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")

mostrar_inventario(True)