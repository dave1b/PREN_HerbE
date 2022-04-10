response = {
    "id": 40469614,
    "custom_id": None,
    "meta_data": {
        "latitude": None,
        "longitude": None,
        "date": "2022-04-04",
        "datetime": "2022-04-04"
    },
    "uploaded_datetime": 1649066504.502392,
    "finished_datetime": 1649066504.897418,
    "images": [
        {
            "file_name": "362c69658fe044e3b0ef470f43753541.jpg",
            "url": "https: //plant.id/media/images/362c69658fe044e3b0ef470f43753541.jpg"
        }
    ],
    "suggestions": [
        {
            "id": 245209437,
            "plant_name": "Hoya kerrii",
            "plant_details": {
                "common_names": [
                    "Sweetheart Hoya",
                    "Valentine Hoya",
                    "Wax Hearts"
                ],
                "scientific_name": "Hoya kerrii",
                "structured_name": {
                    "genus": "hoya",
                    "species": "kerrii"
                }
            },
            "probability": 0.2379848557859247,
            "confirmed": False
        },
        {
            "id": 245209438,
            "plant_name": "Ficus elastica",
            "plant_details": {
                "common_names": [
                    "India-rubber Tree",
                    "rubber fig",
                    "rubber bush",
                    "rubber tree",
                    "rubber plant",
                    "Indian rubber bush"
                ],
                "scientific_name": "Ficus elastica",
                "structured_name": {
                    "genus": "ficus",
                    "species": "elastica"
                }
            },
            "probability": 0.200612828371776,
            "confirmed": False
        },
        {
            "id": 245209439,
            "plant_name": "Kalanchoe orgyalis",
            "plant_details": {
                "common_names": [
                    "Copper Spoons"
                ],
                "scientific_name": "Kalanchoe orgyalis",
                "structured_name": {
                    "genus": "kalanchoe",
                    "species": "orgyalis"
                }
            },
            "probability": 0.05086081396465486,
            "confirmed": False
        },
        {
            "id": 245209440,
            "plant_name": "Clusia rosea",
            "plant_details": {
                "common_names": [
                    "autograph tree",
                    "copey",
                    "balsam apple",
                    "pitch-apple",
                    "Scotch attorney"
                ],
                "scientific_name": "Clusia rosea",
                "structured_name": {
                    "genus": "clusia",
                    "species": "rosea"
                }
            },
            "probability": 0.043939241014303174,
            "confirmed": False
        },
        {
            "id": 245209441,
            "plant_name": "Eucalyptus cinerea",
            "plant_details": {
                "common_names": [
                    "Argyle apple",
                    "mealy stringbark"
                ],
                "scientific_name": "Eucalyptus cinerea",
                "structured_name": {
                    "genus": "eucalyptus",
                    "species": "cinerea"
                }
            },
            "probability": 0.03551739324781057,
            "confirmed": False
        },
        {
            "id": 245209442,
            "plant_name": "Calotropis procera",
            "plant_details": {
                "common_names": [
                    "Sodomís apple milkweed",
                    "Apple of Sodom",
                    "Sodom apple",
                    "stabragh",
                    "kings crown", "rubber bush", "rubber tree", "Dead Sea Apple"
                    ],
            "scientific_name": "Calotropis procera", "structured_name": {"genus": "calotropis", "species": "procera"}}, "probability": 0.030890907003361116, "confirmed": False}, {"id": 245209443, "plant_name": "Metrosideros kermadecensis", "plant_details": {"common_names": ["Kermadec pōhutukawa", "New Zealand Christmas bush"], "scientific_name": "Metrosideros kermadecensis", "structured_name": {"genus": "metrosideros", "species": "kermadecensis"}}, "probability": 0.023666798896055087, "confirmed": False}, {"id": 245209444, "plant_name": "Metrosideros excelsa", "plant_details": {"common_names": ["Pohutukawa", "New Zealand Christmas tree", "New Zealand Christmas bush", "iron tree"], "scientific_name": "Metrosideros excelsa", "structured_name": {"genus": "metrosideros", "species": "excelsa"}}, "probability": 0.014656746214056077, "confirmed": False}, {"id": 245209445, "plant_name": "Peperomia obtusifolia", "plant_details": {"common_names": ["baby rubberplant", "pepper face"], "scientific_name": "Peperomia obtusifolia", "structured_name": {"genus": "peperomia", "species": "obtusifolia"}}, "probability": 0.012849721567376763, "confirmed": False}, {"id": 245209446, "plant_name": "Phalaenopsis", "plant_details": {"common_names": ["moth orchids"], "scientific_name": "Phalaenopsis", "structured_name": {"genus": "phalaenopsis"}}, "probability": 0.010450676022727978, "confirmed": False}, {"id": 245209447, "plant_name": "Kalanchoe thyrsiflora", "plant_details": {"common_names": ["paddle plant", "flapjacks", "desert cabbage", "white lady", "geelplakkie", "plakkie"], "scientific_name": "Kalanchoe thyrsiflora", "structured_name": {"genus": "kalanchoe", "species": "thyrsiflora"}}, "probability": 0.010418447841149465, "confirmed": False}, {"id": 245209448, "plant_name": "Euphorbia umbellata", "plant_details": {"common_names": None, "scientific_name": "Euphorbia umbellata", "structured_name": {"genus": "euphorbia", "species": "umbellata"}}, "probability": 0.01021545827925187, "confirmed": False}], "modifiers": ["crops_medium"], "secret": "pcxYRpQNUvMET1F", "fail_cause": None, "countable": True, "feedback": None, "is_plant_probability": 0.9807335336666666, "is_plant": True}

recognisedPlantsList = []
imgURL = (response["images"][0]["url"])
for suggestion in response["suggestions"]:
    print("PlantApiSerice - detectPlant()" )
    if(suggestion["probability"] >= 0.01):
        recognisedPlantsList.append(suggestion["plant_name"])
        if(True):
            recognisedPlantsList1 = recognisedPlantsList
            commonName = response["suggestions"][0]["plant_details"]["common_names"][0]
            plant1Type = recognisedPlantsList[0]
            imageURL = imgURL
        else:
            recognisedPlantsListx = recognisedPlantsList

print("recognisedPlantsList1 " + str(recognisedPlantsList1))
print("plant1Type " + str(plant1Type))
print("commonName " + str(commonName))
print("imageURL " + str(imageURL))
#print("recognisedPlantsListx " + str(recognisedPlantsListx))
