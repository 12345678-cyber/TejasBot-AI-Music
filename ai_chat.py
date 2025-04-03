import openai
from config import OPENAI_API_KEY, BOT_NAME

openai.api_key = OPENAI_API_KEY

def get_ai_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return f"🤖 **{BOT_NAME} Says:** {response['choices'][0]['message']['content']}"
