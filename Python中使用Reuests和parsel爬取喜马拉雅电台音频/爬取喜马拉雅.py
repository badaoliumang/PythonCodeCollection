
#能发送http请求的库
import requests
import parsel
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}

def download_meida(media_url,media_name):
    response = requests.get(media_url,headers = headers);
    with open(f'{media_name}.mp4',mode='wb') as f:
        f.write(response.content)

#media_url = 'http://audio.cos.xmcdn.com/group47/M0A/34/EA/wKgKm1tHj6GwgeWBAFehkfjyvKI181.m4a'
#download_meida(media_url,'badao');

#https://www.ximalaya.com/revision/play/v1/audio?id=98791745&ptype=1
def media_api(track_id):
    api_url =f'https://www.ximalaya.com/revision/play/v1/audio?id={track_id}&ptype=1';
    response = requests.get(api_url,headers = headers)
    #print(response.json())
    #json返回字典类型  提取使用[]
    data_json = response.json()
    src = data_json['data']['src']
    return src

#print(media_api(98791745))

def get_total_page(page_url):
    #请求页面
    response = requests.get(page_url,headers = headers)
    print(response.text)
    #获取页面html的内容
    sel = parsel.Selector(response.text)
    print(sel)
    #通过css选择器找到a标签   .sound-list代表 class属性为sound-list 然后下面的ul 下的li 下的a
    sound_list = sel.css('.sound-list ul li a')
    print(sound_list)
    #只有前30个是页面链接 截取前30个
    for sound in sound_list[:30]:
        #extract_first()将对象中的文字提取出来
        #获取a标签的href属性的内容
        media_url = sound.css('a::attr(href)').extract_first()
        #/youshengshu/16411402/98791745 --只去最后面的id
        media_url = media_url.split('/')[-1]
        # 获取a标签的title属性的内容
        media_name = sound.css('a::attr(title)').extract_first()
        #用yield将整个循环的内容返回
        yield media_url,media_name

if __name__ == '__main__':
    #循环页数下载 range代表下载的页数范围
    for page in range(2,3):
        meidas = get_total_page(f'https://www.ximalaya.com/youshengshu/16411402/p{page}')
        for media_id,media_name in meidas:
            #print(media_url, media_name)
            media_url = media_api(media_id)
            download_meida(media_url, media_name)


