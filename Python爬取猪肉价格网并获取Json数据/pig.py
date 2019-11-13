import requests
import json

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}


def get_json(url):
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            json_text=response.json()
            return json_text
    except Exception:
        print('获取json接口有问题！')
        return None


json_data = get_json('http://zhujia.zhuwang.cc/index/api/chartData?areaId=370000&aa=1573300145544')


# 将dict格式数据转换成json格式字符串
dump_data = json.dumps(json_data)

# 将json格式字符串转换成对应的python值
load_data = json.loads(dump_data)




# 打印转换结果
print(type(json_data))
print(type(dump_data))
print(type(load_data),load_data)
