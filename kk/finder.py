import requests
try:
	url = input('URL: ')
	if 'http://' in url:
		url = url.split('http://')
		url = url[1].split('/')
	elif "https://" in url:
		url = url.split('https://')
		url = url[1].split('/')
	url = url[0]
	arch = open('wordlist.txt', 'r')
	for w in arch:
		w = w.strip()
		d = 'http://'+url+'/'+w
		r = requests.get(d)
		status = r.status_code
		if status == 200:
			print(f'{d} => Status: {status} (Sucesso!)')
		else:
			print(f'{d} => Status: {status} [ Falha :( ]')
except KeyboardInterrupt:
	print('Saindo...')
	exit()