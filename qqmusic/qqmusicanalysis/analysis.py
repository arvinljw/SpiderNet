"""
分析数据类
"""
import numpy as np
import pandas as pd
from PIL import Image
from matplotlib import pyplot as plt
from wordcloud import WordCloud


class BaseAnalysis:

    def __init__(self):
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
        self.dfAll = pd.read_csv('../music.csv')

    def show(self):
        pass


class AnalysisPlayTimes(BaseAnalysis):

    def __init__(self):
        super().__init__()
        play50M = self.dfAll[self.dfAll.playTimes >= 50000000]['playTimes'].size
        play10M = self.dfAll[(self.dfAll.playTimes >= 10000000) & (self.dfAll.playTimes < 50000000)]['playTimes'].size
        play5M = self.dfAll[(self.dfAll.playTimes >= 5000000) & (self.dfAll.playTimes < 10000000)]['playTimes'].size
        play1M = self.dfAll[(self.dfAll.playTimes >= 1000000) & (self.dfAll.playTimes < 5000000)]['playTimes'].size
        play500K = self.dfAll[(self.dfAll.playTimes >= 500000) & (self.dfAll.playTimes < 1000000)]['playTimes'].size
        play100K = self.dfAll[(self.dfAll.playTimes >= 100000) & (self.dfAll.playTimes < 500000)]['playTimes'].size
        playLess100K = self.dfAll[(self.dfAll.playTimes < 100000)].size

        self.playTimes = np.array([play50M, play10M, play5M, play1M, play500K, play100K, playLess100K])
        self.index = ['五千万以上', '1千万以上', '5百万以上', '1百万以上', '5十万以上', '1十万以上', '十万以下']

    def show(self):
        plt.xlabel('播放量')
        plt.ylabel('歌单数')
        for i in range(len(self.playTimes)):
            size = self.playTimes[i]
            plt.bar(self.index[i], size)
            plt.text(self.index[i], size + 10, str(size) + '个', ha='center')
        plt.show()


class AnalysisTags(BaseAnalysis):

    def __init__(self):
        super().__init__()
        self.tags = np.array(self.dfAll['tags'])

    def show(self):
        alice_mask = np.array(Image.open("../images/qqmusic.jpeg"))
        wordCloud = WordCloud(font_path='../font/simhei.ttf',
                              background_color='white',
                              max_font_size=100,
                              random_state=60,
                              mask=alice_mask
                              )
        data = self.dealData()
        wordCloud.generate_from_frequencies(data)
        plt.imshow(wordCloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()
        data = sorted(data.items(), key=lambda data: data[1], reverse=True)
        print(data[:10])

    def dealData(self):
        allTags = self.tags.flatten()
        tagDict = {}
        for allTag in allTags:
            tags = str(allTag).split(',')
            for tag in tags:
                val = tagDict.setdefault(tag, 0)
                tagDict[tag] = val + 1
        return tagDict
