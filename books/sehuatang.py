#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook # 继承基类BaseFeedBook

def getBook():
    return sehuatang

class sehuatang(BaseFeedBook):
    title                 = u'色花堂'# 设定标题
    description           = u''# 设定简介
    language              = 'zh-cn'# 设定语言
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8" # 设定待抓取页面的页面编码
    mastheadfile          = "mh_SHT.gif"# 设定标头图片
    coverfile             = "cv_SHT.jpg"# 设定封面图片
    oldest_article        = 1  # 设定文章的时间范围。小于等于365则单位为天，否则单位为秒，0为不限制
    max_articles_per_feed = 40 # 设定每个主题下要最多可抓取的文章数量
    fulltext_by_readability = True    
    
    
    # 指定要提取的包含文章列表的主题页面链接
    # 每个主题是包含主题名和主题页面链接的元组
    feeds = [
            (u'卡通动漫', 'https://rsshub.app/dsndsht23/117/648'),
            (u'武侠虚幻', 'https://rsshub.app/dsndsht23/138'),
            (u'青春校园', 'https://rsshub.app/dsndsht23/137'),
            (u'乱伦人妻', 'https://rsshub.app/dsndsht23/135'),
            (u'激情都市', 'https://rsshub.app/dsndsht23/136'),
            ]
            
    def fetcharticle(self, url, opener, decoder):
        #每个URL都增加一个后缀full=y，如果有分页则自动获取全部分页
        url += '?full=y'
        return BaseFeedBook.fetcharticle(self,url,opener,decoder)
    
    # 在文章内容被正式处理前做一些预处理
    def preprocess(self, content):
        # 将页面内容转换成BeatifulSoup对象
        soup = BeautifulSoup(content, 'lxml')
        # 调用处理内容分页的自定义函数SplitJointPagination()
        content = self.SplitJointPagination(soup)
        # 返回预处理完成的内容
        return unicode(content)     