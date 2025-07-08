from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

def match_resume_to_job(resume_text, jd_text):
    prompt = PromptTemplate(
        input_variables=["resume", "job"],
        template="""
You are an AI HR recruiter.
Given the resume and job description below, answer:

1. Is the candidate eligible? (Yes or No)
2. List 3 matching skills or experiences.
3. List 2 key gaps.
4. Write a 1-line summary for email.

Resume:
{resume}

Job Description:
{job}
"""
    )
    llm = OpenAI(temperature=0)
    return llm(prompt.format(resume=resume_text, job=jd_text))
