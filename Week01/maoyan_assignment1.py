## 作业一：
## 安装并使用 requests、bs4 库
## 爬取猫眼电影的前 10 个电影名称、电影类型和上映时间
## 并以 UTF-8 字符集保存到 csv 格式的文件中

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

## 加入http请求的头部信息，来模拟浏览器
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'

header = {'user-agent':user_agent}

myurl = 'https://maoyan.com/films?showType=3'

## myurl相当于把我们的网址传递给requests库，等同于网址输入浏览器；参数headers，让requests库尽可能的去模拟浏览器
response = requests.get(myurl,headers=header)

## response.text 是完整的网页源代码内容；
## html.parser是对HTML的解析，是bs内置的默认解析方式
## 解析的结果存入变量bs_info
bs_info = bs(response.text, 'html.parser')

## 通过for循环，加入过滤条件

for movie_items in bs_info.find_all('div', attrs={'class':'movie-hover-info'},limit=10):
    ## 使用find提取需要的标签
    for movie_tags in movie_items.find_all('div', attrs={'class':'movie-hover-title'}):
        ## 获取电影名称
        movie_name = movie_tags.find_all('span', attrs={'class':'name'}).text
        ## 获取电影类型
        movie_type = movie_tags.find('span', attrs={'class':'hover-tag'}).text
        ## 获取电影上映日期
    for movie_tags2 in movie_items.find_all('div', attrs={'class':'movie-hover-title movie-hover-brief'}):    
        movie_date = movie_tags2.find('span', attrs={'class':'hover-tag'}).text

    movie_list = [movie_name, movie_type, movie_date]

    ## 信息保存

    maoyan_assignment1 = pd.DataFrame(data = movie_list)

    maoyan_assignment1.to_csv('./maoyan_assignment1.csv', encoding='utf8', index=False, header=False)




 







