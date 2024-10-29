from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:8000/ollama/v1",
    api_key="XXX",
    default_headers={"apikey": "f9941bef-b8e2-41d3-8705-2da8f21f0dfe"}
)


chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "translate rabbit in french",
        }
    ],
    model="gemma2:2b",
)

