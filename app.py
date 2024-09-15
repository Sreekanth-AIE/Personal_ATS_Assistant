import streamlit as st
from utils import cnv_pdf_to_text
from llm_inference import get_gemini_response, prompt_template

## Streamlit app
st.title("personal ATS Assistant")
job_description = st.text_area("Paste the Job Description")
uploaded_pdf = st.file_uploader("Upload Your Resume (please see that there are no sensitive data in resume like phone number, etc.)",type="pdf",help="Please upload the pdf")
explanation = st.checkbox(":orange-background[I want explanation]")
temperature = st.select_slider(":orange-background[higher temperature higher creativity]",options=map(lambda x: x/10, [i for i in range(0,11)]))
evaluate = st.button("evaluate")

if evaluate:
    if uploaded_pdf is not None:
        resume = cnv_pdf_to_text(uploaded_pdf)
        response = get_gemini_response(prompt_template.format(resume=resume,job_desc=job_description,explanation="with complete explanation" if explanation else "without any explanation"),temperature)
        st.write(response)
