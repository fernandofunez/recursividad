def suma_naturales(num):
    if num <=1:
        return 1
    else:
        return num + suma_naturales(num - 1) 
num = int(input("ingrese un numero :"))
resultado = suma_naturales(num)
print("la sumas de los numeros naturales es:", resultado)