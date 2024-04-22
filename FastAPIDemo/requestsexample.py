import requests
import io
from PIL import Image
import json


def download_cat_image(cat_id:str):
    api_id= "https://api.thecatapi.com/v1/images/" + cat_id
    #result = requests.get("https://api.thecatapi.com/v1/images/0XYvRd7oD")
    result = requests.get(api_id)
    result.raise_for_status()
    print(result)
    jsonResult = result.json()
    #print(jsonResult["url"])
    url = jsonResult["url"]
    #print(url)
    #r = requests.get(url)
    #for key, value in jsonResult.items():
    #    print(key, ":", value)
    
    img = Image.open(requests.get(url, stream = True).raw)
    #img.save('img1.jpg')
    img.show()
    
    
if __name__ == "__main__":
    
    download_cat_image("0XYvRd7oD")
    
    