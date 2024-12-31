# workspace

## Reading a CSV file and displaying a graph using Streamlit

This section explains how to read a CSV file and display a graph using Streamlit.

### Example Code

```python
import pandas as pd
import streamlit as st

def read_csv(file_path):
    return pd.read_csv(file_path)

def plot_graph(data):
    st.line_chart(data)

def main():
    file_path = 'data.csv'
    data = read_csv(file_path)
    plot_graph(data)

if __name__ == "__main__":
    main()
```

## Uploading a CSV file if it does not exist

If the CSV file does not exist, the web application will prompt you to upload a CSV file.

### Example Code

```python
import os
import pandas as pd
import streamlit as st

def read_csv(file_path):
    return pd.read_csv(file_path)

def plot_graph(data):
    st.line_chart(data)

def main():
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
```

## Performing arithmetic operations on two input values

The web application allows you to perform arithmetic operations (addition, subtraction, multiplication, division) on two input values.

### Example Code

```python
import streamlit as st

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
```

## Handling non-numeric characters and displaying '🙅'

The web application includes error handling to display '🙅' for non-numeric characters.

### Example Code

```python
import streamlit as st

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
```
