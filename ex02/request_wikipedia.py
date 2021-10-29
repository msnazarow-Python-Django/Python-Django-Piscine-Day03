#!/usr/bin/python3
import requests, json, sys
from dewiki.parser import Parser


def parse_data(text):
	try:
		data = list(json.loads(text)['query']['pages'].values())[0]['revisions'][0]['*']
	except:
		data = json.loads(text)['parse']['wikitext']['*']
	return Parser().parse_string(data)

def wiki_find(search_string):
	endpoint = 'https://en.wikipedia.org/w/api.php'
	queries = {
		'page': search_string,
		'action': 'parse',
		'prop': 'wikitext',
		'format': 'json',
		'redirects': 'true',
	}
	resp = requests.get(endpoint, params=queries)
	return resp


def main(argv):
	try:
		resp = wiki_find(argv[1])
		if not resp.ok:
			raise ConnectionError
		with open(f'{argv[1].replace(" ", "_")}.wiki', 'w') as file:
			file.write(parse_data(resp.text))
	except KeyError:
		print('No results found')
	except IndexError:
		print("Error: Required one parameter to execute")
	except Exception as e:
		print(e)

if __name__ == '__main__':
	main(sys.argv)