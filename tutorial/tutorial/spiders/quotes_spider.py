import scrapy
import re

class QuotesSpider(scrapy.Spider):
    name = "quotes_EL"

    url = 'https://snapr.bis.doc.gov/stela/view-application;jsessionid=EEE7D84DAF40BF8409495CC092DE0C0F?number=z'
    # case id format: z1234567, put the number part here.
    caseId = 1234567
    num = 2
    start_urls = []
    # support batch check
    # eg. 2 means, two id will be check here, 1234567, 1234568
    for x in range(num):
        start_urls.append(url+str(caseId))
        caseId += 1

    def parse(self, response):
        title = response.css('div.login-header::text').re(r'ACN:\s\w\d+')[0]
        # print(title)        
        rows = response.css('table#appInfo td')
        line = []
        for row in rows:
            line.append(row.css('td::text').get().strip())
            lis = row.css('ul li')
            for l in lis:
                stringBuilder = ''
                strs = l.css('li::text').getall()
                for s in strs:
                    s = s.strip()
                    stringBuilder += s + ' '
                    if s == 'Referred to':
                        stringBuilder += l.css('strong::text').get() + ' '
                # print(stringBuilder)
                line.append(stringBuilder)


        yield{
            'ID' : title,
            'Info' : line, 
        }

