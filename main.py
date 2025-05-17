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