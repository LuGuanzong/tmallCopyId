import requests
from bs4 import BeautifulSoup

import random


def getSentence():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    }
    i = random.randint(1, 21)
    link = 'https://www.juzikong.com/works/bb21ba71-2bb3-46fa-83fe-f8d50b7c8a6c?page=%d' % i
    try:
        r = requests.get(link, headers=headers, timeout=2)
    except:
        print('我的浪漫是：一起爬山看日出，夜晚喝点小酒在昏黄路灯下一起跳恰恰，黄昏开车去海边把车内音响调到最大，在晚饭洗完碗后触不及防地说我爱你。')
        return 0
    try:
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, "html.parser", )
            li = soup.find_all('div', class_="content_2hYZM")
            i = random.randint(0, 9)
            for sentence in li[i].stripped_strings:
                print(sentence)
        else:
            print('只要还有三两件热爱的事，人生便不算失败。')
    except:
        print('”事情能有多糟呢“，每当我面临焦虑不安的时候，我就这样问自己。再困难的事情它最终也会走向终止。'
              '所以不管有多少问题接踵而来，根据你自己的想法，一件一件去做就是了，不要把自己所经历的挫折太当回事儿了。')

    return 0
