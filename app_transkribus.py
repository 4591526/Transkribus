import streamlit as st
import pandas as pd
import csv
import os
from PIL import Image
import fitz

# ...

# Ruta al directorio de documentos PDF
pdf_directory = "C://Users//u_humanidades//Desktop//Transkribus//documentos"

# Obtener la lista de archivos PDF en el directorio
pdf_files = [f for f in os.listdir(pdf_directory) if f.endswith(".pdf")]

# Mostrar el título de la web
st.markdown("<h1 style='text-align: center; color: dark blue;'>Paratextos del siglo XVII</h1>", unsafe_allow_html=True)

# Resto del código ...

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