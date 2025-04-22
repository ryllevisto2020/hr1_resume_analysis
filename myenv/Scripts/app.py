
section = [1,2,3]
data = {"a":1,"b":2,"c":3}

_x = 1
_y = 2

def sum(x,y):
    return x+y

print("Hello World")
print(sum(_x,_y))

section.append(4)
print(section)

data["d"] = 4
print(data)

from google import genai
from pydantic import BaseModel

class PreInterviewQuestion(BaseModel):
    question:str
    choice:list[str]
    answer:str

client = genai.Client(api_key="AIzaSyAGYuIhuTyWhSKB0XE_I6RIOmNvma3OqaI")
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Give me 10 Question with 4 multiple Choice about tourism with correct answer",
    config={
        'response_mime_type': 'application/json',
        'response_schema': list[PreInterviewQuestion],
    },
)

print(response.text)