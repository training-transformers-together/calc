import json
import random

with open(
    "/mnt/storage/Documents/hugging_face/colaborative_hub_training/demo_neurips/training-transformers-together-dashboard/data/"
    "serializaledata.json",
    "r",
) as f:
    serialized_data = json.load(f)

serialized_data_v2 = serialized_data
serialized_data_v2["points"] = [[item for item in serialized_data["points"][-1] if random.random() > 0.8]]

with open(
    "/mnt/storage/Documents/hugging_face/colaborative_hub_training/demo_neurips/training-transformers-together-dashboard/data/"
    "serializaledata_V2.json",
    "w",
) as f:
    f.write(json.dumps(serialized_data_v2))
