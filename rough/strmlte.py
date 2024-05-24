import streamlit as st

def main():
    st.title("Simple Streamlit App")

    # Add a text input widget
    user_input = st.text_input("Enter some text:")

    # Add a button widget
    button_clicked = st.button("Click Me")

    # When the button is clicked, display the input text
    if button_clicked:
        st.write("You entered:", user_input)

if __name__ == "__main__":
    main()






