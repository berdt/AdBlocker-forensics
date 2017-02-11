from bs4 import BeautifulSoup
import requests

amountOfPages = 4
top100Sites = list()

for i in range(amountOfPages):
    r = requests.get(f'http://www.alexa.com/topsites/countries;{i}/NL')
    soup = BeautifulSoup(r.text, 'html.parser')
    sites = soup.find_all('p', {'class':'desc-paragraph'})
    for site in sites:
        top100Sites.append(site.text.strip())

with open('top100sites2.txt', 'w') as sites:
    for site in top100Sites:
        sites.write(f'{site}\n')
