# String into Dictionary
import json
str = '{"Country": "Ukraine", "Capital": "Kiev", "Large Cities": "Kiev, Kharkiv and Lviv"}'
convertedDict = json.loads(str)
print(convertedDict)
print(type(convertedDict))
