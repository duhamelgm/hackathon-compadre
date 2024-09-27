from pydantic import BaseModel, HttpUrl

from typing import List

class DescriptionOutputFormat(BaseModel):
    description: str
    
class ComparatorImage(BaseModel):
    name: str
    price: float
    currency: str
    imageUrl: HttpUrl
    url: str = None
    source: str
    MSE: float = None

class ComparatorInputFormat(BaseModel):
    image_list: List[ComparatorImage]
    
class ComparatorOutputFormat(BaseModel):
    response: list