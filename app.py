import os
from dotenv import load_dotenv
from groq import Groq  # Correctly importing from the external `groq` library

load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def get_chat_completion():
    return client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Qual é o seu nome ?",
            }
        ],
        model="llama3-8b-8192",
    )

chat_completion = get_chat_completion()
print(chat_completion.choices[0].message.content)
