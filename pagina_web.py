import streamlit as st  #Importamos Streamlit: esta biblioteca de Python facilita la creación y visualización de páginas web interactivas 
import pandas as pd  #Importamos Pandas: esta biblioteca sirve para el análisis de datos tabulados en Python
import csv  #Este comando sirve para leer y escribir archivos CSV 
import os #Esta biblioteca proporciona una interfaz para interactuar con el sistema operativo (manipulación de rutas, la creación y eliminación de directorios, y la obtención de información sobre archivos)
from PIL import Image #Es una clase dentro de la biblioteca Pillow que proporciona funcionalidades para trabajar con imágenes
import fitz

# Con formato de Markdown centramos y agrandamos la letra del título de la web en streamlit
st.markdown("<h1 style='text-align: center; color: dark blue;'>Paratextos del siglo XVII</h1>", unsafe_allow_html=True)

# Nombramos al archivo de la imagen de Zoila y Team Zoila
imagen_inca = "inca.jpg"
imagen_calderon = "calderon.jpg"
imagen_siguenza = "siguenza.jpg"

texto = """
Escogimos los paratextos de estas obras (La aurora en Copacabana de Pedro Calderón de la Barca; 
El teatro de virtudes políticas de Carlos de Sigüenza y Góngora; y los Comentarios reales de 
los Incas del Inca Garcilaso de la Vega). En primer lugar, decidimos enfocarnos en secciones cortas 
de los textos. En segundo lugar, buscamos comparar el registro del español escrito en tres distintas 
zonas hispanoparlantes en el siglo XVII, tomando como muestra a personajes reconocidos por su manejo 
de la escritura.
"""

# Definimos la tipografía deseada ('Courier New')
tipografia = "Arial, sans-serif"

# Definimos el tamaño de la fuente, justificación y color
estilo_personalizado = f"""
    <div style="font-family: {tipografia}; font-size: 20px; text-align: justify; color: dark blue;">
        {texto}
"""

# Mostramos el texto con la tipografía personalizada
st.markdown(estilo_personalizado, unsafe_allow_html=True)

# Función para leer archivos PDF
def read_pdf(file_path):
    try:
        doc = fitz.open(file_path)
        text = ""
        for page_num in range(doc.page_count):
            page = doc[page_num]
            text += page.get_text()
        doc.close()
        return text
    except Exception as e:
        st.error(f"Error al leer el archivo PDF: {e}")
        return ""

# Ruta al directorio de documentos PDF
pdf_directory = "C://Users//Luisa//Desktop//Transkribus"

# Obtener la lista de archivos PDF en el directorio
pdf_files = [f for f in os.listdir(pdf_directory) if f.endswith(".pdf")]

# Selección del archivo PDF
selected_pdf = st.selectbox("Selecciona un archivo PDF", pdf_files)

# Ruta completa del archivo PDF seleccionado
pdf_path = os.path.join(pdf_directory, selected_pdf)

# Mostrar el nombre del archivo seleccionado
st.write(f"Archivo PDF seleccionado: {selected_pdf}")

# Leer el contenido del archivo PDF
pdf_text = read_pdf(pdf_path)

# Mostrar el contenido en Streamlit
st.subheader("Contenido del PDF:")
st.text(pdf_text)

# Texto sobre las grafías utilizadas en la escritura
st.markdown("## *Comentarios reales* del Inca Garcilaso de la Vega:")
st.write("- Y, yo, ya, después no usa la grafía “y”, sino la i. Por ejemplo, en *reyes, leyes, leyere, cuyos, muy, hay, soy, ley escribe reies, leies, leiere, cuios, mui, ai, soi, lei* respectivamente.")
st.write("- No hay intercambio entre las grafías “u” y “v”, ambas responden a sus sonidos respectivos a excepción del sonido [u] al inicio de palabra, para lo cual se utiliza la grafía “v”. La única excepción es cuando utiliza la grafía “v” para escribir Jesús, que lo termina escribiendo *Jesvs*.")
st.write("- Utiliza la grafía “s” (la letra actualmente utilizada) cuando aparece el sonido [s] al final de la palabra; cuando el mismo sonido aparece al inicio o en el medio de la palabra, tiende a utilizar la otra grafía de la “s” (la “s” larga). No obstante, hay un caso que llama la atención y es cuando escribe islas, pues lo escribe tal cual, con las dos letras “s” regulares.")

# Mostramos la imagen 
st.image(imagen_inca, caption="Portada de Comentarios reales", use_column_width=True)

# Texto sobre las grafías utilizadas en la escritura
st.markdown("## *La aurora en Copacabana* de Calderón de la Barca:")
st.write("- Con Avellaneda, la “u” representa el sonido [v] entre palabras, mientras que la “v” aparece cuando la palabra inicia con el sonido [u] como en Auellaneda en vez de “Avellaneda”) o vn en vez de “un”.")
st.write("- Escribe “buelos” en vez de “vuelos” lo que puede hacer pensar que tanto la [b] como la [v] se representa con “b”. Sin embargo, vanidad sí está bien escrito, con la “v”, lo que nos puede indicar que hay diferencia entre “b” y “v”, pero no sabemos si es cuestión tan solo gráfica u oral.")
st.write("- Las palabras valentía y veneraciones también están bien escritas. Pero también aparece breves escrita “breues”.")
st.write("- “Dissipar” la primera s era la larga, mientras que la segunda era la regular. Sin embargo, en “passos” y “assombro” las “s” estaban ambas representadas con el símbolo largo.")

# Mostramos la imagen 
st.image(imagen_calderon, caption="Portada de La aurora en Copacabana", use_column_width=True)

# Texto sobre las grafías utilizadas en la escritura
st.markdown("## *El teatro de virtudes políticas* de Sigüenza y Góngora:")
st.write("- Parece que Sigüenza tan solo utiliza la grafía “s” cuando el sonido [s] se encuentra al final de palabra. Las dobles “s” siempre van con la grafía extraña, ambas.")
st.write("- Aparece “oy” cuando hay un sonido [oj] junto, por ejemplo, en las palabras *hoy* y *heroicas* (escritas *oy* y *heroycas*), aquí tan solo hay dos ocurrencias.")
st.write("- “De el” separa la preposición del artículo, pero solo hay una ocurrencia, por lo que no podemos deducir mucho.")
st.write("- Cada vez que el sonido labial aparece antes de una consonante, se utiliza la “b” (celebrar, sublime, nobleza, obtenerlo).")
st.write("- La “v” parece que se presenta antes de vocal. Sin embargo, escribe también *Nobilissima, debiles y beneficio*, además del apellido *Ribera* del propio marqués.")

# Mostramos la imagen
st.image(imagen_siguenza, caption="Portada de El teatro de virtudes políticas", use_column_width=True)