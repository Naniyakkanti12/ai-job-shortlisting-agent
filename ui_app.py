import streamlit as st
from resume_parser import extract_text_from_pdf
from jd_parser import extract_text_from_pdf as extract_jd
from ai_matcher import match_resume_to_job
from email_sender import send_email

st.title("🤖 AI Job Screening Agent")

resume = st.file_uploader("Upload Resume", type=["pdf"])
jd = st.file_uploader("Upload Job Description", type=["pdf"])
email = st.text_input("Candidate Email")

if st.button("Screen Candidate"):
    if resume and jd and email:
        r_text = extract_text_from_pdf(resume)
        jd_text = extract_jd(jd)
        result = match_resume_to_job(r_text, jd_text)
        st.text_area("AI Result", result)
        shortlisted = "Yes" in result
        summary = result.split("4.")[1].strip()

        send_email(
            to_email=email,
            subject="Job Application Status",
            message=("🎉 Shortlisted!\n\n" if shortlisted else "❌ Not Shortlisted.\n\n") + summary
        )
        st.success("✅ Email Sent to Candidate.")
    else:
        st.warning("Please upload both files and enter an email.")
