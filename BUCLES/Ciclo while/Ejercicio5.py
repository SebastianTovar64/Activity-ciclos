#Crear un programa que permita al usuario ingresar los valores totales de n facturas (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.
total = 0
monto = float(input("Ingrese el monto de la factura (Ingrese 0 para finalizar): "))
while monto != 0:
    total += monto
    monto = float(input("Ingrese el monto de la siguiente factura (Ingrese 0 para finalizar): "))
if total > 1000:
    descuento = total * 0.1
    total -= descuento
    print(f"El total a pagar es: {total} con un descuento del 10% por haber superado los $1000 en ventas.")
else:
    print(f"El total a pagar es: {total}")
