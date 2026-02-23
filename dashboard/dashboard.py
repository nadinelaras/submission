import streamlit as st
import pandas as pd
import altair as alt

# Config
st.set_page_config(
    page_title="Dashboard Analisis E-Commerce",
    layout="wide"
)

st.title("Dashboard Analisis E-Commerce 2016-2018")
st.markdown("Analisis performa pengiriman dan kontribusi revenue kategori produk.")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("main_data.csv")
    return df

df = load_data()

# Memastikan tidak ada missing kategori
df["product_category_name"] = df["product_category_name"].fillna("Unknown")

# Filter interaktif
st.sidebar.header("Filter Data")

year_range = st.sidebar.slider(
    "Pilih Rentang Tahun",
    min_value=int(df["purchase_year"].min()),
    max_value=int(df["purchase_year"].max()),
    value=(
        int(df["purchase_year"].min()),
        int(df["purchase_year"].max())
    )
)

filtered_df = df[
    (df["purchase_year"] >= year_range[0]) &
    (df["purchase_year"] <= year_range[1])
]

selected_categories = st.sidebar.multiselect(
    "Pilih Kategori Produk",
    options=sorted(filtered_df["product_category_name"].unique()),
    default=sorted(filtered_df["product_category_name"].unique())
)

filtered_df = filtered_df[
    filtered_df["product_category_name"].isin(selected_categories)
]

# Visualisasi 1 (Pertanyaan pertama)
# Persentase keterlambatan
st.subheader("Persentase Keterlambatan Pengiriman")

delay_summary = (
    filtered_df["is_delayed"]
    .value_counts(normalize=True)
    .mul(100)
    .reset_index()
)

delay_summary.columns = ["is_delayed", "percentage"]

delay_summary["Status"] = delay_summary["is_delayed"].map({
    True: "Delayed",
    False: "On Time / Early"
})

delay_chart = alt.Chart(delay_summary).mark_bar().encode(
    x=alt.X("Status:N", title="Status Pengiriman"),
    y=alt.Y("percentage:Q", title="Persentase (%)"),
    tooltip=["Status", alt.Tooltip("percentage:Q", format=".2f")]
).properties(
    title="Persentase Keterlambatan"
)

st.altair_chart(delay_chart, use_container_width=True)

# Visualisasi 2 (Pertanyaan kedua)
# Top 10 Revenue category
st.subheader("Top 10 Kategori Berdasarkan Total Revenue")

top_revenue_category = (
    filtered_df.groupby("product_category_name")["price"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

revenue_chart = alt.Chart(top_revenue_category).mark_bar().encode(
    x=alt.X("price:Q", title="Total Revenue"),
    y=alt.Y(
        "product_category_name:N",
        sort="-x",
        title="Kategori Produk"
    ),
    tooltip=[
        "product_category_name",
        alt.Tooltip("price:Q", format=",.0f")
    ]
).properties(
    title="Top 10 Kategori dengan Revenue Tertinggi"
)

st.altair_chart(revenue_chart, use_container_width=True)

# Footer info
st.markdown("---")
st.markdown(
    "Dashboard ini memungkinkan pengguna untuk mengeksplorasi dan "
    "memanipulasi data berdasarkan rentang tahun dan kategori produk."
)