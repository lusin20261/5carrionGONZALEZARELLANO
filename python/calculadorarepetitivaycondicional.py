print ("==============================")
print ("CALCULADORA DE LA MARCA PAJARO")
print ("==============================")

while True:
    print("")
    print("¿Que operacion quieres hacer?")
    print("a) Sumar")
    print("b) Restar")
    print("c) Multiplicacion")
    print("d) Division")
    print("e) Salir")

    opcion = input ("Elige una opcion: ")

    if opcion == "a":
        num1 = input ("Ingresa el primer numero: ")
        num1 = int (num1)
        num2 = input ("Ingresa el segundo numero:")
        num2 = int (num2)
        print("El resultado de la suma es", num1+num2 )

    elif opcion == "b":
        num1 = input ("Ingresa el primer numero:")
        num1 = int (num1)
        num2 = input ("Ingresa el segundo numero:")
        num2 = int (num2)
        print ("El resultado de la resta es:", num1-num2)

    elif opcion == "c":
        num1 = input ("Ingresa el primer numero:")
        num1 = int (num1)
        num2 = input ("Ingresa el segundo numero")
        num2 = int (num2)
        print ("el resultado de la multiplicacion es:", num1*num2)

    elif opcion == "d":
        num1 = input ("Ingresa el primer numero:")
        num1 = int (num1)