import argparse


def main():
    description = """ Ejemplo de uso:
                    + Para encriptar:
                     -modo e -mensaje hola -clave 5
                    + Para desencriptar:
                     -modo d -mensaje 'encriptado' -clave 5
                    + Para crackeo
                     -modo c -mensaje 'encriptado' """

    parser = argparse.ArgumentParser(epilog=description ,
                                    formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-modo", help="Agrega 'e' para encriptar, 'd' para desencriptar o 'c' para crackear")
    parser.add_argument("-mensaje", help="Agrega el mensaje a encriptar, desencriptar o crackear")
    parser.add_argument("-clave", help="Agrega un numero para la clave", 
                         default="4")
    args = parser.parse_args()

    key = int(args.clave)
    argumento = args.mensaje

    if args.modo == "e":
        encriptar(argumento, key)
    
    if args.modo == "d":
        desencriptar(argumento, key)
    
    if args.modo == "c":
        hackeo(argumento)


#funcion encriptado de mensaje
def encriptar(mensaje, clave):
    Palabra = mensaje
    key = clave

    SIMBOLOS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    translated = ''

    for simbolo in Palabra:
    
        if simbolo in SIMBOLOS:
            symbolIndex = SIMBOLOS.find(simbolo)
            translatedIndex = symbolIndex + key
        
            if translatedIndex >= len(SIMBOLOS):
                translatedIndex = translatedIndex - len(SIMBOLOS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SIMBOLOS)

            translated = translated + SIMBOLOS[translatedIndex]
        else:
            
            translated = translated + simbolo

    print(translated)

def desencriptar(mensaje, clave):
    Palabra = mensaje
    key = clave

    SIMBOLOS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    translated = ''

    for simbolo in Palabra:
    
        if simbolo in SIMBOLOS:
            symbolIndex = SIMBOLOS.find(simbolo)
            translatedIndex = symbolIndex - key
        
            if translatedIndex >= len(SIMBOLOS):
                translatedIndex = translatedIndex - len(SIMBOLOS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SIMBOLOS)

            translated = translated + SIMBOLOS[translatedIndex]
        else:
            translated = translated + simbolo

    print(translated)

def hackeo(mensaje):
    Palabra = mensaje
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'


    for key in range(len(SYMBOLS)):
  
        translated = ''

        for symbol in Palabra:
            if symbol in SYMBOLS:
                symbolIndex = SYMBOLS.find(symbol)
                translatedIndex = symbolIndex - key

                if translatedIndex < 0:
                    translatedIndex = translatedIndex + len(SYMBOLS)

                translated = translated + SYMBOLS[translatedIndex]

            else:
           
                translated = translated + symbol

        print('Key #%s: %s' % (key, translated))

if __name__ == '__main__':            
    main()