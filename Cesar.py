#Jorge Rodrigo Torres Ochoa
#Programa de cifrado y descifrado
#23/10/20 - 20:16
abc = "abcdefghijklmnopqrstuvwxyz"
numeros = "0123456789"
puntuacion = ".,:;-_"
def cifrar(cadena, clave):
    textocif = ''
    for letra in cadena:
        if letra == " ":
            textocif = textocif + str(" ")
        elif letra in puntuacion:
            textocif = textocif + letra
        else:
            if letra in numeros:
                suma = numeros.find(letra) + clave 
                modulo = int(suma) % len(numeros)
                textocif = textocif + str(numeros[modulo])
            else:
                suma = abc.find(letra) + clave 
                modulo = int(suma) % len(abc)
                textocif = textocif + str(abc[modulo])
    return textocif
def descifrar(cadena, clave):
    textocif = ''
    for letra in cadena:
        if letra == " ":
            textocif = textocif + str(" ")
        elif letra in puntuacion:
            textocif = textocif + letra
        else:
            if letra in numeros:
                suma = numeros.find(letra) - clave 
                modulo = int(suma) % len(numeros)
                textocif = textocif + str(numeros[modulo])
            else:
                suma = abc.find(letra) - clave 
                modulo = int(suma) % len(abc)
                textocif = textocif + str(abc[modulo])
    return textocif
def main():
    while True:
        modo = input("¿Qué modo deseas usar?¿cifrado o descifrado?:\n").lower()
        if modo == "cifrado":
            cad = str(input("Cadena a cifrar: ")).lower()
            num = int(input("Clave numerica: "))
            print(cifrar(cad, num))
            break
        elif modo == "descifrado":
            cadc = str(input("Cadena a descifrar: ")).lower()
            cnum = int(input("Clave numerica: "))
            print(descifrar(cadc, cnum))
            break
        else:
            print("Modo no valido")

if __name__ == "__main__":
    main()