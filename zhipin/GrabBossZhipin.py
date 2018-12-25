import requests
from bs4 import BeautifulSoup
from lxml import etree

"""
学习xpath的使用

"""

class GrabBossZhipin():

    url="https://www.zhipin.com/job_detail/?query=爬虫&scity=101280600"
    headers = {
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.9",
        'cache-control': "no-cache",
        'postman-token': "99df9adb-6437-b62a-fd9d-59c4adf5354f"
    }

    response=requests.request("GET", url=url, headers=headers,)
    html=response.text
    print(html)
    print(type(html))


    def saveHtml(self):
        with open('zhipin.html', 'w', encoding='utf-8') as f:
            conten=f.write(self.html)


    def getData(self):
        # soup=BeautifulSoup(self.html, 'lxml')
        html=etree.HTML(self.html)
        print(html)
        job_title=html.xpath('//*[@class="job-title"]')
        job_price=html.xpath('//*[@id="main"]/div/div[3]/ul/li/div/div[1]/h3/a/span')
        job_price=html.xpath('')
        print(job_price)
        for i in job_price:
            print(i.text)

if __name__ == "__main__":
    # GrabBossZhipin().getData()
    GrabBossZhipin().saveHtml()