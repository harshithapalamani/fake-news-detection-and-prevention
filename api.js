import requests

def detect_fake_news(text, api_key):
    url = "https://api.grok.ai/v1/fake-news-detection" 
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "text": text
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()  # parse and handle the response accordingly
    else:
        print("Error:", response.status_code, response.text)
        return None

api_key = ""
news_text = "Sample news text to classify."
result = detect_fake_news(news_text, api_key)
print(result)
