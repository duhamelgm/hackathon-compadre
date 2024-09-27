from model.openai_agent import OpenAIAgent
import base64
from PIL import Image
from image_similarity_measures.evaluate import evaluation


class ImageDescriptor:
    def __init__(self) -> None:
        self.openai_agent = OpenAIAgent()
    
    @staticmethod
    def _encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
        
    def describe(self, image):
        base64_image = ImageDescriptor._encode_image(image)
        response = self.openai_agent.make_api_call(base64_image)
        return response
    
    def _resize(self,image_path):
        img = Image.open(image_path)
        new_img = img.resize((1000, 1000))
        new_img.save(image_path)     
        
    def compare(self, base_image_path, marketplace_image_path_dict):
        output_list = []
        self._resize(base_image_path)
        for elem in marketplace_image_path_dict:
            self._resize(elem["path"])
            elem["hashDiff"] = evaluation(org_img_path=base_image_path, 
               pred_img_path=elem['path'], 
               metrics=["rmse", "psnr"])
            output_list.append(elem)
        return output_list