import os
import gradio as gr
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

def chatbot(message):
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": message
            }
        ]
    )

    answer = response.choices[0].message.content

    return answer

app = gr.Interface(
    fn=chatbot,
    inputs=gr.Textbox(
        placeholder="Ask me anything...",
        label="Your Message"
    ),
    outputs=gr.Textbox(
        label="AI Response"
    ),
    title="My AI Chatbot",
    description="A simple chatbot using Groq API",
)

app.launch()


