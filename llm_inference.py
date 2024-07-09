import google.generativeai as genai
import os

# securely loading the environment variable here it is "GOOGLE_API_KEY"
from dotenv import load_dotenv
load_dotenv() 
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# initializing GEMINI model with customized system role
model=genai.GenerativeModel('gemini-1.5-flash')


# Prompt Template ##### **for original template contact me** #####
prompt_template = \
"""you are a sophisticated ATS (Application Tracking System) equipped with plethora of vocabulary and a deep understanding of technical fields like 
Software Engineering, Data Scientist, Data Analyst and Machine Learning Engineer.
Additionally, You must consider the job market is very competitive and you should provide best assistance for improving the resumes.
your task is to evaluate the resume based on the job description which are available from context.
context:
    1. resume:{resume}
    2. description:{job_desc}
output format:
    1. Assign the percentage Matching based on missing keywords in resume w.r.t. job description maintaining high accuracy and without hallucinating.
    2. The response should be in "heading and content" like markdown structure given below
    ATS_Match(%): %,
    Missing_Keywords:
        list of skills,
    Job Profile Summary:
        paragraph
    
    And provide the response {explanation}"""
  

def get_gemini_response(formatted_prompt: str,temperature: float) -> str:
    """function to te get response after the prompt inference"""    
    response = model.generate_content(formatted_prompt, generation_config = genai.GenerationConfig(temperature=temperature))
    return response.text