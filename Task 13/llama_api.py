import requests

LLAMA_API_URL = "https://api.together.xyz/v1/chat/completions"
LLAMA_API_KEY = "tgp_v1_kpN6r1tNqgrVrwosftbD3PSwnjx-DjVeNnaVCbKwF3k"

def generate_quiz(topic):
    headers = {
        "Authorization": f"Bearer {LLAMA_API_KEY}",
        "Content-Type": "application/json"
    }

    messages = [
        {
            "role": "system",
            "content": "You are a quiz generator. Generate exactly 10 quiz questions (without options) on the given topic. Number them clearly."
        },
        {
            "role": "user",
            "content": f"Generate a quiz on the topic: {topic}"
        }
    ]

    payload = {
        "model": "mistralai/Mistral-7B-Instruct-v0.1",
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 700,
        "top_p": 0.9
    }

    try:
        response = requests.post(LLAMA_API_URL, headers=headers, json=payload)
        response.raise_for_status()

        data = response.json()
        content = data.get("choices", [])[0].get("message", {}).get("content", "").strip()

        if not content:
            raise ValueError("No content returned from LLaMA API.")
        
        return content

    except requests.exceptions.RequestException as e:
        raise Exception(f"Request error: {e}")
    except (KeyError, IndexError, ValueError) as e:
        raise Exception(f"Unexpected response format: {e}")
