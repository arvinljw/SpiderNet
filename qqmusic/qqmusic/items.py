# -*- coding: utf-8 -*-

from scrapy import Item, Field


class QQMusicItem(Item):
    songSheet = Field()
    authorName = Field()
    playTimes = Field()
    createTime = Field()
    tags = Field()
    introduce = Field()
