import requests

LLAMA_API_URL = "https://api.together.xyz/v1/chat/completions"
LLAMA_API_KEY = "tgp_v1_kpN6r1tNqgrVrwosftbD3PSwnjx-DjVeNnaVCbKwF3k"

def generate_quiz(topic):
    headers = {
        "Authorization": f"Bearer {LLAMA_API_KEY}",
        "Content-Type": "application/json"
    }

    messages = [
        {"role": "system", "content": "You are a quiz generator. Generate 5 multiple-choice questions on the given topic. Each question should have 4 options and indicate the correct answer."},
        {"role": "user", "content": f"Generate a quiz on: {topic}"}
    ]

    payload = {
        "model": "mistralai/Mistral-7B-Instruct-v0.1",
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 700,
        "top_p": 0.9
    }

    response = requests.post(LLAMA_API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        content = response.json()["choices"][0]["message"]["content"]
        return content
    else:
        raise Exception(f"API Error {response.status_code}: {response.text}")
