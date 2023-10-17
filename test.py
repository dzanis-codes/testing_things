
Conversation opened. 2 messages. All messages read.

Skip to content
Using Gmail with screen readers
3 of 3,819
statement (7).pdf
Inbox

Janis Strazdins
AttachmentsWed, Oct 11, 12:50 PM (6 days ago)
 

Janis Strazdins <janis.strazdins@gmail.com>
Attachments
Mon, Oct 16, 5:10 PM (18 hours ago)
to Janis



On Wed, Oct 11, 2023 at 12:50 PM Janis Strazdins <dzanis@gmail.com> wrote:

 One attachment
  •  Scanned by Gmail
# -*- coding: utf-8 -*-


import time
from bs4 import BeautifulSoup
import json
import requests

import asyncio
import sqlite3
import traceback

from requests.structures import CaseInsensitiveDict
import requests_html




path = 'barbora.db'
conn = sqlite3.connect(path) 
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS results
           (name_id INTEGER PRIMARY KEY, produkta_id, prod_nosaukums, prod_cena, prod_kategorija, prod_isiedati, prod_pilniedati, avots, timestamp)''')
conn.commit()

def skaita_lapas(pagination):
    lapu_skaits =[]
    h_data = pagination.find_all("li")
    for hh in h_data:
        k_data = hh.find("a").text
        try:
            m_data = int(k_data)
        except Exception as e:
            m_data = 0
        lapu_skaits.append(m_data)
    return max(lapu_skaits)

def savaksana(url):
    #driver.get(url)
    session = requests_html.HTMLSession()
    
    #headers = CaseInsensitiveDict()
    #headers["Cookie"] = "region=barbora.lv"
    #response = requests.get(url, headers=headers)
    cookies = {'region': 'barbora.lv'}
    response = session.get(url, cookies=cookies)
    rendered_html = response.html.render()
    #print(response.html)  
    print(rendered_html)
    time.sleep(1)


    time.sleep(10)
    soup = BeautifulSoup(rendered_html, 'html.parser')
    print(soup)
    g_data = soup.find("ul", {"class": "pagination"})
    max_lapa = skaita_lapas(g_data)        
    item_data = soup.find_all("div", {"class": "b-product--wrap2 b-product--desktop-grid"})

    for item in item_data:
        produkta_isiedati = item.find("div")['data-b-units']
        produkta_pilniedati = item.find("div")['data-b-for-cart']
        pdati = json.loads(produkta_pilniedati)

        prod_id = pdati.get("id")
        prod_nosaukums = pdati.get("title")
        prod_cena = pdati.get("price")
        prod_kategorija = pdati.get("category_name_full_path")
        #print(produkta_pilniedati)
        prod_nr = pdati.get("product_position_in_list")
        print(prod_nr)
        print(prod_nosaukums, "..", prod_cena)
        avots = "barbora"
        ts = time.gmtime()
        timestamp = (time.strftime("%Y-%m-%d %H:%M:%S", ts))

        #šeit tiek apkopoti visi savāktie dati, tiek "izprintēti" bugfixing nolūkiem un tad tiek ievietoti datubāzē
        sql_entry = (str(prod_id), str(prod_nosaukums), str(prod_cena), str(prod_kategorija), str(produkta_isiedati), str(produkta_pilniedati), str(avots), timestamp)
        print(sql_entry)
        c.execute("INSERT INTO results VALUES (null, ?, ?, ?, ?, ?, ?, ?, ?)", sql_entry)
        conn.commit()
    return max_lapa







def main():
  linku_saraksts = ('https://www.barbora.lv/piena-produkti-un-olas/?order=SortByPopularity&page=1', 
                    'https://www.barbora.lv/augli-un-darzeni/?order=SortByPopularity&page=1',
                    'https://www.barbora.lv/maize-un-konditorejas-izstradajumi/?order=SortByPopularity&page=1',
                    'https://www.barbora.lv/gala-zivs-un-gatava-kulinarija/?order=SortByPopularity&page=1',
                    'https://www.barbora.lv/bakaleja/?order=SortByPopularity&page=1',
                    'https://www.barbora.lv/saldeta-partika/?order=SortByPopularity&page=1',
                    'https://www.barbora.lv/dzerieni/?order=SortByPopularity&page=1',
                    'https://www.barbora.lv/zidainu-un-bernu-preces/?order=SortByPopularity&page=1',
                    'https://www.barbora.lv/kosmetika-un-higiena/?order=SortByPopularity&page=1',
                    'https://www.barbora.lv/viss-tirisanai-un-majdzivniekiem/?order=SortByPopularity&page=1',
                    'https://www.barbora.lv/majai-un-atputai/?order=SortByPopularity&page=1')

  linka_nr = 0
  while linka_nr < len(linku_saraksts):
    headers = CaseInsensitiveDict()
    headers["Cookie"] = "region=barbora.lv"
    response = requests.get(linku_saraksts[linka_nr], headers=headers)
    time.sleep(2)
    soup = BeautifulSoup(response.content, 'html.parser')
    g_data = soup.find("ul", {"class": "pagination"})
    lapa = 1
    max_lapa = skaita_lapas(g_data)
    print(max_lapa)

        ##main funkcija 
    while lapa <= max_lapa:           
      url_part = "page=" + str(lapa)
      full_url = linku_saraksts[linka_nr]
      new_url = full_url.replace('page=1', url_part)
      print(url_part)
      max_lapa = savaksana(new_url)
      lapa += 1

  linka_nr += 1
        #driver.quit()
  time.sleep(5)


if __name__ == '__main__':
  main()
scraping barb.txt
Displaying scraping barb.txt.
