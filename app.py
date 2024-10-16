"""
The `os` module provides a way to interact with the operating system. 
It includes functions for file and directory manipulation, environment 
variables access, and path operations. Common functionalities include:

- Accessing and modifying the file system (e.g., creating, deleting files).
- Retrieving environment variables (e.g., `os.getenv()`).
- Working with paths and directories (e.g., `os.path`).
- Managing processes and system-specific parameters.

This module is essential for applications that require OS-level interactions.
"""
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq


# Define the Streamlit app

def main():
    """
    Main function for the Language Translation Streamlit app.

    This function sets up the Streamlit user interface, including a title,
    sidebar inputs for the GROQ API key and target language, and a text area
    for entering the text to be translated. It handles user interactions,
    initiates the translation process using the Langchain and GROQ API,
    and displays the translation results or any relevant messages.

    Sidebar Inputs:
    - GROQ API Key: A secure input field for entering the API key.
    - Language: A dropdown menu for selecting the target language for translation.

    Main Inputs:
    - Text to translate: A text area where the user can input the text that needs
      translation.

    On button click ("Translate"), the function validates inputs, initializes the
    translation model, prepares the prompt, and retrieves the translation,
    displaying it to the user. If inputs are missing or an error occurs,
    appropriate messages are shown to the user.
    """
    st.title("Language Translation App")

    # Sidebar for API key and language selection
    st.sidebar.header("Settings")
    groq_api_key = st.sidebar.text_input(
        "Enter your GROQ API Key", type="password")
    language = st.sidebar.selectbox(
        "Select Language", ["Spanish", "French", "German", "Chinese", "Japanese", "Portuguese"])

    # Input text for translation
    text_to_translate = st.text_area("Enter text to translate:")

    if st.button("Translate"):
        if groq_api_key and text_to_translate:
            # Initialize the model
            model = ChatGroq(model="gemma2-9b-it", groq_api_key=groq_api_key)

            # Prepare the prompt
            prompt_template = """
            Traduza o texto: {text} para a linguagem: {language}. Faça duas versões da tradução.
            Escreva apenas a tradução e nada mais, siga esse padrão:
            1. **formal**
            2. **informal**
            """
            prompt = ChatPromptTemplate.from_messages(
                [("system", prompt_template), ("user", text_to_translate)]
            )
            parser = StrOutputParser()
            chain = prompt | model | parser

            # Run the translation
            translation = chain.invoke(
                {"text": text_to_translate, "language": language})
            st.success(f"{translation}")

        else:
            st.warning(
                "Please enter both the GROQ API key and text to translate.")


if __name__ == "__main__":
    main()
