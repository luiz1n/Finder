import os

def Check():
	try:
		import requests
	except ImportError:
		os.system("python -m pip install requests")
	except Exception:
		pass
Check()
import requests

def Finder():
	try:
		url = input('URL: ')
		for word in open('wordlist.txt', 'r'):
			r = requests.get(f'{url}/{word}')
			if '404' in r.text:
				print(f'{url}/{word} -> Falha!')
			else:
				print(f'{url}/{word} -> Sucesso!')
	except KeyboardInterrupt:
		exit()
		os.close()

Finder()
