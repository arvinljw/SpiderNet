from qqmusic.qqmusicanalysis.analysis import *


if __name__ == '__main__':
    # 播放量分析
    playTimes = AnalysisPlayTimes()
    playTimes.show()
    # 标签分析
    tags = AnalysisTags()
    tags.show()
