#ejercicio que calcula el IMC y lo clasifica

print("Programa para calcular el IMC y lo clasifica")

M= float(input("Ingrese por favor su masa en KG: "))
H= float(input("Ingrese su altura por favor en M: "))


IMC=(M/(H**2))

if IMC <18.5:
    print(f"su IMC es: {IMC} clasificado como peso bajo")
if IMC >= 18.5 and IMC <= 24.9:
    print(f"su IMC es: {IMC} clasificado como peso normal")
if IMC>= 25 and IMC <= 29.9:
    print(f"su IMC es: {IMC} clasificado como sobrepeso")
if IMC >= 30 and IMC <= 34.9:
    print(f"su IMC es: {IMC} clasificado como obesidad tipo I")
if IMC >= 35 and IMC <=39.9:
    print(f"su IMC es: {IMC} clasificado como obesidad tipo II")
if IMC >=40:
    print(f"su IMC es: {IMC} clasificado como obesidad tipo III")

print("Cuida tu salud :)")