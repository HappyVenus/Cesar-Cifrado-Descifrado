#Jorge Rodrigo Torres Ochoa
#Descifrado a fuerza bruta
#23/10/20 - 20:16
simbolos = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
def cifrar(cadena, clave):
    textocif = ''
    for letra in cadena:
        if letra == " ":
            textocif = textocif + str(" ")
        else:    
            suma = simbolos.find(letra) + clave 
            modulo = int(suma) % len(simbolos)
            textocif = textocif + str(simbolos[modulo])
    return textocif
def descifrar(cadena, clave):
    textocif = ''
    for letra in cadena:
        if letra == " ":
            textocif = textocif + str(" ")
        else:
            suma = simbolos.find(letra) - clave 
            modulo = int(suma) % len(simbolos)
            textocif = textocif + str(simbolos[modulo])
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
            for i in range(len(simbolos)):
                cnum = i
                print("llave #", i, descifrar(cadc, cnum))
            break
        else:
            print("Modo no valido")

if __name__ == "__main__":
    main()