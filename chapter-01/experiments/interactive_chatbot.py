from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

llm = OpenAI()

prompt = input("Ask a question: ")

response = llm.responses.create(
  model="gpt-4.1",
  temperature=0,
  input=prompt
)

print("AI Response: ", response.output_text)
print("Total tokens: ", response.usage.total_tokens)
