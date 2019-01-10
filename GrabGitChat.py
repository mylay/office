import requests
from lxml import etree

class GrabGitChat():


    def geHtml(self):
        try:
            url = "https://gitbook.cn/gitchat/free"

            headers = {
                'Host': "gitbook.cn",
                'Connection': "keep-alive",
                'Cache-Control': "max-age=0",
                'Upgrade-Insecure-Requests': "1",
                'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
                'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                'Accept-Encoding': "gzip, deflate, br",
                'Accept-Language': "zh-CN,zh;q=0.9",
                'cache-control': "no-cache",
                'Postman-Token': "719fe353-0ccf-46a3-a84e-4b7871285de2"
            }

            response = requests.request("GET", url, headers=headers)
            html=response.text
            # print(html)
            return html
        except Exception as e:
            print(e)
            print("请求错误")

    def getContent(self):
        # try:
        html = etree.HTML(self.geHtml())
        data = html.xpath('//div[@class="col-md-12"]')
        print(data)
        # for i in data:

        # print(html)
        # data = html.xpath('//*[@id="itemContainer"]')
        # for i in data[0]:
        #     print(i)
        #     article_url=i.xpath('/div/a/@href')
        #     print(article_url)
        # except Exception as e:
        #     print(e)l
        #     print("没有数据解析")




GrabGitChat().getContent()