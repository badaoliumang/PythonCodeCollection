import os
#导入request库
import requests
#导入Beautiful Soup库
from bs4 import BeautifulSoup as BS

#定义获取数据的方法
def Get_data():
    #设置请求头headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'cookie': 'acw_tc=6f3e47cc15498749418558688e3d6410ea97be9a552b180841c5079605; PHPSESSID=s2hjdg3slh32omchfsib4himk0; UM_distinctid=168dbbfe8c533e-0e42df11c1c0a7-9393265-100200-168dbbfe8c71088; CNZZDATA1256319371=345851669-1549873534-%7C1549873534; CNZZDATA1257119496=134880590-1549870452-%7C1549870452; Hm_lvt_a48e6ab107a4e68d47e6fdb5d83961e5=1549875015; Hm_lvt_3c8ecbfa472e76b0340d7a701a04197e=1549875021; CNZZDATA1254708131=653924416-1549874976-%7C1549874976; CNZZDATA1275922735=1673340420-1549874690-%7C1549874690; CNZZDATA1257131565=1820590917-1549873827-%7C1549873827; CNZZDATA1257125147=1301871275-1549871347-https%253A%252F%252Fwww.duanwenxue.com%252F%7C1549871347; Hm_lpvt_a48e6ab107a4e68d47e6fdb5d83961e5=1549875906; Hm_lpvt_3c8ecbfa472e76b0340d7a701a04197e=1549875913; ajax_award_timestamp=1549875887; ajax_award_timestamp__ckMd5=706904497e9c8dfd; ajax_award_key=94a17405d22ab8aacbabbbfdb9d4740c; ajax_award_key__ckMd5=3e97bde02ab1998d',
        'referer': 'https://www.duanwenxue.com/huayu/tianyanmiyu/list_69.html',
        'upgrade-insecure-requests' : '1',
    }
    #根据url中最后数字的不同循环获取情话并调用parse_text写入文件
    for i in range(1,70):
        #使用format可以将i作为占位符的{}里面的内容并填入
        url = 'https://www.duanwenxue.com/huayu/tianyanmiyu/list_{}.html'.format(i)
        #调用requests的get方法爬取内容
        response = requests.get(url,headers=headers)
        #调用parse_text方法来解析网页内容
        parse_text(response.text)


def parse_text(text):
    articles = []
    if text:
        #使用lxml解析器，常用的解析html的解析器
        soup = BS(text,'lxml')
        #调用find方法来首先找到class为list-short-article的div元素再找到target属性为blank的a标签
        arttis = soup.find('div', class_='list-short-article').find_all('a', {'target': "_blank"})
        #这里是通过列表推导式以及for循环获取到每个a标签里面的text内容并通过strip去除空格
        articles = [arttis[i].text.strip() for i in range(len(arttis)) ]
    #将解析后的网页内容存放在text文件中
    #a：表示打开一个文件用于追加。如果该文件已经存在，文件指针会放在文件末尾，也就是说文件内容会被写入到已有内容之后
    #如果该文件不存在，创建新文件进行写入
    with open('Love_words.txt','a',encoding='utf-8') as f:
        for i in articles:
            #每一条内容后面追加换行符
            f.write(i+'\n')


if __name__ == '__main__':
    os.remove('Love_words.txt')
    Get_data()
