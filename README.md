# 🚗 Análisis de Vehículos Usados en EE. UU.

Este proyecto presenta una **aplicación web interactiva** construida con **Streamlit** para analizar anuncios de venta de vehículos usados en Estados Unidos. Permite explorar tendencias de precios, modelos y tipos de transmisión a través de filtros dinámicos y visualizaciones informativas.

## 🔍 ¿Qué hace esta aplicación?

- 📊 Filtra vehículos por año, precio, tipo y transmisión.
- 🧮 Muestra histogramas de precios, gráficas de dispersión y series de tiempo.
- 🌐 Ofrece visualizaciones adicionales usando **Plotly Express**.
- 📥 Permite exportar los datos filtrados como archivo CSV.

## 📁 Estructura del proyecto

streamlit-dashboard/
```├── app.py
├── data_loader.py
├── dashboard.py
├── vehicles_us.csv
├── requirements.txt
├── README.md
├── notebooks/
│ └── EDA.ipynb
├── utils/
│ ├── filters.py
│ ├── state_coords.py
│ └── utils.py


## ⚙️ Tecnologías utilizadas

- Python 3.x
- Streamlit
- Pandas
- Seaborn & Matplotlib
- Plotly Express

## 🚀 Cómo ejecutar localmente

1. Clona este repositorio:
   ```bash
   git clone https://github.com/Eme48/streamlit-dashboard.git
   cd streamlit-dashboard

2. Crea un entorno virtual e instálalo:
    ```python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt

3. Ejecuta la aplicación:
    ```streamlit run app.py

## 🌐 Versión en línea
Puedes acceder a la versión desplegada en Render en el siguiente enlace:

➡️ https://streamlit-dashboard-dlsq.onrender.com/

## ✍️ Autor
Emerson Ríos