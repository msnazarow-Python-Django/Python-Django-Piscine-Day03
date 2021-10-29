#!/usr/bin/python3
from local_lib.path import *


def main():
	try:
		folder = Path('some_folder')
		if not folder.isdir():
			folder.mkdir()
		file = folder / 'some_file'
		if not file.isfile():
			file.touch()
		file.write_text("Lol kek")
		print(file.read_text())
	except Exception as e:
		print(e)


if __name__ == '__main__':
	main()
