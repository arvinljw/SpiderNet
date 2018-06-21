import json
import random

from scrapy import Request
from scrapy.spiders import CrawlSpider

from ..items import QQMusicItem

# 其中rnd，sin，ein三个参数需要动态改变
LIST_URL = r"""https://c.y.qq.com/splcloud/fcgi-bin/fcg_get_diss_by_tag.fcg?picmid=1&rnd=%s&g_tk=128941526&jsonpCallback=getPlaylist&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&categoryId=10000000&sortId=5&sin=%s&ein=%s"""

# 其中disstid需要动态改变
DETAIL_URL = r"""https://c.y.qq.com/qzone/fcg-bin/fcg_ucc_getcdinfo_byids_cp.fcg?type=1&json=1&utf8=1&onlysong=0&disstid=%s&format=jsonp&g_tk=128941526&jsonpCallback=playlistinfoCallback&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0"""

PER_PAGE_SIZE = 30


def getRnd():
    return random.random()


class QQMusic(CrawlSpider):
    name = 'qqmusic'
    host = 'https://y.qq.com'
    allowed_domains = ['y.qq.com']
    url = LIST_URL
    start_size = 0
    total_size = 0
    end_size = PER_PAGE_SIZE - 1
    start_urls = [
        url % (getRnd(), start_size, end_size),
    ]

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "referer": "https://y.qq.com/portal/playlist.html",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    }

    detail_header = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "referer": "",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    }

    def start_requests(self):
        yield Request(self.start_urls[0], headers=self.headers, dont_filter=True)

    def parse(self, response):
        playList = self.getDict(response.text, 'getPlaylist')
        self.total_size = playList['data']['sum']
        items = playList['data']['list']
        print('item->', items)
        for item in items:
            for result in self.parse_item(item):
                yield result

        self.start_size = self.end_size + 1
        self.end_size += PER_PAGE_SIZE
        next_page_url = self.url % (getRnd(), self.start_size, self.end_size)
        if next_page_url and self.start_size <= self.total_size:
            yield Request(next_page_url, headers=self.headers, callback=self.parse)

    def parse_item(self, each):
        item = QQMusicItem()
        item['songSheet'] = each['dissname']
        item['authorName'] = each['creator']['name']
        item['playTimes'] = each['listennum']
        item['createTime'] = each['createtime']

        dissid = each['dissid']
        detail_url = DETAIL_URL % dissid
        if detail_url:
            self.detail_header['referer'] = 'https://y.qq.com/n/yqq/playsquare/%s.html' % dissid
            yield Request(detail_url, headers=self.detail_header, meta={'data': item}, callback=self.parse_detail)
        else:
            return item

    def parse_detail(self, response):
        item = response.meta['data']
        getDetail = self.getDict(response.text, 'playlistinfoCallback')
        print("detail->", getDetail)
        cd_list = getDetail['cdlist']
        for cd in cd_list:
            item['tags'] = self.getTags(cd)
            item['introduce'] = cd['desc'][0:30]
        yield item

    @staticmethod
    def getDict(content, replace_str):
        content = content[len(replace_str) + 1: len(content) - 1]
        return json.loads(content)

    @staticmethod
    def getTags(cd):
        return ','.join(str(tag['name']) for tag in cd['tags'])
