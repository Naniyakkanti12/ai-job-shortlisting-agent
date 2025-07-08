from resume_parser import extract_text_from_pdf
from jd_parser import extract_text_from_pdf as extract_jd
from ai_matcher import match_resume_to_job
from email_sender import send_email

resume_text = extract_text_from_pdf("uploads/resume.pdf")
jd_text = extract_jd("uploads/job_description.pdf")

result = match_resume_to_job(resume_text, jd_text)

print("\nAI Output:\n", result)

shortlisted = "Yes" in result
summary = result.split("4.")[1].strip()

send_email(
    to_email="candidate@example.com",
    subject="Job Application Status",
    message=("🎉 Shortlisted!\n\n" if shortlisted else "❌ Not Shortlisted.\n\n") + summary
)
