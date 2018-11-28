import urllib.request
import urllib.parse
import json

content=input('需要翻译的内容:')
#翻译内容

url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom=http://fanyi.youdao.com/'
#有道翻译查询入口
data = {        #表单数据
            'i': content,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_CLICKBUTTION',
            'typoResult': 'false'
        }

data=urllib.parse.urlencode(data).encode('utf-8')
#对POST数据进行编码

response=urllib.request.urlopen(url,data)
#发出POST请求并获取HTTP响应

html=response.read().decode('utf-8')
#获取网页内容，并进行解码解码

target=json.loads(html)
#json解析

print("\n翻译结果:%s"%target['translateResult'][0][0]['tgt'])
#输出翻译结果
