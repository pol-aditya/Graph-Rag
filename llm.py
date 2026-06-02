
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()


# OpenRouter client
client = OpenAI(

    api_key=os.getenv("OPENROUTER_API_KEY"),

    base_url="https://openrouter.ai/api/v1"
)


def ask_llm(context, question):

    prompt = f"""
You are an AI App Store compliance auditor.

Analyze the provided source code and privacy policy.

Check for:
- privacy risks
- permissions
- tracking
- GDPR issues
- missing disclosures

Context:
{context}

Question:
{question}
"""

    completion = client.chat.completions.create(

        model="openai/gpt-3.5-turbo",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return completion.choices[0].message.content
