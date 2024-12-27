import streamlit as st
import pandas as pd

# input data harga bensin
data_harga = {
    'pulau' : ['jawa', 'sumatra', 'kalimantan', 'sulawesi', 'papua'], 
    'harga pertalite' : [6500, 6800, 7000, 7200, 7500],
    'harga pertamax' : [8500, 9000, 9500, 10000, 10500],
    'harga pertamax turbo' : [14400, 15000, 15500, 16000, 16500]
}
df = pd.DataFrame(data_harga)

# tampilkan data
st.write(" Data Harga Bensin:")
st.dataframe(df)

#judul aplikasi
st.title(" PERBANDINGAN HARGA BENSIN DI BERBAGAI PULAU")
st.write(df)

# pilih pulau untuk melihat harga
pulau = st.selectbox("pilih pulau:", df['pulau'])
harga = df[df['pulau']== pulau]
['Harga Bensin (per liter)']

st.write(f"harga bensin di{pulau}: Rp{harga}")



