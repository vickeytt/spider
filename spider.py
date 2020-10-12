import json,os,re
import requests
from bs4 import BeautifulSoup

lis= ['cm_guonei','cm_guonei_02','cm_guonei_03']
num = 0
for i in lis:
    url = 'https://temp.163.com/special/00804KVA/{}.js?callback=data_callback'.format(i)
    #print(url)
    html = requests.get(url)
    str1 = html.text.strip().replace(" ", '').replace("\n", '')
    str2 = str1.lstrip('data_callback(')


    result = str2.strip(')')
    #print(result)

    # start = result.find('{"title"')
    # end = result.find('"add3":""}') + len('"add3":""}')
    data = json.loads(result)
    #print(data)

    for d in data:
        num += 1
        print(num)
        title = d["title"]
        print('新闻标题：',title)
        source =d["source"]
        print('新闻来源：',source)
        inerurl=d['docurl']
        #print(inerurl)
        html = requests.get(inerurl)
        soup = BeautifulSoup(html.text, 'lxml')
        divs1 = soup.select('.post_text')

        res1=''
        for r1 in divs1:
            res1+=r1.text.strip().replace(" ", '').replace("\n", '')
            print('新闻内容：',res1)
        divs2 = soup.select('.content')
        res2 = ''
        for r2 in divs2:
            res2 += r2.text.strip().replace(" ", '').replace("\n", '')
            print('新闻内容：', res2)

        # with open('neteasy.txt','a',encoding='utf8') as txtfile:
        #
        #     txtwriter =txt.writer(txtfile,delimiter='|')
        #
        #     txtwriter.writerow([title,source,res1,res2])









