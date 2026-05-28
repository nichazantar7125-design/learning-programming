palabra = input("Ingrese la palabra secreta: ").lower()

vidas = 6
letras_adivinadas = []

while vidas > 0:

    progreso = ""

    for letra in palabra:
        if letra in letras_adivinadas:
            progreso += letra + " "
        else:
            progreso += "_ "

    print("\nPalabra:", progreso)
    print("Vidas:", vidas)

    if "_" not in progreso:
        print("¡Ganaste!")
        break

    intento = input("Ingrese una letra: ").lower()

    if intento in palabra:
        print("¡Correcto!")
        letras_adivinadas.append(intento)
    else:
        print("Incorrecto")
        vidas -= 1

if vidas == 0:
    print("Perdiste. La palabra era:", palabra)