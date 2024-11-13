from operaciones import suma, resta, multiplicacion, division

def main():
    while True:
        try:
            # Solicitar dos números al usuario
            numero1 = float(input("Introduce el primer número: "))
            numero2 = float(input("Introduce el segundo número: "))
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue

        # Solicitar el tipo de operación
        print("Operaciones disponibles:")
        print("1 - Suma")
        print("2 - Resta")
        print("3 - Multiplicación")
        print("4 - División")
        operacion = input("Selecciona el tipo de operación (1/2/3/4): ")

        # Ejecutar la operación seleccionada
        if operacion == "1":
            resultado = suma(numero1, numero2)
        elif operacion == "2":
            resultado = resta(numero1, numero2)
        elif operacion == "3":
            resultado = multiplicacion(numero1, numero2)
        elif operacion == "4":
            resultado = division(numero1, numero2)
        else:
            print("Operación no válida.")
            continue

        print(f"El resultado es: {resultado}")

        # Preguntar si el usuario quiere hacer otra operación
        continuar = input("¿Quieres hacer otra operación? (s/n): ").lower()
        if continuar != "s":
            print("Gracias por usar la calculadora. ¡Adiós!")
            break

if __name__ == "__main__":
    main()
