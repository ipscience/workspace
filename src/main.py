import os
import pandas as pd
import streamlit as st

def read_csv(file_path):
    return pd.read_csv(file_path)

def plot_graph(data):
    st.line_chart(data)

def main():
    st.title("CSV File Uploader and Analyzer")

    file_path = 'data.csv'
    if not os.path.exists(file_path):
        uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
        if uploaded_file is not None:
            data = pd.read_csv(uploaded_file)
            plot_graph(data)
        else:
            st.write("Please upload a CSV file.")
    else:
        data = read_csv(file_path)
        plot_graph(data)

if __name__ == "__main__":
    main()
