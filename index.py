import requests
from bs4 import BeautifulSoup
import csv
import urllib3

urllib3.disable_warnings()

HOST = 'https://www.goszakup.gov.kz/'
URL = 'https://www.goszakup.gov.kz/ru/registry/rqc'
HEADERS = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params,verify=False)
    return r
def get_content(html):
    soup=BeautifulSoup(html,'html.parser')
    items=soup.find_all('tr')
    
    sup=[]
    for item in items:
      sup.append({
          'title':item.a['strong'].get_text
      })
    return sup
