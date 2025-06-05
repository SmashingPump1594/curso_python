    # Este bloque solicita al usuario su nombre y lo saluda.
print("Bienvenido al programa multifunciones.")
print("Cual es tu nombre?")
nombre = input("Por favor, ingresa tu nombre: ")
print(f"Hola, {nombre}. Bienvenido al programa.")

    # Aqui te pedira que tarea quieres realizar.
print("A continuación, te mostraremos las opciones disponibles.")
print("1. Calculadora")
print("2. Dibujar estrella")
print("3. Lista de compras")

opcion = int(input("Por favor, selecciona una opción (1-3): "))
if opcion == 1:
     # Este bloque imprime las opciones matematicas que puede realizar.
    print(f"Hola, {nombre}, selecciona una opción usuario")
    print("1. Calcular área y perímetro de un círculo")
    print("2. Dividir dos números")
    print("3. Sumar dos números")
    print("4. Restar dos números")
    print("5. Multiplicar dos números")
    print("6. Identificar si un número es primo")
    print("7. Salir")

    opcion = int(input("Por favor, selecciona una opción: "))
    import math

    if opcion == 1:
        # Este bloque calcula el área y el perímetro de un círculo dado su radio.
        radio = float(input("Por favor, ingresa el radio del círculo: "))
        area = math.pi * radio**2
        circunferencia = 2 * math.pi * radio

        print(f"El área del círculo es: {area}")
        print(f"El perímetro del círculo es: {circunferencia}")

    elif opcion == 2:
        # Este bloque divide dos números.
        num1 = float(input("Por favor, ingresa el primer número: "))
        num2 = float(input("Por favor, ingresa el segundo número: "))
        if num2 != 0:
            resultado = num1 / num2
            print(f"El resultado de la división es: {resultado}")
        else:
            print("Error: No se puede dividir entre cero.")

    elif opcion == 3:
        # Este bloque suma dos números.
        num1 = float(input("Por favor, ingresa el primer número: "))
        num2 = float(input("Por favor, ingresa el segundo número: "))
        resultado = num1 + num2
        print(f"El resultado de la suma es: {resultado}")
    
    elif opcion == 4:
        # Este bloque resta dos números.
        num1 = float(input("Por favor, ingresa el primer número: "))
        num2 = float(input("Por favor, ingresa el segundo número: "))
        resultado = num1 - num2
        print(f"El resultado de la resta es: {resultado}")
    
    elif opcion == 5:
        # Este bloque multiplica dos números.
        num1 = float(input("Por favor, ingresa el primer número: "))
        num2 = float(input("Por favor, ingresa el segundo número: "))
        resultado = num1 * num2
        print(f"El resultado de la multiplicación es: {resultado}")

    elif opcion == 6:
        # Este bloque identifica si un número es primo.
        def num_primo(numero):
            if numero <= 1:
                return False
            for inicial in range(2, int(numero**0.5) + 1):
                if numero % inicial == 0:
                    return False
            return True

        numero = int(input("Ingresa un número: "))
        if num_primo(numero):
            print(f"El número {numero} es primo.")
        else:
            print(f"El número {numero} no es primo.")

    elif opcion == 7:
        print("Gracias por usar el programa. ¡Hasta luego!")
    else:
        print("Opción no válida.")

elif opcion == 2:
    # Este bloque dibuja una estrella de David.
    def estrella(numero):

        for i in range(numero):
            if i != numero - 1:
                print(" " * i + "*" + " " * (numero - 2 - i) + "*" + " " * (numero - 2 - i) + "*")
            else:
                print(" " * (numero - 1) + "*")

        n = numero
        for i in range(numero - 1):
            print(" " * (n - 2 - i) + "*" + " " * i + "*" + " " * i + "*")


    tamaño = int(input("Ingresa el tamaño de la estrella de David: "))
    estrella(tamaño)

elif opcion == 3:
    # Este bloque crea una lista de compras.
    lista_compras = []

    while True:
        item = input("Ingresa un artículo para la lista de compras (o escribe 'salir' para terminar): ")
        if item.lower() == 'salir':
            break
        lista_compras.append(item)

    print("Tu lista de compras es:")
    for i, item in enumerate(lista_compras, start=1):
        print(f"{i}. {item}")