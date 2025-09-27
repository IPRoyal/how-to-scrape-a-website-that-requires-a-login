import requests
from bs4 import BeautifulSoup

# Create a session object
session = requests.Session()

# Add login data
login_url = 'https://practice.expandtesting.com/authenticate'
credentials = {
    'username': 'practice',
    'password': 'SuperSecretPassword!'
}

# Send POST request
response = session.post(login_url, data=credentials)
if response.ok:
    print("Login successful!")
else:
    print("Login failed!")
