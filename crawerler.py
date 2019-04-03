import urllib.request
import re
import os
#从网页上获取github项目url
# 1. 确定好要爬取的入口链接     爬取github网址
url = "https://blog.csdn.net/jiuhaofangyinyue/article/details/78989885"
# 2.根据需求构建好链接提取的正则表达式
pattern1 = '<.*?(href=".*?").*?'
# 3.模拟成浏览器并爬取对应的网页 谷歌浏览器
headers = {'User-Agent',
           'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
opener = urllib.request.build_opener()
opener.addheaders = [headers]
data = opener.open(url).read().decode('utf8')
# 4.根据2中规则提取出该网页中包含的链接
content_href = re.findall(pattern1, data, re.I)
# print(content_href)
# 5.过滤掉重复的链接
#    # 列表转集合(去重) list1 = [6, 7, 7, 8, 8, 9] set(list1) {6, 7, 8, 9}
set1 = set(content_href)
# 6.后续操作，比如打印出来或者保存到文件中。
file_new = "D:\\研一学习下\\科研\\href2.txt"
github = "github.com"
count =0
f = open(file_new,"w")
for i in set1:
    if github in i:
        string = i[6:-1]
        f.write(string)
        f.write("\n")
        count += 1
text = "总共"+str(count)+"个项目"
f.write(text)
f.write("\n")
f.close()

print('已经生成文件')


#从文件读取url
file_new = "D:\\研一学习下\\科研\\hreff.txt"
f = open(file_new,"r")
href=[]
line = f.readline()
while line:
    href.append(line)
    line= f.readline()
f.close()
#将重复的url去掉
hreflist = list(set(href))  #去重
hreflist=hreflist[47:]
print(len(hreflist))

#执行git命令下载项目
for url in hreflist:
    cmd ="git  clone "+url
    os.system(cmd)
print("下载项目完成！")




