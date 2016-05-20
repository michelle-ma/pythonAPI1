# pythonAPI1
disney=open('disney.txt').read()
import json
jsondisney=json.loads(disney)

for i in jsondisney['attributes']:
    print(i['displayName'], i['attributeId'])
