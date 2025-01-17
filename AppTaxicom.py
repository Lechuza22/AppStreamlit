import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(page_title="TaxiCom2.0", layout="wide")

# Colores de la paleta
PRIMARY_COLOR = "#008080"  # Verde azulado del logo
SECONDARY_COLOR = "#444444"  # Gris oscuro
BACKGROUND_COLOR = "#F4F4F4"  # Fondo claro

# Estilo general
st.markdown(
    f"""
    <style>
        .css-18e3th9 {{
            background-color: {BACKGROUND_COLOR};
        }}
        .stButton > button {{
            background-color: {PRIMARY_COLOR};
            color: white;
            border-radius: 5px;
        }}
        h1 {{
            color: {PRIMARY_COLOR};
        }}
        .stSidebar {{
            background-color: {SECONDARY_COLOR};
            color: white;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Título y logo
st.sidebar.image("Logo.png", use_container_width=True)
st.sidebar.title("TaxiCom2.0")

# Opciones del menú
menu_option = st.sidebar.radio(
    "Seleccione una sección:",
    ("Comparar marcas y modelos", "Recomendaciones", "Marcas y modelos")
)

# Cargar datos
@st.cache_data
def load_data():
    file_path = 'ElectricCarData.csv'
    return pd.read_csv(file_path)

data = load_data()

if menu_option == "Comparar marcas y modelos":
    st.header("Comparar marcas y modelos")
    st.subheader ("Marcas(Brands) y modelos")
    st.text ("Para comparar primero selecciona las marcas y modelos, luego selecciona las variables que quieras incluir en la comparación")
    # Selección de marcas para comparación
    brands = data["brand"].unique()
    col1, col2 = st.columns(2)

    with col1:
        brand1 = st.selectbox("Seleccione la primera marca", brands, key="brand1")
    with col2:
        brand2 = st.selectbox("Seleccione la segunda marca", brands, key="brand2")

    # Filtrar modelos por marca
    models_brand1 = data[data["brand"] == brand1]
    models_brand2 = data[data["brand"] == brand2]

    # Selección de modelo dentro de cada marca
    col1, col2 = st.columns(2)
    
    with col1:
        model1 = st.selectbox("Seleccione el modelo de la primera marca", models_brand1["model"].unique(), key="model1")
    with col2:
        model2 = st.selectbox("Seleccione el modelo de la segunda marca", models_brand2["model"].unique(), key="model2")

    # Mostrar variables seleccionables
    variables = ["accel", "topspeed", "range", "efficiency", "priceusd"]
    selected_variables = st.multiselect("Seleccione las variables a comparar", variables, default=variables)

    # Filtrar datos de los modelos seleccionados
    data_model1 = data[(data["brand"] == brand1) & (data["model"] == model1)][selected_variables]
    data_model2 = data[(data["brand"] == brand2) & (data["model"] == model2)][selected_variables]

    # Mostrar tablas comparativas
    col1, col2 = st.columns(2)

    with col1:
        st.subheader(f"Datos de {model1}")
        st.write(data_model1)

    with col2:
        st.subheader(f"Datos de {model2}")
        st.write(data_model2)

    # Graficar comparación
    if selected_variables:
        st.subheader("Gráfico comparativo")
        fig, ax = plt.subplots(figsize=(6, 4))

        x = range(len(selected_variables))
        ax.bar(x, data_model1.iloc[0], width=0.4, label=model1, align="center", color="blue")
        ax.bar([i + 0.4 for i in x], data_model2.iloc[0], width=0.4, label=model2, align="center", color="orange")

        ax.set_xticks([i + 0.2 for i in x])
        ax.set_xticklabels(selected_variables, rotation=45)
        ax.set_title("Comparación de modelos")
        ax.legend()

        st.pyplot(fig)

elif menu_option == "Predicciones":
    st.header("Predicciones")
    st.write("Esta sección estará disponible próximamente.")

elif menu_option == "Marcas y modelos":
    st.header("Marcas y modelos")
    st.write("Esta sección estará disponible próximamente.")
