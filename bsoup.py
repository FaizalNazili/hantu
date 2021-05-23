from bs4 import BeautifulSoup as bs
import requests

DOMAIN = 'https://github.com/'
URL ='https://github.com/budimm/pythoncode-tutorials/tree/master/machine-learning/speech-recognition'
FILETYPE = '.wav'

def get_soup(url):
    return bs(requests.get(url).text, 'html.parser')

for link in get_soup(URL).find_all('a'):
    file_link = link.get('href')
    if FILETYPE in file_link:
        print(file_link)
        with open(link.text, 'wb') as file:
            response = requests.get(DOMAIN + file_link)
            file.write(response.content)