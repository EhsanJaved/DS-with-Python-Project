import requests
from bs4 import BeautifulSoup
import pandas as pd
from caraddextracter_OLX import inrernaladd
from flask import Flask, request, jsonify, send_file

def OLX(records):
    mainURL = 'https://www.olx.com.pk'
    url = 'https://www.olx.com.pk/vehicles_c5?page=1&sorting=desc-creation'
    page_number = 1

    data_links = []

    # getting data 
    while len(data_links) < records:
        response = requests.get(url, params={'page': page_number})
        soup = BeautifulSoup(response.content, "html.parser")

        link_div = soup.find_all('div', {'class': 'a52608cc'})

        if not link_div:
            break

        for div in link_div[0].select("a"):
            data_links.append({'Links': div['href']})

            if len(data_links) >= records:
                break

        page_number += 1

    dfdata = pd.DataFrame(data_links)

    data_list = []

    for index, row in dfdata.iterrows():
        try:
            result = inrernaladd(mainURL + row['Links'])

            data_list.append(result)
            # return({index + 1})
            
        except Exception as e:
            return print(f"Error occurred while processing row {index + 1}: {e}")

    if data_list:
        dfdata = pd.concat(data_list, ignore_index=True)

    return  dfdata     