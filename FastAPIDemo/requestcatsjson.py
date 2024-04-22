import json
import requests
import io
from PIL import Image


result = requests.get("https://api.thecatapi.com/v1/images/0XYvRd7oD")

result.raise_for_status()
print(result)

jsonResult = result.json()
print(jsonResult)

url = jsonResult["url"]
print(url)

img = Image.open(requests.get(url, stream = True).raw)
img.save('img1.jpg')


#img.show()