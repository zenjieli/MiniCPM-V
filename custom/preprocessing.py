import os.path as osp
import json


def generate_conversations(img_filename, value):
    label_dict = {}
    # get the base name of img_filename without extension
    img_basename = osp.splitext(osp.basename(img_filename))[0]
    label_dict["id"] = img_basename
    label_dict["image"] = osp.join("data/VIRAT/VIRAT_S_000002", img_filename)

    label_dict["conversations"] = [
        {
            "role": "user",
            "content": "<image>\nHow many people are there? Answer with a single number."
        },
        {
            "role": "assistant",
            "content": f"{value}."
        }]

    return label_dict


label_dict = {"VIRAT_S_000002_002.jpg": 3,
              "VIRAT_S_000002_006.jpg": 3,
              "VIRAT_S_000002_014.jpg": 3,
              "VIRAT_S_000002_019.jpg": 6,
              "VIRAT_S_000002_024.jpg": 6,
              "VIRAT_S_000002_025.jpg": 7,
              "VIRAT_S_000002_028.jpg": 7,
              "VIRAT_S_000002_032.jpg": 6,
              "VIRAT_S_000002_039.jpg": 5,
              "VIRAT_S_000002_045.jpg": 5}

labels = [generate_conversations(img_filename, value) for img_filename, value in label_dict.items()]

with open('labels.json', 'w') as f:
    json.dump(labels, f, indent=2)
