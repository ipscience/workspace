# workspace

## Uploading a CSV file and generating graphs

The web application allows users to upload a CSV file and analyze it to generate graphs using Python and Streamlit.

### Instructions

1. Upload a CSV file:
   - Click on the "Upload a CSV file" button.
   - Select the CSV file you want to upload.

2. Generate graphs:
   - Once the CSV file is uploaded, the application will automatically read the file and generate graphs.
   - The graphs will be displayed on the web application.

## Text Editor Functionality

The web application now includes a text editor that allows users to input and edit text.

### Instructions

1. Use the text editor:
   - The text editor is available on the main page of the application.
   - You can input and edit text using the text editor.

### Example Code

```python
import streamlit as st
import pandas as pd

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

    # Text editor functionality
    text = st.text_area("Enter text here")
    st.write("You entered:", text)

if __name__ == "__main__":
    main()
```
