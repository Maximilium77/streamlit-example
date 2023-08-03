import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

# Funzione per generare il grafico
def create_chart(data, start_date, end_date):
    filtered_data = data[(data['DATA'] >= start_date) & (data['DATA'] <= end_date)]
    plt.figure(figsize=(8, 6), tight_layout=True, dpi=100)
    plt.plot(filtered_data['DATA'], filtered_data['VALORE'])
    plt.title('Grafico')
    plt.xlabel('Data')
    plt.ylabel('Valore')
    return plt.gcf()

# Caricamento del file Excel
uploaded_file = st.file_uploader("Carica un file Excel", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    # Interfaccia per selezionare il periodo
    start_date = st.date_input("Seleziona la data di inizio", min_value=df['DATA'].min(), max_value=df['DATA'].max())
    end_date = st.date_input("Seleziona la data di fine", min_value=df['DATA'].min(), max_value=df['DATA'].max())

    # Crea il grafico
    chart = create_chart(df, start_date, end_date)
    st.pyplot(chart)

    # Salva il grafico come immagine e permetti di scaricarlo
    img_buffer = BytesIO()
    chart.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    st.markdown("### Scarica il grafico come immagine:")
    st.image(img_buffer, use_container_width=True)
    b64 = base64.b64encode(img_buffer.read()).decode()
    href = f'<a href="data:image/png;base64,{b64}" download="grafico.png">Clicca qui per scaricare</a>'
    st.markdown(href, unsafe_allow_html=True)
