#!/usr/bin/env python3

import requests
from pathlib  import Path 
image_folder = Path.joinpath(Path.cwd(), "images")
image_files = image_folder.glob("*.jpeg")
file_data = [("files", image.open(mode='rb')) for image in image_files]
url = "http://httpbin.org/post"
r = requests.post(url, files=file_data)
print(r.json())
