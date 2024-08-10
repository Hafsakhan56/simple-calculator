import streamlit as st
from Addition import add
from Subtraction import subtract
from Multiplication import multiply
from Division import divide

def main():
    st.title("HEY! I Am HAFSA KHAN")
    st.header("Let's Calculate with ease!")
    st.subheader("--> Experience the smartest way to calculate with our intuitive and user-friendly calculator")

    num1 = st.number_input("Enter the first number", format="%.2f")
    num2 = st.number_input("Enter the second number", format="%.2f")
    operator = st.selectbox("Select an operator", ('+', '-', '*', '/'))

    result = None
    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)

    if result is not None:
        st.write(f"The result is: {result}")

        # Add a radio button for user choice to continue or quit
        choice = st.radio("Do you want to quit the calculator?", ('No', 'Yes'))

        if choice == 'Yes':
            st.write("Thank you for using the calculator!")
            st.stop()  # Stop the execution if the user chooses to quit

if __name__ == "__main__":
    main()