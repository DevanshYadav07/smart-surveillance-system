import html_to_json
import requests
import json

html_string = requests.get('https://tedxgraphicerauniversitywomen.com/').text
print(html_string)

output_json = html_to_json.convert(html_string=html_string)

print(output_json)
# pickle.dump(output_json, './data.json')

with open('data.json', 'w') as data:
    data.write(json.dumps(output_json, indent=4))