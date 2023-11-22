from datetime import datetime


def obtener_valor(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor >= 0:
                return valor
            else:
                print("Error: Ingrese un valor válido mayor o igual a cero.")
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")


def calcular_descuento(subtotal, fecha):
    # Obtener el día actual
    hoy = datetime.now().day

    # Aplicar descuento del 5% si el día es anterior al 15 de cada mes
    if hoy < 15:
        descuento = subtotal * 0.05
        return descuento
    else:
        return 0


def calcular_total(subtotal, descuento):
    return subtotal - descuento


def main():
    print("Ingrese los datos para calcular la factura:")

    unidades = obtener_valor("Ingrese la cantidad de unidades: ")
    precio = obtener_valor("Ingrese el precio por unidad: ")

    subtotal = unidades * precio
    descuento = calcular_descuento(subtotal, datetime.now())
    total = calcular_total(subtotal, descuento)

    print(f"\nSubtotal: ${subtotal:.2f}")
    print(f"Descuento: ${descuento:.2f}")
    print(f"Total: ${total:.2f}")


if __name__ == "__main__":
    main()
