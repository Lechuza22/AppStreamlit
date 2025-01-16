import streamlit as st

# Función de recomendaciones de ejemplo
def obtener_recomendaciones(usuario_id, num_recomendaciones=5):
    # Aquí va tu lógica de recomendaciones
    recomendaciones = [
        f"Recomendación {i + 1} para el usuario {usuario_id}"
        for i in range(num_recomendaciones)
    ]
    return recomendaciones

# Interfaz de Streamlit
st.title("Sistema de Recomendaciones")
st.subheader("Ingresa los datos para obtener recomendaciones")

# Entrada del usuario
usuario_id = st.text_input("ID del usuario:")
num_recomendaciones = st.slider(
    "Número de recomendaciones:",
    min_value=1,
    max_value=10,
    value=5,
)

# Botón para generar recomendaciones
if st.button("Obtener recomendaciones"):
    if usuario_id:
        recomendaciones = obtener_recomendaciones(usuario_id, num_recomendaciones)
        st.write("### Tus recomendaciones:")
        for rec in recomendaciones:
            st.write(f"- {rec}")
    else:
        st.warning("Por favor, ingresa un ID de usuario válido.")
