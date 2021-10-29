#!/usr/bin/python3
import sys, requests
from bs4 import BeautifulSoup


def find_next_link(data: BeautifulSoup):
	paragraphs = data.find('div', id="mw-content-text").findAll('p')
	brackets = False
	for one in paragraphs:
		check = one.findAll('a', style=lambda value: value and 'italic' in value)
		for elem in one.contents:
			brackets = (brackets or '(' in elem) and not ')' in elem
			if brackets:
				continue
			try:
				ref = elem.get('href')
				if not '/wiki/Help:' in ref and not '/wiki/File:' in ref and ref.startswith('/wiki'):
					return ref
				# refs = list(filter(
				# 	lambda ref: not '/wiki/Help:' in ref and not '/wiki/File:' in ref and ref.startswith('/wiki'),
				# 	map(lambda ref: ref.get('href'), elem)))
				# return refs[0]
			except:
				pass
	return None


def find_article_name(data: BeautifulSoup):
	name = data.find('h1', id='firstHeading').text
	return name


def wiki_find(wiki_search_text):
	url = f"http://en.wikipedia.org/{wiki_search_text}"
	resp = requests.get(url)
	return resp


def main(argv):
	try:
		search_text = f"wiki/{argv[1].replace(' ', '_')}"
		articles = []
		while True:
			resp = wiki_find(search_text)
			if not resp.ok:
				raise ConnectionError("No result found")
			soap = BeautifulSoup(resp.text, 'html.parser')
			search_text = find_next_link(soap)
			if not search_text:
				print("It leads to a dead end!")
				return
			article_name = find_article_name(soap)
			print(article_name)
			if article_name in articles:
				print('It leads to an infinite loop !')
				return
			articles.append(article_name)
			if article_name == 'Philosophy':
				print(str(len(articles)) + " road(s) from " + articles[0] + " to philosophy!")
				return
	except KeyError:
		print('No results found')
	except IndexError:
		print("Error: Required one parameter to execute")
	except Exception as e:
		print(e)


if __name__ == '__main__':
	main(sys.argv)
