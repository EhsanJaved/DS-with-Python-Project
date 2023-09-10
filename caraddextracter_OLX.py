# ready
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def remove_tags(text):
    clean_text = re.sub(r"<.*?>", "", text)
    return clean_text.strip()

def inrernaladd(ad_url):
    response = requests.get(ad_url)
    response.encoding = 'utf-8'  # Explicitly set the encoding
    soup = BeautifulSoup(response.content.decode('utf-8'), "html.parser")
    # soup = BeautifulSoup(response.content, "html.parser")
    listings = soup.find_all('div', {'class': 'b44ca0b3'})
    data_list = [item.prettify() for item in listings]
    

# Create an empty dictionary to store the key-value pairs
    data_dict = {}

    # Process each string in the list
    for item in data_list:
        spans = item.split("<span>")
        key = remove_tags(spans[1])
        value = remove_tags(spans[2])
        data_dict[key] = value

    # Convert the dictionary to a pandas DataFrame
    df = pd.DataFrame([data_dict])
    # df.append
    # pd.concat
    return df