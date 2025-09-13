import streamlit as st
from generator import ImageGenerator

def main():
    st.title("AI Image Generator")
    st.write("Enter a text prompt to generate an image.")

    text_prompt = st.text_input("Text Prompt")

    if st.button("Generate Image"):
        if text_prompt:
            generator = ImageGenerator()
            image = generator.generate_image(text_prompt)
            st.image(image, caption="Generated Image", use_container_width=True)
        else:
            st.error("Please enter a text prompt.")

if __name__ == "__main__":
    main()