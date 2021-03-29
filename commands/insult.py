import json
import requests

r = requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json')
insult = json.loads(r.text)

print('-'*len(insult['insult']))
print('\n{0}\n'.format(insult['insult']))
print('-'*len(insult['insult']))