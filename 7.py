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
