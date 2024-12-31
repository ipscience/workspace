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

if __name__ == "__main__":
    main()
```
