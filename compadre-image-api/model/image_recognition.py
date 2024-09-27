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

    def _resize(self, image_path: str) -> None:
        img = Image.open(image_path)
        new_img = img.resize((1000, 1000))
        new_img.save(image_path)

    def compare(self, base_image_path: str, marketplace_image_path_dict: list) -> list:
        output_list = []
        self._resize(base_image_path)
        for elem in marketplace_image_path_dict:
            self._resize(elem["path"])
            elem["hashDiff"] = evaluation(
                org_img_path=base_image_path,
                pred_img_path=elem['path'],
                metrics=["rmse", "psnr"]
            )
            output_list.append(elem)
        return output_list