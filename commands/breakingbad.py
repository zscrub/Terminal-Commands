import json
import requests

get_quote = requests.get('https://breaking-bad-quotes.herokuapp.com/v1/quotes')
quote_ = json.loads(get_quote.text)

quote = quote_[0]['quote']
author = quote_[0]['author']

print()
print('-'*len(quote))
print('{0}\n-{1}'.format(quote, author))
print('-'*len(quote))
