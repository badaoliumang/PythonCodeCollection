import requests
from requests import exceptions
from urllib.request import urlopen
from bs4 import BeautifulSoup
from wxpy import *
import  time
from threading import Timer
 
 
bot=Bot() #登陆网页微信，并保存登陆状态
 
def sendblogmsg(content):
    #搜索自己的好友，注意中文字符前需要+u
 
    my_group = bot.friends().search('发送好友的微信名')[0]
    my_group.send(content) #发送天气预报
 
def job():
    #要改为自己想要获取的城市的url，下面是青岛的url
    resp=urlopen('http://www.weather.com.cn/weather1d/101120201.shtml')
    soup=BeautifulSoup(resp,'html.parser')
    #获取温度数据
    tem=soup.find('p',class_="tem").find('span').string  #第一个包含class="tem"的p标签即为存放今天天气数据的标签
    #获取天气状况
    weather=soup.find('p',class_="wea").string 
    #获取风力情况
    win = soup.find('p',class_="win").find('span').string
    #获取日出时间
    sun = soup.find('p',class_="sun sunUp").find('span').string
    #拼接要发送的消息格式
    contents = '青岛今日：' +'\n' + '天气：'+weather + '\n'+'温度：'+tem+'℃'+ '\n'+'风力：'+win+ '\n'+sun +'\n'+'注意天气变化！！'
    sendblogmsg(contents)
    #设置每隔30秒发送一次，可以自己设置为一天的秒数
    t = Timer(30, job)
    t.start()

#定时
if __name__ == "__main__":
    job()
