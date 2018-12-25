from lxml import etree

def readHtml():
    with open('zhipin.html', 'r', encoding='utf-8') as f:
        content=f.read()
        print(content)
        html=etree.HTML(content)
        job_title=html.xpath('//*[@class="job-title"]')
        print(job_title)
        for i in job_title:
            print(i.text)


if __name__ == "__main__":
    readHtml()