import requests
from bs4 import BeautifulSoup

goodbad = {'zero':'loads of', "'unjustified'":'very justified', 'failure':'success', 'mass':'no', 
			'shortages':'surpluss', 'homeless':'millionaies', 'overlooked':'helped', 'kills':'saves', 
			'kill':'marry', 'warn':'remind', 'slow-motion':'really fast paced', 'deaths;':'puppies', 'ugly':'beatiful',
			'murder':'hug', 'murdered':'hugged', 'bad':'good', 'sad':'happy', 'sorry':'extatic', 'drowning':'flying', 
			'crash':'party', 'killed':'married', 'concerning':'exciting', 'killing':'saving', 'warns':'announces',
			'hospital':'theme park', 'knifepoint':'a cake', 'gunpoint':'a cake', 'covid':''}

def main():

	headlines = []
	newheadlines = []

	url='https://www.theguardian.com/uk'
	

	response = requests.get(url)

	soup = BeautifulSoup(response.text, 'html.parser')
	heads = soup.find('body').find_all('h3')
	for x in heads:
		headlines.append(x.text.strip().lower())
		headlines = headlines[0:100]

	for j in headlines:
		if (any(x in j for x in goodbad.keys())):
			h = j.split(' ')
			replacer = goodbad.get
			newsentence = [replacer(n,n) for n in h]
			newheadlines.append(' '.join(newsentence))


	#only show nicer headlines
	for h in newheadlines:
		print(h)
	





if __name__ == '__main__':
	main()
