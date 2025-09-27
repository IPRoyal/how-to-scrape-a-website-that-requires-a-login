# How to Scrape a Website That Requires a Login: Python Tutorial

**Author:** Eugenijus Denisov  
**Last updated:** August 29, 2025 • ~7 min read

This README condenses the article into a GitHub-friendly format. It shows how to log in with Python Requests, maintain a session, and scrape data from a protected page.  

---

## Why login scraping?
Some sites hide data behind authentication (forums, ecommerce, dashboards). With Requests, you can:  
- Create a session to store cookies/headers  
- Send a POST request with credentials  
- Reuse the session for subsequent GET requests  

⚠️ Always check Terms of Service before scraping. If ToS forbid scraping, you must not proceed.

---

## Step 1: Inspect the login form
Use browser DevTools (F12 → *Elements*) to find:  
- Authentication endpoint (usually from the `action` attribute in `<form>`).  
- HTTP method (often `POST`).  
- Field names (e.g., `username`, `password`).  

---

## Step 2: Install dependencies
```bash
pip install requests beautifulsoup4
```

---

## Step 3: Log in with a session
*Send a POST with credentials to authenticate.*
```python
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
```

---

## Step 4: Scrape data after login
*Reuse the session to fetch protected content.*
```python
data_url = 'https://practice.expandtesting.com/secure'
data_page = session.get(data_url)

if data_page.ok:
    print("Data retrieved successfully!")
    soup = BeautifulSoup(data_page.text, 'html.parser')
    first_paragraph = soup.find('h1')
    print("First text:", first_paragraph.text)
else:
    print("Failed to retrieve data.")
```

---

## Step 5: Handle common login issues
- **CSRF tokens**: may need an initial GET to extract token from headers or HTML.  
- **CAPTCHAs**: switch IPs, use automation, or CAPTCHA-solving services.  
- **2FA (two-factor authentication)**: use throwaway accounts with 2FA disabled, or handle custom flows.  

---

## Full Example
```python
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
```

---

## Notes
- Always check legality (ToS).  
- For JS-heavy or CAPTCHA-protected logins, switch to Selenium.  
- Sessions save cookies—always reuse the same session for authenticated requests.  

