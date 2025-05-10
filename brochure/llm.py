import requests
import json

MODEL = 'llama3.2'

link_system_prompt = """
You are provided with a list of links found on a webpage. 
You are able to decide which of the links would be most relevant to include in a brochure about the company, 
such as links to an About page, or a Company page, or Careers/Jobs pages.
Respond in JSON format like:
{
    "links": [
        {"type": "about page", "url": "https://example.com/about"},
        {"type": "careers page", "url": "https://example.com/careers"}
    ]
}
""".strip()

def chat_with_llama(system_prompt: str, user_prompt: str, model=MODEL):
    url = 'http://localhost:11434/api/chat'
    data = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": "Links: /about /contact"},
            {"role": "assistant", "content": '{"links": [{"type": "about page", "url": "https://example.com/about"}]}'},
            {"role": "user", "content": "Links: /terms /privacy"},
            {"role": "assistant", "content": '{"links": []}'},
            {"role": "user", "content": user_prompt}
        ],
        "stream": False
    }
    response = requests.post(url, json=data)
    return response.json()["message"]["content"]