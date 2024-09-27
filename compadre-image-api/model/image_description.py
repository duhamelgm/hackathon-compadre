import base64
from PIL import Image
from image_similarity_measures.evaluate import evaluation
from model.openai_agent import OpenAIAgent
import io


class ImageDescriptor:
    def __init__(self) -> None:
        self.openai_agent = OpenAIAgent()

    def _encode_image(self, image_data: io.BytesIO) -> str:
        image_data.seek(0)
        return base64.b64encode(image_data.read()).decode('utf-8')

    def describe(self, image_data: io.BytesIO) -> str:
        base64_image = self._encode_image(image_data)
        response = self.openai_agent.make_api_call(base64_image)
        return response