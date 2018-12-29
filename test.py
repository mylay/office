import requests
from lxml import etree
import re
import time

url_prefix = "http://www.zhipin.com"
list = []
i = 0

def start_requests():
    headers = {
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.9",
        'cache-control': "no-cache",
        'postman-token': "99df9adb-6437-b62a-fd9d-59c4adf5354f"
    }
    url = "https://www.zhipin.com/job_detail/?query=爬虫&scity=101280600"

    response = requests.request("GET", url, headers=headers)
    html = etree.HTML(response.text)
    return html


# 解析搜索页面
def readHtml():
    #读取后，没有同步更新会出现重复数据
    with open('zhipin.html', 'r', encoding='utf-8') as f:
        content = f.read()
        html = etree.HTML(content)
        return html
        # print(content)

# 解析index页面，并实现翻页
def parse_index(html):
    headers = {
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.9",
        'cache-control': "no-cache",
        'postman-token': "99df9adb-6437-b62a-fd9d-59c4adf5354f"
    }

    job_urls = html.xpath('//div[@class="info-primary"]/h3/a/@href')
    print(job_urls)
    for job_url in job_urls:
        url = url_prefix + job_url
        print(url)
        response = requests.request("GET", url, headers=headers)
        h=etree.HTML(response.text)
        parse_detail(h, url)
        time.sleep(1)
        # response = requests.request("GET", job_url, headers=headers, callback=parse_detail())
    time.sleep(2)
    next_page_urls = html.xpath('//a[@class="next"]/@href')  #liat类型
    print(next_page_urls)
    print('----------------------------------------下一页-------------------------------------------')
    if len(next_page_urls) != 0:
        list=[]
        #翻页
        print("-------------------翻页--------------------")
        for next_page_url in next_page_urls:
            next_page_url = url_prefix + next_page_url
            response = requests.request("GET", next_page_url, headers=headers)
            html=etree.HTML(response.text)
            parse_index(html)  #'str' object has no attribute 'xpath'


# 解析详情页
def parse_detail(html, url):
    print('被调用')
    # html = etree.HTML(html)
    # job_title=html.xpath('//*[@id="main"]/div/div[3]/ul/li[1]/div/div[1]/h3/a/div[1]')
    try:
        job_title = html.xpath('//div[@class="name"]/h1/text()')
        print(job_title)
        obj = html.xpath('//div[@class="job-banner"]/div/div/div[2]/p/text()')
        # print(obj)
        # 经验
        job_experience = obj[1]
        print(job_experience)
        # 学历
        education = obj[-1]
        print(education)
        """
        如果把个数限定符号放在后面与之并列(即[条件1][1])则后一个[]不执行，
        所以要加括号，表示只取前一个查询集合中的第1个元素。
        """
        job_salary = html.xpath(('//div[@class="info-primary"]/div[2]/span/text()'))
        print(job_salary)
        # job_sub=html.xpath('')
        # 名字
        company_name = html.xpath('//div[@class="info-company"]/h3/a/text()')
        print(company_name)
        # 规模
        company_size = html.xpath('//div[@class="info-company"]/p/text()')
        for size in company_size:
            if bool(re.match('\d', size)):
                company_size = size
                break

        print(company_size)
        # 职位描述
        # job_detail=html.xpath('//div[@class="job-detail"]/div[3]/div/div/text()')
        # print(job_detail)
        info = {}
        info['job_title'] = job_title[0]
        info['job_experience'] = job_experience.split("：")[1]
        info['education'] = education.split("：")[1]
        info['job_salary'] = job_salary[0].strip()
        info['job_url'] = url
        info['company_name'] = company_name[0]
        info['company_size'] = company_size
        # info['job_detail']=job_detail[0].strip()
        print(info)
        list.append(info)
    except Exception as e:
        print(e)
    # ['不需要融资', <Element em at 0xb25a948>, '1000-9999人', <Element em at 0xb25ac48>, <Element a at 0xb25ae48>, 'http://www.zac.cn']
    # company_size = html.xpath("//div[@class='job-primary detail-box']/div[@class='info-company']/p/child::node()[3]")

# 翻页
# def parse_next_page():


if __name__ == "__main__":
    parse_index(html=start_requests())
    print(list)
    with open('data.txt', 'w') as f:
        s=str(list)
        f.write(s)
