import os
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import messagebox
from tkinter.ttk import Style
import re
import logging
from colorama import Fore, Style, init

def buscar_texto_en_archivos(carpeta, palabras_buscar):
    archivos_encontrados = []
    tipos_archivo_buscar = ['.php', '.js', '.html', '.json', '.ini', '.css']

    # Escapar caracteres especiales en cada palabra buscada
    palabras_buscar_regex = [re.escape(palabra) for palabra in palabras_buscar]

    # Crear una expresión regular que buscará todas las palabras
    texto_buscar_regex = re.compile(r"|".join(palabras_buscar_regex), re.IGNORECASE)

    # Configurar el sistema de logs con color
    init(autoreset=True)  # Inicializar colorama
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger('buscador_log')

    # Recorre todos los archivos en la carpeta y sus subcarpetas
    for ruta_actual, carpetas, archivos in os.walk(carpeta):
        # Excluye ciertas carpetas si es necesario
        # Por ejemplo, si deseas excluir la carpeta 'excluir_carpeta':
        # if 'excluir_carpeta' in carpetas:
        #     carpetas.remove('excluir_carpeta')

        for archivo in archivos:
            # Comprueba si el archivo tiene una extensión de archivo válida
            if any(archivo.endswith(extension) for extension in tipos_archivo_buscar):
                ruta_completa = os.path.join(ruta_actual, archivo)

                try:
                    # Lee el contenido del archivo
                    with open(ruta_completa, 'r', encoding='utf-8') as archivo_contenido:
                        contenido = archivo_contenido.read().lower()  # Convierte el contenido a minúsculas
                        
                        # Imprime las palabras que se están buscando en el archivo actual
                        logger.info(f"{Fore.RED}Buscando palabras en el archivo: {ruta_completa} - Palabras: {', '.join(palabras_buscar)}")

                        # Busca todas las palabras en el contenido utilizando la expresión regular
                        resultados = texto_buscar_regex.finditer(contenido)
                        for resultado in resultados:
                            archivos_encontrados.append((ruta_completa, resultado.group()))

                            # Imprime el resultado con la palabra encontrada en amarillo
                            resultado_coloreado = re.sub(resultado.group(), f"{Fore.YELLOW}{resultado.group()}{Fore.WHITE}", resultado.group())
                            logger.info(f"{Fore.WHITE}{Style.BRIGHT}Texto encontrado en el archivo: {ruta_completa} - Palabra encontrada: {resultado_coloreado}")
                except Exception as e:
                    logger.error(f"{Fore.RED}Error al abrir el archivo {ruta_completa}: {e}")

    return archivos_encontrados

def obtener_palabras_buscadas():
    # Obtener las palabras a buscar utilizando un cuadro de diálogo
    palabras_buscadas = simpledialog.askstring("Codewords v1.2 by @FreddyDeveloper", "Ingrese las palabras que desea buscar en el código separadas por comas:")

    if not palabras_buscadas:
        messagebox.showwarning("Advertencia", "No se ingresaron palabras de búsqueda.")
        return None

    # Convertir las palabras ingresadas en una lista
    palabras_buscadas = [palabra.strip() for palabra in palabras_buscadas.split(",")]
    return palabras_buscadas

# Crear una ventana de Tkinter para que el usuario seleccione la carpeta de búsqueda
app = tk.Tk()
app.withdraw()  # Oculta la ventana principal

# Obtener las palabras a buscar
palabras_buscadas = obtener_palabras_buscadas()

if palabras_buscadas is None:
    messagebox.showwarning("Advertencia", "No se ingresaron palabras de búsqueda. Saliendo...")
else:
    # Seleccionar la carpeta de búsqueda
    carpeta_seleccionada = filedialog.askdirectory(title="Selecciona una carpeta para iniciar la búsqueda:")

    if not carpeta_seleccionada:
        messagebox.showwarning("Advertencia", "No se ha seleccionado ninguna carpeta. Saliendo...")
    else:
        # Llamar a la función para buscar las palabras en los archivos
        archivos_encontrados = buscar_texto_en_archivos(carpeta_seleccionada, palabras_buscadas)

        # Imprime los resultados en colores y formato personalizados
        if archivos_encontrados:
            print(f"{Fore.GREEN}{Style.BRIGHT}Texto encontrado en los siguientes archivos:")
            for ruta_completa, palabra_encontrada in archivos_encontrados:
                print(f"{Fore.GREEN}{Style.BRIGHT}{ruta_completa}")
                print(f"{Fore.YELLOW}{Style.BRIGHT}Palabra encontrada: {palabra_encontrada}{Fore.WHITE}")
        else:
            print(f"{Fore.RED}{Style.BRIGHT}Texto no encontrado en ningún archivo.")