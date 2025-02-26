from bs4 import BeautifulSoup
import requests
url = 'https://www.bbc.com/sport/football/scores-fixtures/2025-03-04'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')
clubs = ['Real Madrid', 'Bayern Munich', 'Barcelona', 'Arsenal', 'Manchester City', 'Liverpool', 'Atlético Madrid']
matches = soup.find_all('span', class_ = 'visually-hidden ssrcss-1f39n02-VisuallyHidden e16en2lz0')
for match in matches:
    text = match.text
    if 'kick off' in text:
        print(text)
