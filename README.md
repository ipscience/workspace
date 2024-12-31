# workspace

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
