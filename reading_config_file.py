import json

with open("config.json", "rb") as read_file:
    configFile = json.load(read_file)

excel_file_path = (configFile['ExcelFilePath'])
