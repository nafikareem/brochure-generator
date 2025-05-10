import streamlit as st
from brochure.brochure import create_brochure
import markdown as md
import pdfkit
import tempfile
import os

st.set_page_config(page_title="Company Brochure Generator", layout="centered")

st.title("Company Brochure Generator")
st.write("Generate a markdown brochure for any company website using AI")

company_name = st.text_input("Company Name", value="", placeholder="e.g. HuggingFace")
company_url = st.text_input("Company URL", value="", placeholder="e.g. https://huggingface.co")

if st.button("Generate Brochure"):
    with st.spinner("Generating brochure..."):
        result = create_brochure(company_name, company_url)
        st.markdown(result)