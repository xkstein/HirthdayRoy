import json
class File():
    def __init__(self, contents, container):
        self.contents = {}
        self.container = container


json_data = '{"name": "Brian", "city": "Seattle"}'
python_obj = json.loads(json_data)
print(python_obj["name"])
print(python_obj["city"])

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}
    
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)

with open("data_file.json","r") as read_file:
    meme = json.load(read_file)

print(meme)
