#encoding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import sys
import os
import requests
from bs4 import BeautifulSoup
import markdown


class MarkdownToHtml:

    _headTag = '<head><meta charset="utf-8" /></head>'
    _urlcss = 'https://raw.githubusercontent.com/mrcoles/markdown-css/master/markdown.less'

    def __init__(self):
        self.genStyle

    def genStyle(self):
        with requests.get(_urlcss) as r:
            cssString = r.read()
        self._headTag = self._headTag[:-7] + '<style type="text/css">{}</style>'.format(cssString) + self._headTag[-7:]

    def markdownToHtml(self, sourceFilePath, filename):
        with open(sourceFilePath + "\\" + filename, 'r') as f:
            markdownText = f.read()
        # 编译出原始 HTML 文本
        rawHtml = self._headTag + markdown.markdown(markdownText, output_format='html5')
        # 格式化 HTML 文本为可读性更强的格式
        beautifyHtml = BeautifulSoup(rawHtml,'html5lib').prettify()
        with open(sourceFilePath + "\\" + filename.split(".")[0] + ".html", 'w') as f:
            f.write(beautifyHtml)


if __name__ == "__main__":
    mth = MarkdownToHtml()
    argv = sys.argv[1:]
    for file in argv:
    	filePath = os.path.dirname(os.path.abspath(__file__))
        # 判断文件路径是否有效
        print filePath
        print file
        file_abs_path = filePath + "\\" + file
        if os.path.isfile(file_abs_path):
            mth.markdownToHtml(filePath, file)
        else:
            print('Invalid Path: ' + filePath)