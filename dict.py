import json
with open ("output.json","r") as dict: 
   data = json.load(dict)
tukhoa = input("nhập từ khóa tiếng anh cần tìm kiếm: ")
if tukhoa in (data['entries'['part'['meaning']]]):
    print(True)
else:
    print(False)
