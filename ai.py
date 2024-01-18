import openai
import time
import json

import requests

def load_config(filename='config.json'):
    with open(filename, 'r') as f:
        return json.load(f)

config = load_config()

# Initialize your API key
openai.api_key = config['api']['key']

def process_line_with_chatgpt(prompt, request):
    headers = {
        "Authorization": f"Bearer {config['api']['key']}",
        "Content-Type": "application/json",
        "User-Agent": "OpenAI Python"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt + request}],
        "temperature": config['api']['temperature']
    }
    
    retries = config['api']['retries']
    while retries > 0:
        try:
            response = requests.post(config['api']['endpoint'], headers=headers, json=data, timeout=config['api']['timeout'])
            response_data = response.json()
            if response.status_code == 200:
                return response_data['choices'][0]['message']['content']
            else:
                raise Exception(response_data['error']['message'])
        except (requests.Timeout, requests.RequestException) as e:
            retries -= 1
            if retries == 0:
                raise e
            time.sleep(5)  # Wait for 5 seconds before retrying

def ai_topic():
    prompt = config['prompt']
    if prompt == "":
        prompt = input('Your prompt : ')
    request = input('Your request : ')
    response = process_line_with_chatgpt(prompt, request)
    print(f"Response: {response}\n")

    time.sleep(config['delay'])

if __name__ == "__main__":
   ai_topic()