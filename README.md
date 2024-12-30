# workspace

## Reading a CSV file and displaying a graph

This section explains how to read a CSV file and display a graph using Python.

### Example Code

```python
import pandas as pd
import matplotlib.pyplot as plt

def read_csv(file_path):
    return pd.read_csv(file_path)

def plot_graph(data):
    data.plot()
    plt.show()

def main():
    file_path = 'data.csv'
    data = read_csv(file_path)
    plot_graph(data)

if __name__ == "__main__":
    main()
```
