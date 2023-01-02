import streamlit as st
from PIL import Image

st.title('Apriori')
st.write('Cara Menggunakan Apriori di Website Ini')

st.write("Untuk memulai menggunakan apriori di situs ini, pertama-tama siapkan file Excel yang berisi kolom 'No. Pesanan', 'Nama Produk', dan 'Jumlah' seperti yang dijelaskan pada gambar di bawah ini.	")

image1 = Image.open('img/1.PNG')
st.image(image1, caption='Nama Kolom')

st.write("Kolom 'No. Pesanan', 'Nama Produk', dan 'Jumlah' sudah dibuat, sekarang isilah masing-masing kolom dengan data yang sesuai. Gambar di bawah ini hanyalah contoh penggunaan data pada masing-masing kolom, Anda bebas mengisinya sesuai kebutuhan.")

image2 = Image.open('img/2.PNG')
st.image(image2, caption='Nama Kolom dan Contoh Data')

st.write("unggah berkas Excel yang sudah dibuat sebelumnya dengan mengklik tombol 'Browse files' yang terdapat pada gambar di bawah ini.")

image3 = Image.open('img/4.PNG')
st.image(image3, caption='Tombol Upload File Excel')

st.write('Setelah mengupload file excel kalian, nanti nama file excel kalian akan muncul dibawah tombol upload ini. Untuk nama file Excel tidak harus sama seperti pada contoh gambar di bawah ini.')

image4 = Image.open('img/5.PNG')
st.image(image4, caption='Contoh Nama File Excel Ketika Berhasil Diupload')

st.write('Setelah mengupload file Excel dan nama file Excel akan terlihat di situs. Selanjutnya, Anda akan melihat input untuk nilai support dan confidence seperti yang terlihat pada gambar di bawah ini.	')

image5 = Image.open('img/6.PNG')
st.image(image5, caption='Inputan Nilai Support dan Confidence')

st.write("Masukkan nilai support dan confidence pada input dengan rentang nilai 0-1. Setelah selesai, klik tombol 'Generate Aturan Asosiasi' yang terdapat di bagian paling bawah halaman untuk mendapatkan aturan asosiasi. Gambar di bawah ini menunjukkan bentuk tombol tersebut.")

image6 = Image.open('img/7.PNG')
st.image(image6, caption='Tombol Untuk Menghasilkan Aturan Asosiasi')

st.write("Setelah kalian mengklik tombol tersebut nanti hasil aturan asosiasinya akan muncul seperti pada contoh di bawah ini.")

image7 = Image.open('img/8.PNG')
st.image(image7, caption='Contoh Aturan Asosiasi yang Dihasilkan')