import requests

class OpenAIAgent:
    def __init__(self, api_key) -> None:
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
            }
    
    
    @staticmethod
    def _generate_payload(base64image):
        return {
                "model": "gpt-4o-mini",
                "messages": [
                    {
                    "role": "user",
                    "content": [
                        {
                        "type": "text",
                        "text": "Can you described the most prominent object in this image?"
                        },
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
        return response.json()