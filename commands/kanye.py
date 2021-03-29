import json
import requests

kanye = requests.get('https://api.kanye.rest')
tweets = json.loads(kanye.text)

print('-'*len(tweets['quote']))
print('\n{0}\n'.format(tweets['quote']))
print('-'*len(tweets['quote']))
