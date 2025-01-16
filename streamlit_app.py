import streamlit as st

def main():
    st.title("Curso de streamlit")
    st.header ("Encabezado")
    st.subheader ("subencabezado")
    st.text ("Aca se pone texto")
    nombre = "Jero"    
    st.text(f"Hola {nombre}, esto es una prueba")
    st.markdown ("### Esto es un Markdown") 
if __name__== '__main__':
    main()
