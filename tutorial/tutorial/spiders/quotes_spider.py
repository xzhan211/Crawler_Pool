import scrapy
import re

class QuotesSpider(scrapy.Spider):
    name = "quotes_EL"

    # start_urls = ['https://www.fairfaxcounty.gov/fido/complaints/comp_display.aspx?type=addr&addrkey=1593968&cnt=1&stno=&stname=BABASHAW']

    # def parse(self, response):
    #     rows = response.css('table.tbBorder tr')
    #     for row in rows:
    #         print(row.css('td.colTitle::text').getall())
    #         print(row.css('td span::text').get())
    url = 'https://snapr.bis.doc.gov/stela/view-application;jsessionid=EEE7D84DAF40BF8409495CC092DE0C0F?number=z'
    num = 1626745
    start_urls = []
    for x in range(2):
        start_urls.append(url+str(num))
        num += 1
    
    # def parse(self, response):
    #     title = response.css('div.login-header::text').re(r'ACN:\s\w\d+')[0]
    #     print(title)        
    #     rows = response.css('table#appInfo td')
    #     for row in rows:
    #         line = row.css('td::text').get().strip()
    #         print(line)

    #     print('------------')

    def parse(self, response):
        title = response.css('div.login-header::text').re(r'ACN:\s\w\d+')[0]
        # print(title)        
        rows = response.css('table#appInfo td')
        line = []
        for row in rows:
            line.append(row.css('td::text').get().strip())
            # print(line)
        yield{
            'ID' : title,
            'Info' : line, 
        }

