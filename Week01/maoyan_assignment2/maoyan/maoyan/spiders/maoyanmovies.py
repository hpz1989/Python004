import scrapy
from maoyan.items import MaoyanItem
from scrapy.selector import Selector


class MaoyanmoviesSpider(scrapy.Spider):
    ## 定义爬虫名称
    name = 'maoyanmovies'
    allowed_domains = ['maoyan.com']
    ## 起始URL
    start_urls = ['https://maoyan.com/films?showType=3']

##     注释掉默认的parse函数
##     def parse(self, response):
##        pass
    
    ## url请求访问的地址，callback回调函数
    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse)

    ## 解析函数
    def parse(self, response):
        i = 1
        movie_items = MaoyanItem()
        movies = Selector(response=response).xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd/div[1]/div[2]/a/div')  ## 把整个页面当成xml来处理

        for movie in movies:
            if i > 10:
                break
            else:
                movie_name = movie.xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd/div[1]/div[2]/a/div/div[1]/span[1]/text()')
                movie_type = movie.xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd/div[1]/div[2]/a/div/div[2]/text()')
                movie_date = movie.xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd/div[1]/div[2]/a/div/div[4]/text()')

            movie_items['movie_name'] = movie_name
            movie_items['movie_type'] = movie_type
            movie_items['movie_date'] = movie_date

            i = i+1
            yield movie_items

