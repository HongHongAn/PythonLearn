#CalHamlet.py

def getText():
    txt = open("hamlet.txt","r").read()
    txt = txt.lower()  # 将所有字符转换为小写
    for ch in '!@#$%^&*()":;?,.><+=-_{}[\\]\/|`~':  #将所有特殊符号用空格替代
        txt = txt.replace(ch," ")
    return txt

hamletTxt = getText()
words = hamletTxt.split()  #用空格分隔文本并返回列表格式
counts = {}
for word in words:
    # counts.setdefault(word, 0)
    # counts[word] += 1
    # 如果 word变量对应的Key已经在字典中了，那么counts.setdefault(word, 0) 这一行的作用相当于counts.get(word)。
    #    # 如果word变量对应的Key不在字典中了，那么此时就会添加这个Key，然后把它的值设置为0。
    # 原文链接：https: // blog.csdn.net / weixin_39862985 / article / details / 111499002
    counts[word] = counts.get(word,0) + 1
items = list(counts.items())  #返回所有键值对信息，生成列表
#key=lambda 元素: 元素[字段索引] .例如：key=lambda x: x[1] 对元素第二个字段排序.
# 排序默认从小到大升序，reverse= True表示对列表反排序:降序排列
items.sort(key=lambda x : x[1],reverse= True)
for i in range(10):
    word,count = items[i]
    print("{0:<10}{1:>5}".format(word,count))
    #题中0对应的是Word，1对应的是count。
    # 冒号是引导符，后面跟的是格式控制方法。<表示左对齐，>表示右对齐，数字表示宽度。
    # 文中<10表示左对齐，并占10个位置，>5表示右对齐，占5个位置。
