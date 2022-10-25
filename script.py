#Importo librerias necesarias para hacer web scraping

from bs4 import BeautifulSoup
import requests

## Script para conectarnos  a la fuente de datos

web = "https://www.musimundo.com/informatica/notebook/c/98" # Esta es la web de donde vamos a sacar los datos

respuesta = requests.get(web)   # Todo lo que se extrajo se guarda en la variable respuesta

contenido = respuesta.text  # El contenido de respuesta se transforma a texto y se guarda en contenido

## Ahora empezamos a usar BS4

soup = BeautifulSoup(contenido, 'lxml')  ## Se parsean los datos

soup_pretty = soup.prettify()

print(soup_pretty) ## Todo listo para mostrar en formato HTML para luego sacar los datos que nos interesan

## Fin del script