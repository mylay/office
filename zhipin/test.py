import requests
from lxml import etree

info={}
url_prefix = "http://www.zhipin.com"

def start_requests():
    pass


#解析搜索页面
def readHtml():
    with open('zhipin.html', 'r', encoding='utf-8') as f:
        content=f.read()
        html = etree.HTML(content)
        return html
        # print(content)


def parse_index():
    headers = {
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.9",
        'cache-control': "no-cache",
        'postman-token': "99df9adb-6437-b62a-fd9d-59c4adf5354f"
    }


    html=readHtml()
    job_urls = html.xpath('//div[@class="info-primary"]/h3/a/@href')
    print(job_urls)
    for job_url in job_urls:
        url=url_prefix+job_url
        response=requests.request("GET", url, headers=headers)
        obj=response.text
        parse_detail(obj)
        # response = requests.request("GET", job_url, headers=headers, callback=parse_detail())


#解析详情页
def parse_detail(html):
    print('被调用')
    html = etree.HTML(html)
    # job_title=html.xpath('//*[@id="main"]/div/div[3]/ul/li[1]/div/div[1]/h3/a/div[1]')
    job_title = html.xpath('')
    print(job_title)
    obj = html.xpath('')
    print(obj)
    """
    如果把个数限定符号放在后面与之并列(即[条件1][1])则后一个[]不执行，
    所以要加括号，表示只取前一个查询集合中的第1个元素。
    """
    job_salary = html.xpath((''))
    print(job_salary)
    # job_sub=html.xpath('')
    # 链接
    job_url = html.xpath('')
    print(job_url)
    # 名字
    company_name = html.xpath('')
    print(company_name)
    # 规模
    company_size = html.xpath('')
    print(company_size)

    info['job_title'] = job_title
    info['obj'] = obj
    info['job_salary'] = job_salary
    info['job_url'] = url_prefix + job_url
    info['company_name'] = company_name
    info['company_size'] = company_size
    print(info)


if __name__ == "__main__":
    parse_index()

