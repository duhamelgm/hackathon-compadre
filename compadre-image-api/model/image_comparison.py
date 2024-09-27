from skimage.metrics import structural_similarity as ssim 
import numpy as np
import cv2
import requests
import logging
import warnings
warnings.filterwarnings("ignore")

class ImageComparator:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def _mean_squared_error(image1, image2):
        error = np.sum((image1.astype('float') - image2.astype('float'))**2)
        error = error/float(image1.shape[0] * image2.shape[1])
        return error
    
    @staticmethod
    def _image_read(image_path):
        return cv2.imread(image_path)
    
    @staticmethod
    def _turn_gray(image):
        return cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    
    @staticmethod
    def _load_image_from_url(image_url):
        response = requests.get(image_url)

        # Check if the request was successful
        if response.status_code == 200:
            # Convert the image data to a numpy array
            image_array = np.frombuffer(response.content, np.uint8)
            
            # Decode the numpy array as an image
            return cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        
    @staticmethod
    def _resize_image(base_image, image):
        try:
            return cv2.resize(image,(base_image.shape[1::-1]),interpolation=cv2.INTER_AREA)
        except Exception as e:
            print(str(e))
    
    # def compare(self,base_image,image_url_list):
    #     base_image = ImageComparator._image_read(base_image)
    #     image_list = [
    #         ImageComparator._load_image_from_url(elem["imageUrl"]) for elem in image_url_list
    #     ]
        
    #     image_list = [
    #      ImageComparator._resize_image(base_image, image) for image in image_list   
    #     ]
        
    #     base_image = ImageComparator._turn_gray(base_image)
        
    #     image_list = [
    #      ImageComparator._turn_gray(image) for image in image_list   
    #     ]
    #     for index in range(len(image_url_list)):
    #         image_url_list[index]["MSE"] = ImageComparator._mean_squared_error(base_image, image_list[index])
            
    #     return image_url_list
    def compare(self, base_image_data, image_url_list):
        logging.info("compare")
        base_image = cv2.imdecode(np.frombuffer(base_image_data.getvalue(), np.uint8), cv2.IMREAD_COLOR)
        
        image_list = [self._load_image_from_url(elem["imageUrl"]) for elem in image_url_list]
        
        # Resize and convert to grayscale
        base_image = self._turn_gray(base_image)
        base_shape = base_image.shape
        
        for index in range(len(image_list)):
            image_list[index] = self._turn_gray(cv2.resize(image_list[index], (base_shape[1], base_shape[0])))
            
        for index in range(len(image_url_list)):
            mse_value = self._mean_squared_error(base_image, image_list[index])
            image_url_list[index]["MSE"] = mse_value
            
        return image_url_list