
from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class Sentiment(BaseModel):
    review: str 
    