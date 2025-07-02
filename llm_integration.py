from openai import OpenAI
import os

client = OpenAI(
  api_key=os.environ["CHATBOT_PLATFORM_TEMPLATE_API_KEY"]
)

completion = client.chat.completions.create(
  model="gpt-4.1-nano",
  store=True,
  messages=[
    {"role": "user", "content": "Say hello to template"}
  ]
)

print(completion.choices[0].message);
