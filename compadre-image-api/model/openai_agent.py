import requests
from dotenv import load_dotenv
import os
from model.config.prompt import system_message
load_dotenv()

class OpenAIAgent:
    def __init__(self) -> None:
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"
            }
    
    
    @staticmethod
    def _generate_payload(base64image):
        return {
                "model": "gpt-4o-mini",
                "messages": [
                    {
                    "role": "system",
                    "content": system_message
                    },
                    {
                    "role": "user",
                    "content": [
                        {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64image}"
                        }
                        }
                    ]
                    }
                ],
                "max_tokens": 300
                }
        
    def make_api_call(self,base64image):
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=self.headers, json=OpenAIAgent._generate_payload(base64image))
        return response.json()["choices"][0]["message"]["content"]