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
