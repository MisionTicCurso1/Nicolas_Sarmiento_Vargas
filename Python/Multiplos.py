#Ejercicio para calcular si un numero es multiplo de otro

#Definir la funcion que calcula si a es multiplo de b
def Multiplo(a, b):
    if a%b == 0:
        print(f"{a} es multiplo de {b}")
    else:
        print(f"{a} NO es multiplo de {b}")

print("Programa para evaluar si el primer numero es multiplo del segundo...")

#Llamamos la funcion
Multiplo(int(input("Ingrese el primer numero: ")),int(input("Ingrese el segundo numero: ")))