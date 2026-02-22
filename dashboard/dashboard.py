import streamlit as st
import pandas as pd
import altair as alt

# Config
st.set_page_config(page_title="Interactive E-Commerce Dashboard", layout="wide")

st.title("E-Commerce Dashboard")

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("main_data.csv")
    df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"])
    return df

df = load_data()

# Sidebar Filter
st.sidebar.header("Filter")

selected_year = st.sidebar.multiselect(
    "Select Year",
    options=sorted(df["purchase_year"].unique()),
    default=sorted(df["purchase_year"].unique())
)

df = df[df["purchase_year"].isin(selected_year)]

# Visualization Selector
option = st.selectbox(
    "Choose Visualization",
    (
        "Revenue per Year",
        "Top 10 Product Category by Revenue",
        "Average Delivery Time per Category",
        "RFM Segment Distribution"
    )
)

# Chart 1: Revenue per Year
if option == "Revenue per Year":

    data = df.groupby("purchase_year", as_index=False)["price"].sum()

    chart = alt.Chart(data).mark_line(point=True).encode(
        x="purchase_year:O",
        y="price:Q",
        tooltip=["purchase_year", "price"]
    ).interactive()

    st.altair_chart(chart, width="stretch")

# Chart 2: Top Category
elif option == "Top 10 Product Category by Revenue":

    data = (
        df.groupby("product_category_name", as_index=False)["price"]
        .sum()
        .sort_values("price", ascending=False)
        .head(10)
    )

    chart = alt.Chart(data).mark_bar().encode(
        x=alt.X("price:Q", title="Revenue"),
        y=alt.Y("product_category_name:N", sort="-x"),
        tooltip=["product_category_name", "price"]
    ).interactive()

    st.altair_chart(chart, width="stretch")

# Chart 3: Delivery Time
elif option == "Average Delivery Time per Category":

    data = (
        df.groupby("product_category_name", as_index=False)["delivery_time_days"]
        .mean()
        .sort_values("delivery_time_days", ascending=False)
        .head(10)
    )

    chart = alt.Chart(data).mark_bar().encode(
        x="delivery_time_days:Q",
        y=alt.Y("product_category_name:N", sort="-x"),
        tooltip=["product_category_name", "delivery_time_days"]
    ).interactive()

    st.altair_chart(chart, width="stretch")

# Chart 4: RFM Segment
elif option == "RFM Segment Distribution":

    data = df["Segment"].value_counts().reset_index()
    data.columns = ["Segment", "Count"]

    chart = alt.Chart(data).mark_bar().encode(
        x="Count:Q",
        y=alt.Y("Segment:N", sort="-x"),
        tooltip=["Segment", "Count"]
    ).interactive()

    st.altair_chart(chart, width="stretch")