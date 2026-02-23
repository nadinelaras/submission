# E-Commerce Dashboard 

Dashboard untuk analisis performa e-commerce berdasarkan data transaksi.

# AI Attribution/Acknowledgements

Ide dan Konsep: Saya menggunakan ChatGPT untuk brainstorming fitur yang akan dibutuhkan sesuai konteks bisnis pada dataset yang saya pakai yaitu E-Commerce Public Dataset.

Syntax dan Debugging: Saya menggunakan ChatGPT untuk memperbaiki kode yang saya gunakan, terdapat penyesuaian yang diberikan oleh ChatGPT agar selaras dengan syntax Python.

Interpretasi: Saya menggunakan ChatGPT untuk memahami dataset dalam konteks ilmu bisnis sehingga saya dapat melihat insight yang ada pada proses analisis data.

Catatan: Semua kode telah saya uji dan modifikasi.

# Struktur Direktori 

```
submission
├───dashboard
| ├───main_data.csv
| └───dashboard.py
├───data
| ├───orders_dataset.csv
| ├───order_items_dataset.csv
| ├───customers_dataset.csv
| └───products_dataset.csv
├───Proyek_Analisis_Data.ipynb
├───README.md
└───requirements.txt
└───url.txt
```

# Setup Environment - Anaconda 

```
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

# Setup Environment - Shell/Terminal 

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

# Run Streamlit App 

Jalankan dari root folder project:

```
streamlit run dashboard/dashboard.py
```

Aplikasi akan berjalan di:

```
http://localhost:8501
```