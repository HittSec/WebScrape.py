import requests
from bs4 import BeautifulSoup

# URL of the website to be scraped
url = "https://www.exampleurl.com"

# Send a GET request to the URL and store the response
response = requests.get(url)

# Use BeautifulSoup to parse the HTML content of the response
soup = BeautifulSoup(response.content, "html.parser")

# Find all the items on sale
items = soup.find_all("div", class_="free-item")

# Print the details of each item on sale
for item in items:
    name = item.find("h3").text
    price = item.find("span", class_="price").text
    discount = item.find("span", class_="discount").text
    print(f"Item Name: {name}")
    print(f"Price: {price}")
    print(f"Discount: {discount}")
    print("\n")