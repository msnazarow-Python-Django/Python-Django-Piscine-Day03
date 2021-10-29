#!/usr/bin/python3
import sys
from antigravity import geohash


def main(argv):
	try:
		latitude = float(argv[1])
		longitude = float(argv[2])
		date = argv[3].encode('UTF-8')
		return geohash(latitude, longitude, date)
	except IndexError:
		print("Error: Required three parameters to execute")
	except Exception as e:
		print(e)


if __name__ == '__main__':
	main(sys.argv)
