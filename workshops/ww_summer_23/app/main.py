from sqlalchemy import create_engine
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu


with st.sidebar:
    selected = option_menu(
        "OSR Menu",
        ["Run SQL", "List Tables", "Upload Table"],
        icons=["play", "list-task", "cloud-upload"],
        menu_icon="database",
        default_index=0,
    )
    selected

if selected == "Run SQL":
    # if 'default_flag' not in st.session_state:
    #     st.session_state.default_flag = False
    st.title("| graphical OSR |")
    st.subheader("Your Online SQL Runnner")
    st.header("Input query below:")
    txt = st.text_area(label="query")

    @st.cache_data
    def runner(query):
        # st.session_state.default_flag = True
        engine = create_engine("postgresql+psycopg2://postgres:docker@demodb:5432/postgres")
        data = pd.read_sql(query, con=engine)
        return data

    if st.button(label="Submit"):
        data = runner(txt)
        st.dataframe(data)
    # # if st.session_state.default_flag:

if selected == "List Tables":
    st.title("| graphical OSR |")
    st.subheader("Your Online SQL Runnner")
    st.header("Existing tables:")

    engine = create_engine("postgresql+psycopg2://postgres:docker@demodb:5432/postgres")
    data = pd.read_sql("SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public'", con=engine)
    st.dataframe(data)

if selected == "Upload Table":
    st.title("| graphical OSR |")
    st.subheader("Your Online SQL Runnner")
    st.header("Upload table to database:")

    uploaded_file = st.file_uploader("Upload your file here...", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file, sep=",")
        if st.button(label="Add Table"):
            table_name = uploaded_file.name.split(".")[0]
            engine = create_engine("postgresql+psycopg2://postgres:docker@demodb:5432/postgres")
            df.to_sql(table_name, con=engine, if_exists="fail", index=False)
            st.write(f":green[Created table **{table_name}** with {len(df)} records]")
