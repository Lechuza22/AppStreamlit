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
    
    st.write (1+2)
    ## caja de seleccion. 
    opcion = st.selectbox("Elije tu fruta", ["manzana", "naranja", "Platano", "Freza"])
    st.write(f"Tu fruta faborita es: {opcion}")
    
    ## multi select
    opciones = st.multiselect("Selecciona tu color favorito", ["Rojo", "Azul", "Amarillo", "Negro", "Blanco"])
    st.write("Tus colores favoritos son:", opciones)
    ## Slider
    Edad = st.slider(
        "Selecciona tu edad",
        min_value=0,
        Max_value=110,
        value=25, #valor inicial
        step=1)
    st.write("Tu edad es", Edad)







if __name__== '__main__':
    main()
