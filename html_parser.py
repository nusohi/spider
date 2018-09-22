#coding:utf-8
from bs4 import BeautifulSoup
import re

class HtmlParser(object):

    def _get_new_urls(self, url, soup):
        new_urls = set()
        links = soup.find_all('a',href=re.compile(r'\/item\/.+'))
        # test
        # print '\t nuso test:links:'
        # print links
        # test
        for link in links:
            new_url = link['href']
            new_full_url='http://baike.baidu.com%s'%new_url
            # test
            # print '\t nuso test:new_url href:'
            # print new_full_url
            # test
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, url, soup):
        data = {}
        data['url'] = url
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        data['title'] = title_node.get_text()
        summary_node = soup.find('div', class_='lemma-summary')
        data['summary'] = summary_node.get_text()
        return data

    def parse(self, url, cont):
        if url is None or cont is None:
            return
        soup = BeautifulSoup(cont,'html.parser',from_encoding='utf-8')
        new_urls = self._get_new_urls(url,soup)
        new_data = self._get_new_data(url,soup)
        return new_urls, new_data
