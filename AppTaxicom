import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
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
st.sidebar.image("/mnt/data/Logo.png", use_column_width=True)
st.sidebar.title("TaxiCom2.0")

# Opciones del menú
menu_option = st.sidebar.radio(
    "Seleccione una sección:",
    ("Análisis de datos", "Predicciones", "Marcas y modelos")
)

# Cargar datos
@st.cache
def load_data():
    file_path = '/mnt/data/ElectricCarData.csv'
    return pd.read_csv(file_path)

data = load_data()

if menu_option == "Análisis de datos":
    st.header("Análisis de datos")
    
    # Selección de variables relevantes
    selected_columns = ["accel", "topspeed", "range", "efficiency", "priceusd"]
    data_filtered = data[selected_columns]

    # Escalado de datos
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data_filtered)

    # KMeans clustering
    kmeans = KMeans(n_clusters=5, random_state=42)
    data["Cluster"] = kmeans.fit_predict(data_scaled)

    # Visualización de resultados
    st.subheader("Distribución de marcas por clusters")
    cluster_counts = data.groupby(["brand", "Cluster"]).size().reset_index(name="Count")

    st.write(cluster_counts)

    # Gráfica de barras
    st.subheader("Gráfica de clusters")
    fig, ax = plt.subplots()
    cluster_counts.groupby("Cluster")["Count"].sum().plot(kind="bar", ax=ax, color=PRIMARY_COLOR)
    ax.set_title("Número de marcas por cluster")
    ax.set_xlabel("Cluster")
    ax.set_ylabel("Cantidad")
    st.pyplot(fig)

elif menu_option == "Predicciones":
    st.header("Predicciones")
    st.write("Esta sección estará disponible próximamente.")

elif menu_option == "Marcas y modelos":
    st.header("Marcas y modelos")
    st.write("Esta sección estará disponible próximamente.")
