import requests
from bs4 import BeautifulSoup

def main():


	url='https://www.theguardian.com/uk'
	response = requests.get(url)

	soup = BeautifulSoup(response.text, 'html.parser')
	headlines = soup.find('body').find_all('h3')
	for x in headlines:
	    print(x.text.strip())


if __name__ == '__main__':
	main()