menu = "0"

while menu == "0":
    menu = input("Elige una opción a continuación:")
    print("Operaciones")
    print("S. Suma")
    print("R. Resta")
    print("M. Multiplicacion")
    print("D. Division")
    print("A. Salir")

if menu == "S":
    num1 = ("Ingrese el numero 1:\n")
    num2 = ("Ingrese el numero 2:\n")
    resultado = num1 + num2
    print(f"La suma es {resultado}")

if menu == "R":
    num1 = ("Ingrese el numero 1:\n")
    num2 = ("Ingrese el numero 2:\n")
    resultado = num1 - num2
    print(f"La resta es {resultado}")
    
if menu == "M":
    num1 = ("Ingrese el numero 1:\n")
    num2 = ("Ingrese el numero 2:\n")
    resultado = num1 * num2
    print(f"La multiplicación es {resultado}")

if menu == "D":
    num1 = ("Ingrese el numero 1:\n")
    num2 = ("Ingrese el numero 2:\n")
    resultado = num1 / num2
    print(f"La división es {resultado}")

else:
    menu = "0"



