from bs4 import BeautifulSoup as bs
import requests
import os
import logging
import hashlib
import json
import exifread
from PyPDF2 import PdfFileReader
import feedparser
import subprocess


def Web_Scrap():
    print("Inicio de Web Scrap \n")
    
    def Url(url):
        try:
            page = requests.get(url)
            soup = bs(page.text, 'html.parser')
            images = soup.find_all('img')
            Carpeta(images)
        except requests.ConnectionError:
            print("Conectate a una red para funcionar")
            logging.info("Se genero error por falta de internet")
    def Carpeta(images):
        ruta = os.getcwd()
        if os.path.isdir(ruta + "\imagenes"):
            os.chdir(ruta+ "\imagenes")
            imagen(images)
            os.chdir("../")
            print("ya se descargaron las imagenes")
        else:
            os.mkdir("imagenes")
            os.chdir(ruta+ "\imagenes")
            imagen(images)
            os.chdir("../")
            print("ya se descargaron las imagenes")
            
    def imagen(images):
        count = 0
        print(f"{len(images)} imagenes encontradas")
        lista_img = []
        
        for elemento in images:
            recurso = elemento.get('src')
            if recurso == None:
                continue
            lista_img.append(recurso)
        
        x = 1
        for image in lista_img:
            with open("imagen_" + str(x) + ".jpg",'wb') as f:
                res = requests.get(image)
                f.write(res.content)
                f.close()
            x+=1
            count = count + 1 
        
        if count == len(images):
            print("Todas las imagenes fueron encontradas")
            
        else:
            print(f"{count} imagenes descargadas de {len(images)}")
        
        
    # Pagina para descargar imagenes
    url = "https://www.xataka.com.mx/fotografia-y-video/estas-23-increibles-fotografias-fueron-tomadas-smartphone-ganadoras-concurso-mobile-photo-awards-2019"
    Url(url)
    
    
def Hash():
    archivo = "cesar.py"
    name = archivo[:-4] + "_hash.txt"
    if os.path.isfile(name): 
        with open(archivo, 'rb') as f:
            contenido = f.read()
            hash_text = hashlib.sha512(contenido).hexdigest()
            f.close()
            with open(name, 'r') as b:
                valor = b.read()
            if hash_text == valor:
                print("Son iguales")
            else:
                print("No son iguales")
            b.close()
    else:
        try: 
            with open(archivo, 'rb') as f:
                contenido = f.read()
                hash_text = hashlib.sha512(contenido).hexdigest()
                f.close()
                with open(name, 'w') as m:
                    m.write(hash_text)
                    m.close()
                print("El archivo se ha creado")
        except FileNotFoundError:
            print("El Archivo o el nombre del archivo no existe")
            logging.info("Error por archivo inexistente")

def Scanner_Files():
    # Asignamos la url del api
    
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    file = "payload.pyw"

    
    # Abrimos el archivo donde esta la llave
    try:
        with open("Api.json") as f:
            Api = json.load(f)
    except FileNotFoundError:
        print("Agrega el archivo donde esta la llave ")
        logging.info("Error por no agregar archivo de la llave")
    # Brindamos la Apy key
    try:
        params = {'apikey': Api["key"]}
    except UnboundLocalError:
        print("Agrea el nombre correcto de la api")
        logging.info("Se agrego un nombre incorecto a la api")
    try:
        files = {'file': (file, open(file, 'rb'))}
    except FileNotFoundError:
        print("Agrega el archivo a escanear")
        logging.info("Error por no agregar archivo a escanear")
        
    try:
        response = requests.post(url, files=files, params=params)
        json_response = response.json()
    except UnboundLocalError:
        print("El archivo asignado no existe")
        logging.info("Error por archivo inexistente")
    try:
        with open("resultado.txt", "w") as b:
            b.write(str(json_response))
            b.close()
            print("Se ha creado el archivo")
    except UnboundLocalError:
        print("Favor de colocar correctamente el nombre")
        logging.info("Error por archivo inexistente")
        
      
def Metadata():
    print("Iniciando obtencion de metadata")
    
    def Imagen(file):
        try:
            imagen = file
            #abrimos la imagen en modo lectura binaria
            data = open(imagen, 'rb')
        except FileNotFoundError:
            print("Ingresa la imagen a verificar")
            logging.info("Error al no encontrar imagen")
        try:
            # Devuelve las etiquetas Exif
            tags = exifread.process_file(data)
            name = imagen[:-4]+"_reporte.txt"
            f = open(name,'w')
    
            for tag in tags.keys():
                if tag not in ('JPEGThumbnail'): 
                    f.write("\n "+ str(tag) + " = " + str(tags[tag]))
            f.close()
            print("Obtencion de metadatos de imagen completa")
        except UnboundLocalError:
            print("")
            logging.info("Error al no tener valor para procesar")

    
    def Pdf(file):
        try:
            with open(file, 'rb') as f:
                pdf = PdfFileReader(f)
                informacion = pdf.getDocumentInfo()
                numero_de_paginas = pdf.getNumPages()
        except FileNotFoundError:
            print("No se encontro el archivo pdf a investigar")
            logging.info("Error al no encontrar archivo pdf")
        try:
            txt = f"""
            Informacion de {file}:
        
            
            Autor: {informacion.author}
            Creador: {informacion.creator}
            Producido : {informacion.producer}
            Sujeto : {informacion.subject}
            Titulo : {informacion.title}
            Numero de paginas : {numero_de_paginas}
        
            """
            name = file[:-4] + "_reporte.txt"
            with open(name, 'w') as b:
                b.write(txt)
                b.close()
            f.close()
            print(f"Se creo el documento {name} con exito")
        except UnboundLocalError:
            print("")
            logging.info("Error al no tener valor para procesar")  
    
    # Se ejecutan las funciones con los archivos deseados  
    Imagen("Bisonte.jpg")
    Pdf("Actividad.pdf")
    
def Encabezado():
    # Asignamos la url con formato .rss o xml
    url = 'https://www.reddit.com/r/Python/.rss'
    # Declaramos que es lo que leera feedparser
    respuesta = feedparser.parse(url)
    with open("Encabezados.txt", 'w') as f:
        for post in respuesta.entries:
            f.write("\n"+ "Titulo: "+ post.title + "\n" + "Link: " + post.link 
                    + "\n" + "Fecha: " + post.updated + "\n" + "Autor: " + 
                    post.author + "\n" + "Usuario: " + post.id + "\n")
    f.close()
    print("Revision de encabezados terminada")
    

def Escaneo_Puertos():
    try:
        # Mandamos a llamar powershell con subprocess
        Puertos = "powershell -Executionpolicy ByPass -File Escaner_Puertos.ps1" 
        runningProcess = subprocess.check_output(Puertos)
    
        resultado = runningProcess.decode()
        f = open("res_Puertos.txt", 'w')
        f.write(resultado)
        f.close()
        print("El escaneo a terminado")
    except subprocess.CalledProcessError:
        print("Verifique que este bien escrito el proceso de subprocess")
        logging.info("Error al llamar powershell")
