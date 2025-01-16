import streamlit as st

def main():
    st.title("Curso de streamlit")
    st.header ("Encabezado")
    st.subheader ("subencabezado")
    st.text ("Aca se pone texto")
    nombre = "Jero"    
    st.text(f"Hola {nombre}, esto es una prueba")
    st.markdown ("### Esto es un Markdown") 
    
    st.success("Esto es un exito")
    st.warning("Esto es una advertencia")
    st.info("Esto da información")
    st.error ("Esto es un error")
    st.exception("Esto es una excepción")
               
if __name__== '__main__':
    main()
