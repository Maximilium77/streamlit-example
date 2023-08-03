import streamlit as st
import pandas as pd
from io import BytesIO
import base64

# Funzione per generare il grafico
def create_chart(data, start_date, end_date):
    filtered_data = data[(data['DATA'] >= start_date) & (data['DATA'] <= end_date)]
    chart = st.line_chart(filtered_data.set_index('DATA'))
    return chart

# Caricamento del file Excel
uploaded_file = st.file_uploader("Carica un file Excel", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    # Interfaccia per selezionare il periodo
    start_date = st.date_input("Seleziona la data di inizio", min_value=df['DATA'].min(), max_value=df['DATA'].max())
    end_date = st.date_input("Seleziona la data di fine", min_value=df['DATA'].min(), max_value=df['DATA'].max())

    # Crea il grafico
    create_chart(df, start_date, end_date)
