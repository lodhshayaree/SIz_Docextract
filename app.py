import streamlit as st
import google.generativeai as genai
from langchain import OpenAI
from PyPDF2 import PdfReader
from dotenv import load_dotenv
import os
import chromadb
import faiss

# Load environment variables from .env file
load_dotenv()

# Set up API key
google_api_key = os.getenv("GOOGLE_API_KEY")

# Initialize Gemini API Client
genai.configure(api_key=google_api_key)

# Function to get the Gemini response
def get_gemini_response(prompt):
    response = genai.generate(prompt=prompt)
    return response

# Function to read PDF content
def read_pdf(file):
    pdf_reader = PdfReader(file)
    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Function to handle Image input
def process_image(image):
    # Convert image to appropriate format for Gemini Pro
    pass  # Implement image processing here if needed

# Streamlit App Interface
st.title("GeminiDecode for Legal Document Management")
st.write("Upload your documents to analyze using the Gemini Pro Model")

# Upload Document
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
if uploaded_file is not None:
    # Read and display PDF content
    pdf_text = read_pdf(uploaded_file)
    st.write("Extracted Text from PDF:")
    st.write(pdf_text)

    # Prompt for Gemini Model
    prompt = f"Extract and organize the following legal document: {pdf_text}"
    
    # Get response from Gemini API
    st.write("Processing with Gemini Pro...")
    gemini_output = get_gemini_response(prompt)
    
    # Display output
    st.write("Gemini Pro Response:")
    st.write(gemini_output)

# Image input processing
image_file = st.file_uploader("Upload an image for analysis", type=["jpg", "jpeg", "png"])
if image_file is not None:
    # Process the image for the Gemini Model
    process_image(image_file)
    st.write("Image uploaded successfully!")

st.sidebar.title("Navigation")
st.sidebar.write("Choose options from the sidebar to interact with the application.")
