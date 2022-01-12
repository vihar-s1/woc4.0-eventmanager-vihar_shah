# Displaying Usage of atleast one python Library

import urllib.request
import os
from bs4 import BeautifulSoup

url = input('Enter URL: ')

while True:
    try:
        url_handler = urllib.request.urlopen(url)
        break
    except ValueError:
        print('Unknown URL or URL-type found!!')
        choice = None
        
        while choice != 'y' or choice != 'Y' or choice != 'N' or choice != 'n':
            print('Want to Retry?(y/n)')
            choice = input()
        
        if choice == 'n' or choice == 'N':
            break

url_bs = BeautifulSoup(url_handler, 'html.parser')
print('\n\nLinks Found ON the web-page at URL-[', url,']:\n\n')
for link in url_bs('a'):
    print(link.get('href', None),'\n')
