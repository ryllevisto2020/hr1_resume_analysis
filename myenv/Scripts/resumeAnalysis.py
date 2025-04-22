from pypdf import PdfReader

reader = PdfReader('rylle resume.pdf')
job_desc = PdfReader('jobdescription_administrative_assistant.pdf')

#print(len(reader.pages))


pages_job = job_desc.pages[0]
pages = reader.pages[0]

text_job = pages_job.extract_text()
text = pages.extract_text()

from google import genai
from pydantic import BaseModel

class ResumeAnalysis(BaseModel):
    percentage:int

client = genai.Client(api_key="AIzaSyAGYuIhuTyWhSKB0XE_I6RIOmNvma3OqaI")
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Rate this Resume"+ text+ "based on the Job Requirements and Qualifications"+ text_job,
        config={
        'response_mime_type': 'application/json',
        'response_schema': ResumeAnalysis,
    },
)

print(response.text)