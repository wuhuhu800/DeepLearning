import re
from collections import Counter #导入collection计算模块
words = re.findall(r'\w+', open('happiness_seg.txt').read().lower())#用正则分词

def newlist(lists):#将两个词，组合成一个二次词，放入一个列表里 ,清除掉EOS和BOS
    listsm=lists[:]
    del listsm[0]
    listsm.append('EOS')
    listt=[]
    listclear=[]
    for i in range(len(lists)):
        str1=lists[i],listsm[i]
        listt.append(str1)
    for j in listt:
        if 'EOS' not in j and 'BOS' not in j :#过滤掉EOS和BOS
            listclear.append(j)
    return listclear

if __name__ == "__main__":
    new1=newlist(words)
    print(Counter(new1).most_common(10))#counter计数
