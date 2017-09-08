import os
import sys
import getopt
from docopt import docopt
from termcolor import cprint
from bs4 import BeautifulSoup
from pyfiglet import figlet_format

os.system('clear')

try:
	import requests
except:
	print 'Request library not found, please install before proceeding\n'
	sys.exit()

invalid = [
	'Poloniex Wallet',
	'liqui.io',
	'ENS-Registrar'
]

def img():
	cprint(figlet_format('whale-watcher', font='slant'), 'blue')


def header():
	img()
	print '			   author: waymobetta'
	print ''
	print ''
	print ''

def usage():
	print 'Usage: whale-watcher'
	print ''
	print 'Leverage whale-watcher to find the most recent crowdsales an Ethereum account has participated in'
	print ' -f: Fetch most recent transactions'
	print ' -c: Use previously cached (local) transactions'
	print ''

def start():
	if sys.argv[1] == '-f':
		header()
		fetch()
	elif sys.argv[1] == '-c':
		header()
		local()
	else:
		header()
		usage()
		sys.exit()

def fetch():
	addr = raw_input('Input address to investigate: ')
	print ''
	url = 'https://etherscan.io/txs?a=' + addr
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	with open('test.html', 'w') as file:
		file.write(str(soup))

	addresses = soup.find_all('span', class_='address-tag')
	for i in range(0,len(addresses)):
		sig = addresses[i]
		if sig.string.startswith('0x'):
			continue
		elif sig.string[0].isdigit():
			continue
		elif sig.string not in invalid:
			print 'Crowdsale: ', sig.string

def local():
	try: 
		with open('test.html') as sp:
			cached = BeautifulSoup(sp, 'lxml')
	except:
		print 'Error: no local copy found.\nRe-run with fetch flag (-f) to grab new transaction history' # need fix
		sys.exit()

	addresses = cached.find_all('span', class_='address-tag')
	print ''
	print 'Cached results:'
	print ''
	for i in range(0,len(addresses)):
		sig = addresses[i]
		if sig.string.startswith('0x'):
			continue
		elif sig.string[0].isdigit():
			continue
		elif sig.string not in invalid:
			print 'Crowdsale: ', sig.string

if __name__ == '__main__':
	start()


# below for future testing

"""
for i in range(0,len(data)):
	sig = addresses[i]

	if sig.string[0].isdigit():
		# print 'Block: ', strang
		continue
	else:
		print 'Crowdsale: ', sig.string

table = soup.find('tbody')
print table.prettify()

addr = table.find_all('td', class_='address-tag')

for i in range(0,len(addr)):
	sig = addr[i]
	if sig.string[0].isdigit():
		print sig.string
	else:
		print 'Crowdsale: ', sig.string

ct = single.string
tit = single['title']
print 'Addr: ', tit
print 'Contract: ', ct
"""