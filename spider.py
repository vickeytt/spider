import json,os,re
import requests
from bs4 import BeautifulSoup

lis= ['cm_guonei','cm_guonei_02','cm_guonei_03']
for i in lis:
    url = 'https://temp.163.com/special/00804KVA/{}.js?callback=data_callback'.format(i)
    print(url)
    html = requests.get(url)
    str1 = html.text.strip().replace(" ", '').replace("\n", '')
    str2 = str1.lstrip('data_callback(')


    result = str2.strip(')')
    print(result)
    print(type(result))
    # start = result.find('{"title"')
    # end = result.find('"add3":""}') + len('"add3":""}')
    data = json.loads(result)
    print(data)
    print(type(data))

    for d in data:
        title = d["title"]
        print(title)
        source =d["source"]
        print(source)
        inerurl=d['docurl']
        print(inerurl)
        html = requests.get(inerurl)
        soup = BeautifulSoup(html.text, 'lxml')
        divs = soup.select('.HotList-item')


