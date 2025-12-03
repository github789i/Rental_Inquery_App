import sys
import os
import requests
from lxml import etree
import _thread

# 创建多线程下载图片
# 创建对象
class House:
    def __init__(self, name, info, source, price, link):
        self.name = name
        self.info = info
        self.source = source
        self.price = price
        self.link = link