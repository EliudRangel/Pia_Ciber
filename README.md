# Pia_Ciber
Los modulos necesarios para la correcta ejecucion es el siguiente:

beautifulsoup4 requests PyPDF2 feedparser ExifRead

Estos mismos modulos se pueden encontrar en requirements.txt

Conforme al script que esta conformado por diversas tareas independientemente una de la otra, las cuales son: WebScraping, Metadatos, Escaneo de Puertos, Obtencion de encabezados, Obtencion de claves hash, Escaneo de archivos.

Se Tienen 2 scripts con mayor jerarquia. El Pia_Main.py es el encargado de llamar a las funciones que estan escritas en el Pia_Codigo.py, donde se almacenan las tareas de seguridad, esto mediante argparse para ingresar los argumentos que se necesitan cuando queramos ejecutar el codigo.

Para poder ejecutar el codigo se debe de especificar el tipo de tarea que deseas realizar mediante un menu el cual es:

py Pia_Main.py -Menu Scrap la cual ejecutara la tarea de descargar imagenes.

py Pia_Main.py -Menu Hash para obtener las claves hash de un archivo

py Pia_Main.py -Menu Head para obtener los titulos e informacion de una pagina de noticias.

py Pia_Main.py -Menu Scan para escanear un archivo con la API de virus total

py Pia_Main.py -Menu Meta para obtener los metadatos de una imagen y un archivo pdf

py Pia_Main.py -Meta Ports para escanear los puertos de una ip asignada

Ademas de el uso del argumento -h para desplegar la ayuda necesaria la cual mostraria lo antes mencionado

No se debe olvidar que solo se pueden realizar esas tareas ya que se indica directamente en el argumento choices[] una lista de los argumentos obligatorios y aceptables que solo puede aceptar el argparse, si se llega a ingresar un argumento invalido se lanzara una excepcion que indicara que consulte el argumento -h

Utilidades: Todas las tareas generan un archivo .txt que guardara toda la informacion obtenida de las tareas que el usuario quiera ejecutar de esta manera no interactuamos directamente con el cmd, ademas de que si en algun punto el usuario llega a asignar informacion invalida a las tareas, se cuenta con las excepciones necesarias para indicarle al usuario donde se esta equivocando