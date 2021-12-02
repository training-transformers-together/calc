import json

with open(
    "/mnt/storage/Documents/hugging_face/colaborative_hub_training/demo_neurips/training-transformers-together-dashboard/data/"
    "serializaledata_V2.json",
    "r",
) as f:
    serialized_data = json.load(f)

usernames = []
for item in serialized_data["points"][0]:
    usernames.append(item["profileId"])

print(usernames)
