import copy

plantilla_producto = {
    "id": None,
    "nombre": "",
    "precio": 0,
    "cantidad": 0
}
ventas: dict[int, dict] = {}

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
productos = copy.deepcopy(productos_base)


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



def mostrar_inventario(solo_nombre: bool = False):
    print("\n===== INVENTARIO =====")
    for producto in productos.values():  
        if solo_nombre:
            print(f"ID: {producto['id']}, Nombre: {producto['nombre']}")
        else:
            print(f"ID: {producto['id']}, Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")

def agregar_producto():
    print("\n=== Agregar nuevo producto ===")
    nombre = input("Ingrese el nombre del producto: ").strip()
    precio = leer_entero("Ingrese el precio del producto: ", minimo=1)
    cantidad = leer_entero("Ingrese la cantidad del producto: ", minimo=1)


    nuevo_id = max(productos.keys(), default=0) + 1

    nuevo_producto = {
        **plantilla_producto,
        "id": nuevo_id,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    productos[nuevo_id] = nuevo_producto
    print(f"\nProducto '{nombre}' agregado exitosamente con ID {nuevo_id}.")
    
def retirar_producto():
    print("\n=== Retirar una unidad de un producto ===")
    if not productos:
        print("No hay productos en el inventario.")
        return

    mostrar_inventario()
    id_producto = leer_entero("Ingrese el ID del producto del cual desea retirar una unidad: ")

    if id_producto in productos:
        producto = productos[id_producto]
        nombre = producto["nombre"]
        precio = producto["precio"]

        if producto["cantidad"] > 0:
            producto["cantidad"] -= 1
            print(f"Se retiró una unidad de '{nombre}'. Cantidad restante: {producto['cantidad']}")

            id_venta = max(ventas.keys(), default=0) + 1
            ventas[id_venta] = {
                "id": id_venta,
                "nombre": nombre,
                "cantidad_vendida": 1,
                "ganancia": precio
            }

            if producto["cantidad"] == 0:
                print(f"Advertencia: No quedan unidades de '{nombre}' en el inventario.")
        else:
            print(f"No se puede retirar '{nombre}': no hay unidades disponibles.")
    else:
        print("ID no válido. No se encontró ningún producto con ese ID.")
def mostrar_ventas():
    print("\n=== REGISTRO DE VENTAS ===")
    if not ventas:
        print("No se han registrado ventas todavía.")
        return

    for venta in ventas.values():
        print(f"ID: {venta['id']}, Producto: {venta['nombre']}, Cantidad vendida: {venta['cantidad_vendida']}, Ganancia: ${venta['ganancia']}")

def mostrar_ganancia_global():
    print("\n=== GANANCIA GLOBAL ===")
    if not ventas:
        print("No hay ventas registradas todavía.")
        return

    total_ganancia = sum(venta["ganancia"] for venta in ventas.values())
    print(f"La ganancia total hasta el momento es: ${total_ganancia}")

def adicionar_unidades():
    print("\n=== Añadir unidades a un producto ===")
    if not productos:
        print("No hay productos en el inventario.")
        return

    mostrar_inventario(solo_nombre=True)
    
    id_producto = leer_entero("Ingrese el ID del producto al que desea añadir unidades: ")
    if id_producto not in productos:
        print("ID no válido. No se encontró ningún producto con ese ID.")
        return

    unidades = leer_entero("¿Cuántas unidades desea añadir? ", minimo=1)

    producto = productos[id_producto]
    producto["cantidad"] += unidades
    print(f"Se añadieron {unidades} unidades a '{producto['nombre']}'. Nueva cantidad: {producto['cantidad']}")

def reiniciar_datos():
    global productos, ventas
    print("\n=== Reiniciando datos a valores de fábrica ===")
    
    productos.clear()
    productos.update(copy.deepcopy(productos_base))
    
    ventas.clear()
    
    print("Inventario y ventas reiniciados correctamente.")
def menu_principal():
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Retirar productos")
        print("2. Inventario")
        print("3. Informes")
        print("4. Configuración")
        print("5. Finalizar")
        print("==========================")
        opcion = leer_entero("Seleccione una opción (1-5): ", minimo=1, maximo=5)

        if opcion == 1:
            retirar_producto()
            if not continuar_o_salir(): break
        elif opcion == 2:
            if not menu_inventario(): break
        elif opcion == 3:
            if not menu_informes(): break
        elif opcion == 4:
            if not menu_configuracion(): break
        elif opcion == 5:
            print("Programa finalizado.")
            break

def continuar_o_salir() -> bool:
    print("\n¿Desea volver al menú principal o finalizar?")
    print("1. Volver al menú principal")
    print("2. Finalizar programa")
    opcion = leer_entero("Seleccione una opción (1-2): ", minimo=1, maximo=2)
    return opcion == 1  # True para continuar, False para salir

def menu_inventario():
    print("\n--- Submenú de Inventario ---")
    print("1. Añadir unidad de producto")
    print("2. Añadir un producto nuevo")
    print("3. Mostrar inventario actual")
    print("------------------------------")
    opcion = leer_entero("Seleccione una opción (1-3): ", minimo=1, maximo=3)

    if opcion == 1:
        adicionar_unidades()
    elif opcion == 2:
        agregar_producto()
    elif opcion == 3:
        mostrar_inventario()

    return continuar_o_salir()

def menu_informes():
    print("\n--- Submenú de Informes ---")
    print("1. Informe de ganancia")
    print("2. Informe de ventas")
    print("----------------------------")
    opcion = leer_entero("Seleccione una opción (1-2): ", minimo=1, maximo=2)

    if opcion == 1:
        mostrar_ganancia_global()
    elif opcion == 2:
        mostrar_ventas()

    return continuar_o_salir()

def menu_configuracion():
    print("\n--- Submenú de Configuración ---")
    print("1. Restaurar valores de fábrica")
    print("--------------------------------")
    opcion = leer_entero("Seleccione una opción (1): ", minimo=1, maximo=1)

    if opcion == 1:
        reiniciar_datos()

    return continuar_o_salir()
menu_principal()