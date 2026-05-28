Proceso Ahorcado

    Definir palabra, letra, progreso Como Cadena
    Definir vidas, i, aciertos Como Entero
    Definir gano Como Logico

    Escribir "Ingrese la palabra secreta:"
    Leer palabra

    vidas <- 6
    aciertos <- 0
    gano <- Falso

    progreso <- ""

    Para i <- 1 Hasta Longitud(palabra)
        progreso <- progreso + "_ "
    FinPara

    Mientras vidas > 0 Y gano = Falso

        Escribir "Palabra: ", progreso
        Escribir "Vidas: ", vidas

        Escribir "Ingrese una letra:"
        Leer letra

        progreso <- ""

        Para i <- 1 Hasta Longitud(palabra)

            Si Subcadena(palabra, i, i) = letra Entonces
                progreso <- progreso + letra + " "
            SiNo
                progreso <- progreso + "_ "
            FinSi

        FinPara

        Si Buscar(letra, palabra) > 0 Entonces
            Escribir "¡Correcto!"
        SiNo
            Escribir "Incorrecto"
            vidas <- vidas - 1
        FinSi

        aciertos <- 0

        Para i <- 1 Hasta Longitud(palabra)

            Si Subcadena(progreso, (i*2)-1, (i*2)-1) = Subcadena(palabra, i, i) Entonces
                aciertos <- aciertos + 1
            FinSi

        FinPara

        Si aciertos = Longitud(palabra) Entonces
            gano <- Verdadero
        FinSi

    FinMientras

    Si gano Entonces
        Escribir "¡Ganaste!"
    SiNo
        Escribir "Perdiste. La palabra era: ", palabra
    FinSi

FinProceso