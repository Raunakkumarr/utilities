from urllib3.request import Request, urlopen
from bs4 import BeautifulSoup as bs

def pcampus_notice_scrap():
    req = Request('https://pcampus.edu.np/category/admission-notices/', headers={'User-Agent': 'Chrome'})
    webpage = urlopen(req).read()
    soup = bs(webpage, 'lxml')
    new_notice_title = soup.find('main', class_="site-main").find('article', class_="post").find('div',class_="post-inner-content").find('h2', class_="entry-title").text
    new_notice_link = soup.find('main', class_="site-main").find('article',class_="post").find('div', class_="post-inner-content").find('h2', class_="entry-title").find('a').get('href')
    #print(f"{new_notice_title}\n\nLink to the notice: {new_notice_link}")
    new_notice_details = [new_notice_title, new_notice_link]
    return new_notice_details


def wrc_notice_scrap():
    req = Request('https://www.ioepas.edu.np/category/news-notices/admission-notice/',headers={'User-Agent': 'Chrome'})
    webpage = urlopen(req).read()
    soup = bs(webpage, 'lxml')
    new_notice_title = soup.find('a', class_="wpex-inherit-color-important").text
    new_notice_link = soup.find('a', class_="wpex-inherit-color-important").get('href')
    new_notice_details = [new_notice_title, new_notice_link]
    return new_notice_details


def ioe_notice_scrap():
    req = Request('https://entrance.ioe.edu.np/Notice',headers={'User-Agent': 'Chrome'})
    webpage = urlopen(req).read()
    soup = bs(webpage, 'lxml')
    table = soup.find('table', class_="table table-bordered")
    trow = table.find('tbody').find_all('tr')
    last_notice = trow[0].find_all('td')
    notice_date = last_notice[2].text
    notice_title = last_notice[1].text
    new_notice_title = str(notice_title) + 'on' + str(notice_date)
    new_notice_link = 'https://entrance.ioe.edu.np/' + last_notice[3].find('a')['href']
    new_notice_details = [new_notice_title, new_notice_link]
    return new_notice_details


def pu_notice_check():
    req = Request('https://scholarship.pu.edu.np/news',headers={'User-Agent': 'Chrome'})
    webpage = urlopen(req).read()
    soup = bs(webpage, 'lxml')
    notice_date = soup.find_all('div',class_="blog_3_des")[0].find('ul').find('li').find('span').text
    notice_title = soup.find_all('div',class_="blog_3_des")[0].find('h5').text
    new_notice_link = soup.find_all('div', class_="blog_3_des")[0].find('h5').find('a')['href']
    new_notice_title = str(notice_title) + ' on ' + str(notice_date)
    new_notice_details = [new_notice_title, new_notice_link]
    return new_notice_details

def add_notice_to_database(details):
    pass
