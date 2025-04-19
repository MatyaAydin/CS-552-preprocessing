from bs4 import BeautifulSoup
import requests


subject = "apple"
wikipedia_url = f"https://en.wikipedia.org/wiki/{subject}"
response = requests.get(wikipedia_url)

soup = BeautifulSoup(response.content, 'html.parser')


