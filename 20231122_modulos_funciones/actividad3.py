def obtener_numero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Error: Ingrese un número entero válido.")


def generar_lista_pares(inicial, final):
    # Utilizando una función anónima (lambda) para obtener los números pares
    numeros_pares = list(filter(lambda x: x % 2 == 0, range(inicial, final + 1)))
    return numeros_pares


def main():
    print("Ingrese el rango de números para mostrar los pares:")

    numero_inicial = obtener_numero("Ingrese el número inicial: ")
    numero_final = obtener_numero("Ingrese el número final: ")

    # Controlar que el número final sea mayor o igual al número inicial
    while numero_final < numero_inicial:
        print("Error: El número final debe ser mayor o igual al número inicial.")
        numero_final = obtener_numero("Ingrese el número final: ")

    lista_pares = generar_lista_pares(numero_inicial, numero_final)

    print(f"\nNúmeros pares entre {numero_inicial} y {numero_final}:")
    print(lista_pares)


if __name__ == "__main__":
    main()
