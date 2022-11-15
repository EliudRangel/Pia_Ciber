import argparse
import logging
from Pia_Codigo import Web_Scrap, Hash, Scanner_Files, Metadata, Encabezado, Escaneo_Puertos

# Descripcion del formato logging

logging.basicConfig(filename = 'logging.log',
                    level = logging.INFO,
                    format = '%(asctime)s' "\t" '%(message)s',
                    datefmt = '%d/%m/%Y %I:%M:%S %p')

description = """
                    Ejemplo de uso:
                    + py Pia_Main.py -Menu Scrap --> Inicia WebScraping
                    + py Pia_Main.py -Menu Meta  --> Extrae Metadatos
                    + py Pia_Main.py -Menu Hash  --> Obtiene Hash de Archivos
                    + py Pia_Main.py -Menu Ports --> Escanea los Puertos
                    + py Pia_Main.py -Menu Scan ---> Escanea Virus de Archivo
                    + py Pia_Main.py -Menu Head ---> Obtiene Encabezados de Pagina"""

def Main():
    try:
        parser = argparse.ArgumentParser(description='PIA de CiberSeguridad', exit_on_error= False,
                                         epilog= description,add_help = True,
                                         formatter_class= argparse.RawDescriptionHelpFormatter)
        parser.add_argument("-Menu", choices=["Scrap","Meta","Hash","Head","Ports","Scan"],
                            help="Elige la tarea a realizar con las opciones validas")
    
        args = parser.parse_args()
        
        if args.Menu == "Scrap":
            Web_Scrap()
            
        if args.Menu == "Hash":
            Hash()    
            
        if args.Menu == "Scan":
            Scanner_Files()
            
        if args.Menu == "Meta":
            Metadata()
        
        if args.Menu == "Head":
           Encabezado() 
           
        if args.Menu == "Ports":
            Escaneo_Puertos()
            
    except argparse.ArgumentError:
        print("El argumento ingresado no existe, prueba -h para mas ayuda")
        logging.info("Se ingreso un argumento incorrecto")
        
if __name__ == '__main__':
    Main()