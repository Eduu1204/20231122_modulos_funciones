def obtener_numero():
    while True:
        try:
            entrada = input("Ingrese un número (o 'q' para salir): ")
            if entrada.lower() == 'q':
                return None
            else:
                numero = float(entrada)
                return numero
        except ValueError:
            print("Error: Ingrese un número válido.")


def calcular_suma(numeros):
    return sum(numeros)


def main():
    print("Ingrese hasta 5 números para calcular su suma.")

    numeros = []
    for _ in range(5):
        numero = obtener_numero()
        if numero is not None:
            numeros.append(numero)
        else:
            break

    suma = calcular_suma(numeros)
    print(f"La suma de los números ingresados es: {suma}")


if __name__ == "__main__":
    main()
