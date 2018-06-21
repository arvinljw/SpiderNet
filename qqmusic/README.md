## QQ音乐歌单数据爬取分析

### 三方包引入

使用到了以下包：

* 爬虫 **scrapy**
* 网络测试 **requests**
* 数据分析 **numpy和pandas**
* 绘图 **matplotlib和wordcloud**

```
pip install scrapy
pip install requests
pip install numpy
pip install pandas
pip install matplotlib
pip install wordcloud
```

### 爬取数据

[结果数据](https://github.com/arvinljw/SpiderNet/blob/master/qqmusic/music.csv)

这是一个csv文件，可通过excel之类的打开，便可简单的处理数据，例如播放量最高的歌单排行，这里列出播放量前20的歌单：

![rank](https://upload-images.jianshu.io/upload_images/3157525-da3feb8a9926404e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 分析数据

数据拿到后，在上边已经简单的处理了以下数据，就是看看播放次数前20的歌单。

接着我想看看播放次数的大致分布情况，例如播放5000万次以上有多少，1000万，500万，100万，50万，10万以上以及10万以下，都有多少。然后绘制成柱状图，看看是什么情况。

是的，对于这个数据的处理，就用到了numpy和pandas以及matplotlib。经过分析得出下图结果:

#### 播放次数分析

![播放次数分析](https://upload-images.jianshu.io/upload_images/3157525-374fc96737784ee4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

很直观的看到高于500万播放次数的歌单是少数的。按比例来看的话，能明显看到10万以下的歌单有2300多个，还是比较多的，之后再进一步分析这2300多个歌单的创建时间的分布，这里就不继续分析了。

#### 标签分析

对于标签什么的，以下我就想到了使用词云，就能直观的看到哪些词出现的次数多。歌单都主要是什么类型的比较受欢迎。编码后得到如下结果:

![标签分析](https://upload-images.jianshu.io/upload_images/3157525-d9c6892f9bf2b4b5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

可能直接这样看能大概知道哪些多，但是还是不是很能分得很细，我又排了个序，下边列出降序排列前十的标签～

```
[('流行', 1834), ('英语', 1669), ('国语', 1386), ('电子', 723), 
('日语', 552), ('民谣', 369), ('ACG', 347), ('影视', 337), 
('治愈', 337), ('韩语', 330)]
```

先就分析这么多，等有空再分析一下创建时间的分布情况。




