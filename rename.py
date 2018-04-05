import sys
import math
import os
path="f:\\BaiduNetdiskDownload\\中国科学技术大学-数学分析220讲\\文件夹1\\"
f=os.listdir("f:\BaiduNetdiskDownload\中国科学技术大学-数学分析220讲\文件夹1")
n=0
for i in f:
    oldname=f[n]
    print(oldname)
    os.rename(path+oldname,path+oldname[17:])
    n+=1
