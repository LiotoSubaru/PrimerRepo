#Escribir un programa que pida al usuario 2 numeros enteros y calcular la suma desde el numero 1 hasta el numero 2.
#Imprimir el resultado de la suma

suma = 0
num1 = int(input("Dame un numero:\n"))
num2 = int(input("Dame otro numero:\n"))
num2 = num2 + 1

for num in range(num1,num2):
    suma += num
    
print(suma)