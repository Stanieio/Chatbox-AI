import requests, json

API_KEY = "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"   

while True:
    msg = input("You: ")

    r = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {"role": "user", "content": msg}
            ]
        }
    )

    data = r.json()

    
    print("AI:", data["choices"][0]["message"]["content"])
