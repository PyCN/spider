spider
===========================
spider是业余时间，学习Python爬虫的例子。
****
## 介绍
* [网络爬虫的基本工作流程](#网络爬虫的基本工作流程)
  * 首先选取一部分精心挑选的种子URL
  * 将种子URL加入任务队列
  * 从待抓取URL队列中取出待抓取的URL，解析DNS，并且得到主机的ip，并将URL对应的网页下载下来，存储进已下载网页库 中。此外，将这些URL放进已抓取URL队列。
  * 分析已抓取URL队列中的URL，分析其中的其他URL，并且将URL放入待抓取URL队列，从而进入下一个循环。
  * 解析下载下来的网页，将需要的数据解析出来。
  * 数据持久话，保存至数据库中。

* [Python爬虫框架](#Python爬虫框架)
  * grab – 网络爬虫框架（基于pycurl/multicur）。
  * scrapy – 网络爬虫框架（基于twisted），不支持Python3。
  * pyspider – 一个强大的爬虫系统。
  * cola – 一个分布式爬虫框架。
  * portia – 基于Scrapy的可视化爬虫。
  * restkit – Python的HTTP资源工具包。它可以让你轻松地访问HTTP资源，并围绕它建立的对象。
  * demiurge – 基于PyQuery的爬虫微框架。
  
* [学习案例](#Python爬虫学习案例)
  * 本学习案例仅支持Python3.x；
  * basic - 使用requests库爬取新浪股票、全国省市编码；
  * http_lagou - 使用来requests库爬取拉勾网职位信息；
  * douban_book - 使用scrapy框架来爬取豆瓣书籍；
  * zhuhu - 使用scrapy框架来爬取知乎信息。


## 联系我们
  * 邮箱：deamoncao@163.com
  * 博客：http://note.youdao.com/noteshare?id=077ebf1f14de79d1821778d24e713c1c&sub=BE720E09CE75415781F2788F330052A2
