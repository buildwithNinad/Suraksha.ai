import requests
from bs4 import BeautifulSoup

def fetch_cves():
    url = "https://cve.mitre.org/data/downloads/allitems.html"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        return "Sample CVE data extracted here..."
    else:
        return "Failed to fetch CVE data"