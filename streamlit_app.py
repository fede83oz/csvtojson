import streamlit as st

st.title("🎈Dell'Alba csv to json")
st.write(
    "Carica un file csv"
)

st.file_uploader(label="Carica un file csv",type='csv',accept_multiple_files=False)