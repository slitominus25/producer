
# coding: utf-8

# In[1]:


# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import csv
import requests
import sys
import os


def get_html(url):
    r = requests.get(url)
    return r.text


def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('div', class_='_2AYNOUj').find_all('a', class_='_3Z8s_NT')[-1].get('href')
    total_pages = pages.split('page/')[-1].split('/')[0]
    return int(total_pages)

def write_csv(data):
    print(data)
    with open('./lego.csv', 'a', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow((data['url']))

        
def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    ads = soup.find('div', class_='_10wErML').find_all('div', class_='_3u0dHrR _2dOsZar W0fxcbv')
    for ad in ads:
        #title,price,url
        try:
            title = ad.find('div', class_ ='_2RY-kBH').find('p', class_='_1rqTXk0').text.strip()
        except:
            title= ''
        try:
            url = 'https://www.detmir.ru/' + ad.find('div', class_ ='_1DPj93b _2dOsZar wemUAp6').find('a', class_='n7_2LXf _1jOYEtX').get('href')
        except:
            url = ''
        try:
            price = ad.find('div', class_='_3ZxvO6R _1h5mau7').find('p',class_='KfYbTjz').text
        except:
            price = ''
        data = {'url':u''+str(url)}
        write_csv(data)


def main():
    #https://www.detmir.ru/catalog/index/name/lego/
    url = 'https://www.detmir.ru/catalog/index/name/lego/'
    base_url = 'https://www.detmir.ru/catalog/index/name/lego/'
    page_part = 'page/'
    total_pages = get_total_pages(get_html(url))

    for i in range(1, total_pages):
        url_gen = base_url + page_part + str(i)
        #vprint(url_gen)
        html = get_html(url_gen)
        get_page_data(html)

if __name__ == '__main__':
    main()

