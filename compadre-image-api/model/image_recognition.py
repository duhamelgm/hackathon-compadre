from model.openai_agent import OpenAIAgent
import base64

class ImageRecognitionAgent:
    def __init__(self) -> None:
        self.openai_agent = OpenAIAgent()
    
    @staticmethod
    def _encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
        
    def predict(self, image_path):
        base64_image = ImageRecognitionAgent._encode_image(image_path)
        response = self.openai_agent.make_api_call(base64_image)
        return response