#Importo librerias necesarias para hacer web scraping

from bs4 import BeautifulSoup
import requests

## Script para conectarnos  a la fuente de datos

web = "https://www.musimundo.com/informatica/notebook/c/98" # Esta es la web de donde vamos a sacar los datos



respuesta = requests.get(web)   # Todo lo que se extrajo se guarda en la variable respuestanuestro_headers ={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/21.0'} # Se agrega un "User Agent"

contenido = respuesta.text  # El contenido de respuesta se transforma a texto y se guarda en contenido

## Ahora empezamos a usar BS4

soup = BeautifulSoup(contenido, 'html.parser')  ## Se parsean los datos

soup_pretty = soup.prettify()

print(soup_pretty) ## Todo listo para mostrar en formato HTML para luego sacar los datos que nos interesan


titulo = soup.find_all('h3', class_='mus-pro-name')#Aqui por se estraen y se convierten en datos puro los nombres de las notebook

title=[]  


for i in titulo:
    title.append(i.text.strip()) #Se utiliza un ciclo for para crear un lista que traiga todos los nombre de la notebook de la página.

po=soup.find_all('span', class_='mus-pro-price-number')

precio=[]

for pre in po:
    precio.append(pre.text.strip())#Se utiliza un ciclo for para crear un lista que traiga todos los precios de la notebook de la página.
    
print(title)    
print(precio)

import pandas as pd


df = pd.DataFrame({'            Descripcion': title, 'Precio   ': precio},index=list(range(0, 21)))#con la libreria pandas se forma un diccionario y se muesta los dato en forma de tabla
print(df)

df.to_csv('notebook.csv', index= True)#Por ultimo se crea un archivo CSV.