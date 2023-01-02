import streamlit as st
import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori, association_rules
from st_aggrid import AgGrid

st.set_page_config(
    page_title="Apriori Website",
)

st.title('Apriori')
st.write('Selamat Datang di Website Pengolahan Data Transaksi Algoritma Apriori')

uploadFile = st.file_uploader('Upload File Excel Transaksi Penjulalan')

def hot_encode(x):
    if(x<= 0):
        return 0
    if(x>= 1):
        return 1

if uploadFile is not None :

    support = st.number_input('Masukkan Nilai Support', min_value=0.0, max_value=1.0)

    confidence = st.number_input('Masukkan Nilai Confidence', min_value=0.0, max_value=1.0)

    data = pd.read_excel(uploadFile)
    st.write(f"Jumlah data transaksi {len(data)} baris")

    st.dataframe(data)

    generateAturan = st.button('Generate Aturan Asosiai')

    if generateAturan :
        if support <= 0 and confidence <= 0 :
            st.write('Silahkan Periksa Inputan')
        else :
            st.markdown(f"**_Support_** {support} dan **_Confidence_** {confidence}")

            data['Nama Produk'] = data['Nama Produk'].str.strip()
            newData = data.groupby(['No. Pesanan', 'Nama Produk'])['Jumlah'].sum().unstack().reset_index().fillna(0).set_index('No. Pesanan')
            newData = newData.applymap(hot_encode)
            
            frq_items = apriori(newData, min_support = support, use_colnames = True)

            if frq_items.empty :
                st.write('Tidak Ditemukan Aturan, silahkan ubah nilai support')
            else :

                # Collecting the inferred rules in a dataframe
                rules = association_rules(frq_items, metric ="confidence", min_threshold = confidence)
                rules = rules.sort_values(['lift','confidence'], ascending =[False, False])
                rules["antecedents"] = rules["antecedents"].apply(lambda x: ', '.join(list(x))).astype("unicode")
                rules["consequents"] = rules["consequents"].apply(lambda x: ', '.join(list(x))).astype("unicode")

                st.write(f"Menghasilkan {len(rules)} aturan asosiasi")
                AgGrid(rules, theme='streamlit')