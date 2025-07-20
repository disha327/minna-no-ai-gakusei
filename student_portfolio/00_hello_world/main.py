import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
prompt = "Hello, world!"

res = client.chat.completions.create(
    model="gpt-4o-mini",  # Using a current model
    messages=[{"role": "user", "content": prompt}],
)
print(res.choices[0].message.content)
