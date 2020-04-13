import requests
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/coronavirus/country/ireland/"
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/81.0.4044.92 Chrome/81.0.4044.92 Safari/537.36"}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
recovered_text = soup.find_all(id="maincounter-wrap")[2].get_text()
result_text = recovered_text.strip().replace("Recovered:", "")
num = int(result_text)
print("Recovered cases : " + str(num))
