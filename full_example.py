import requests
from bs4 import BeautifulSoup

session = requests.Session()

login_url = 'https://practice.expandtesting.com/authenticate'
credentials = {
    'username': 'practice',
    'password': 'SuperSecretPassword!'
}
response = session.post(login_url, data=credentials)
if response.ok:
    print("Login successful!")
else:
    print("Login failed!")

data_url = 'https://practice.expandtesting.com/secure'
data_page = session.get(data_url)

if data_page.ok:
    print("Data retrieved successfully!")
    soup = BeautifulSoup(data_page.text, 'html.parser')
    first_paragraph = soup.find('h1')
    print("First text:", first_paragraph.text)
else:
    print("Failed to retrieve data.")
