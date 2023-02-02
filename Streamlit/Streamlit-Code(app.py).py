import streamlit as st  # web development
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import time  # to simulate a real time data, time loop
import plotly.express as px  # interactive charts
import os
from google.cloud import bigquery


def bigquery_get_df(query="SELECT * FROM dataEngineeringProjectDataset.dataEngineeringProjectTable"):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'mineral.json'
    client = bigquery.Client()

    table_id = "mineral-rune-365815.dataEngineeringProjectDataset.dataEngineeringProjectTable"
    QUERY = (
        query)
    query_job = client.query(QUERY)  # API request

    rows = query_job.result()  # Waits for query to finish
    row_list = []
    for row in rows:
        value = [row[0], row[1], row[2], row[3], row[4], row[5]]
        row_list.append(value)
    df = pd.DataFrame(row_list,
                      columns=['eth_form', 'eth_to', 'eth_value', 'eth_tms', 'eth_hash', 'eth_paymount_amount'])

    return df


# read csv from a github repo
df = bigquery_get_df()

st.set_page_config(
    page_title='Real-Time Project',
    page_icon='✅',
    layout='wide'
)

# dashboard title

st.title("Real-Time Project")

# top-level filters

job_filter = st.selectbox("İl Seçin", pd.unique(df['eth_form']))

# creating a single-element container.
placeholder = st.empty()

# # dataframe filter

df = df[df['eth_form'] == job_filter]

# near real-time / live feed simulation

while True:
    df = bigquery_get_df()

    with placeholder.container():
        st.markdown("### Detailed Data View")
        st.dataframe(df[df['eth_form'] == job_filter], use_container_width=True)

        time.sleep(1)