#!/usr/bin/env python

import os
import sys
import argparse
from termcolor import cprint
from bs4 import BeautifulSoup
from pyfiglet import figlet_format

os.system('clear')

try:
    import requests
except:
    sys.exit('[!] Requests library not found, please install before proceeding: pip install requests\n')


# todo: add additional non-contract addresses (i.e. exchanges)
invalid = [
    'Poloniex Wallet',
    'liqui.io',
    'ENS-Registrar',
    'Kraken_4',
    'Bittrex',
    'Bitfinex_Wallet1'
]

def img():
    cprint(figlet_format('whale-watcher', font='slant'), 'blue')

def header():
    img()
    print '			author: waymobetta'
    print ''
    print ''
    print ''

def usage():
    print('Usage: whale-watcher')
    print('')
    print('Leverage whale-watcher to find the most recent crowdsales an Ethereum account has participated in')
    print('')

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
        sys.exit('[!] no local copy found.\nRe-run with fetch flag (-f) to grab new transaction history') # need fix

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
    usage = '''%(prog)s [-f fetch] [-c cached]\n\nexample:\n./whale_watcher.py -f <public address>'''
    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument('-f', '--fetch', action='store_true', help='Fetch most recent transactions', dest='fetch')
    parser.add_argument('-c', '--cached', action='store_true', help='Use previously cached (local) transactions', dest='cached')
    args = parser.parse_args()

    # set constructors
    fetched = args.fetch
    cached = args.cached

    if len(sys.argv) == 1:
        header()
        parser.print_help()
        sys.exit(1)
   
    if fetched:
        header()
	fetch()
    else:
        header()
	local()



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
