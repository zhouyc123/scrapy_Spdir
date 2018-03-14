import scrapy
from ..items import ZufangItem


class GanjiSoider(scrapy.Spider):
    name = "zufang"
    start_urls =["http://bj.ganji.com/fang1/chaoyang/"]
    host_name = 'http://bj.ganji.com{}'

    def parse(self,response):
        zf = ZufangItem()

        print(response)
        title_list = response.xpath(".//div[@class='f-list-item ershoufang-list']/dl/dd[1]/a/text()").extract()
        money_list = response.xpath(".//div[@class='f-list-item ershoufang-list']/dl/dd[5]/div[1]/span[1]/text()").extract()
        for i,j  in zip(title_list,money_list):
            zf['title'] = i
            zf['money'] = j
            yield zf
         #   print(i,":",j)

        next_links = response.xpath(".//a[@class='next']/@href").extract()
        if len(next_links) >0 :
            next_link = self.host_name.format(next_links[0])
            print(next_link, '*******' * 20)
            yield scrapy.Request(next_link,callback=self.parse)
        else:
            pass
