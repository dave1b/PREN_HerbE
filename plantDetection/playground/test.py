import base64
import requests
from apiKeys import *

def encode_file(file_name):
    with open(file_name, "rb") as file:
        return base64.b64encode(file.read()).decode("ascii")


def identify_plant(file_names):
    # see the docs for more optional attributes
    params = {
        "api_key": plantIDkey,
        "images": [encode_file(img) for img in file_names],
        "latitude": 49.1951239,
        "longitude": 16.6077111,
        "datetime": 1582830233,
        "modifiers": ["crops_fast", "similar_images", "health_all"],
        "plant_language": "en",
        "plant_details": ["common_names",
                          "edible_parts",
                          "gbif_id"
                          "name_authority",
                          "propagation_methods",
                          "synonyms",
                          "taxonomy",
                          "url",
                          "wiki_description",
                          "wiki_image",
                          ],
        }

    headers = {
        "Content-Type": "application/json"
        }

    response = requests.post("https://api.plant.id/v2/identify",
                             json=params,
                             headers=headers)

    return response.json()


if __name__ == '__main__':
    print(identify_plant(["/Users/davebrunner/myCloud/HSLU/Module/3. Semester/PREN1/PRENcode/pflanze.jpg", "/Users/davebrunner/myCloud/HSLU/Module/3. Semester/PREN1/PRENcode/pflanze2.png"]))