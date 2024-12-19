import streamlit as st

#st.title("hallo mabro")
#st.markdown("selamat datang di kutub utara")
#st.image("images.jpg", caption="ini gambar")

dashboard = st.Page("./fitur/dashboard.py", title="Dashboard")
nabung = st.Page("./fitur/nabung.py", title="Menabung")

pg = st.navigation(
    {
       "Menu Utama" : [dashboard],
       "Transaksi" : [nabung],

    }
)

if 'total_semua' not in st.session_state:
    st.session_state['total_semua'] = []

pg.run()