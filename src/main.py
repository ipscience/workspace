import os
import pandas as pd
import streamlit as st

def read_csv(file_path):
    return pd.read_csv(file_path)

def plot_graph(data):
    st.line_chart(data)

def perform_arithmetic_operations(value1, value2):
    try:
        value1 = float(value1)
        value2 = float(value2)
        addition = value1 + value2
        subtraction = value1 - value2
        multiplication = value1 * value2
        division = value1 / value2 if value2 != 0 else 'Infinity'
        return addition, subtraction, multiplication, division
    except ValueError:
        return '🙅', '🙅', '🙅', '🙅'

def main():
    st.title("CSV File Uploader and Arithmetic Operations")

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

    st.title("Arithmetic Operations")
    value1 = st.text_input("Enter the first value:")
    value2 = st.text_input("Enter the second value:")
    if st.button("Calculate"):
        addition, subtraction, multiplication, division = perform_arithmetic_operations(value1, value2)
        st.write(f"Addition: {addition}")
        st.write(f"Subtraction: {subtraction}")
        st.write(f"Multiplication: {multiplication}")
        st.write(f"Division: {division}")

if __name__ == "__main__":
    main()
