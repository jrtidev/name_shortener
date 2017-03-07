import requests
from bs4 import BeautifulSoup

clubs=[]
init_request = requests.get('http://football.ua/turkey.html')
soup = BeautifulSoup(init_request.content, 'html.parser')

content = soup.find('table',{'class':'tournament-table'})

for club in content.find_all('td', {'class':'team'}):
	club=club.get_text().strip('\n')
	if len(club)>10:
		club = club[:10]+'..'
		clubs.append(club)
		print(club)
	else:
		clubs.append(club)
		print(club)




