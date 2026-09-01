import streamlit as st
import numpy as np
import pandas as pd

st.title("ACW 2026 — Streamlit Test")

st.write("Streamlit is working!")

st.subheader("Environment")

st.write("NumPy version:", np.__version__)
st.write("Pandas version:", pd.__version__)

df = pd.DataFrame({
    "x": np.arange(10),
    "y": np.random.randn(10),
})

st.line_chart(df.set_index("x"))