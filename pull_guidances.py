import requests
from bs4 import BeautifulSoup

URL = "https://www.sec.gov/corpfin/cfdisclosure#cfguidancetopics"

request = requests.get(URL)

soup = BeautifulSoup(request.content, 'html5lib')

article_body_div = soup.find("div", {"class": "article-body"})

for link in article_body_div.find_all("a", {"href": True}):
  if 'https' in link.attrs['href']:
    request = requests.get(link.attrs['href'])
  else:
    request = requests.get(f'https://sec.gov{link.attrs["href"]}')
  guidance_article_soup = BeautifulSoup(request.content, 'html5lib')
  with open(f'./docs/guidances/cf_disclosure_guidance_topics/{guidance_article_soup.find("title").get_text()}.html', 'w') as f:
    f.write(guidance_article_soup.get_text())