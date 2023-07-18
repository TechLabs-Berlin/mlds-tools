import streamlit as st
import pandas as pd
import numpy as np

st.title("Demo's don't get better than this!")

DATA_PATH = ('data/example.csv')

def load_data(nrows):
    data = pd.read_csv(DATA_PATH, nrows=nrows)
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(7)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')
st.subheader('Raw data')
st.write(data)

data["bio_length"] = (
    data["name"] + data["title_01"] + data["title_02"]
).str.len()

data["hero_rating"] = (
    data["name"] + data["title_01"] + data["title_02"]
).str.split().apply(lambda x: len(x))*5

# thresh = st.slider('hero_rating', 2, 5, 3)
# filtered_data = data[data["hero_rating"] > thresh]
st.subheader('Visualization')
st.bar_chart(data.set_index("name")[["hero_rating", "bio_length"]])