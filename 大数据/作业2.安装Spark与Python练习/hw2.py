import os
import string

# Global variables
input_file = os.environ['HOMEPATH']+"/Desktop/hw2_input.txt"
output_file = os.environ['HOMEPATH']+"/Desktop/hw2_output.txt"
stopword = os.environ['HOMEPATH']+"/Desktop/stopwords.txt"

# 从本地读取文件
text = open(input_file, 'r', encoding='utf-8').read()
stopwords = open(stopword, 'r', encoding='utf-8').read()
stopwords = stopwords.split('\n')
# 预处理：大小写
text = text.lower()
# 预处理：标点符号
for i in string.punctuation:
    text = text.replace(i, " ")
# 分词并去除停用词
words = text.split()
wc = {}
for word in words:
    wc[word] = wc.get(word, 0)+1
wclist = list(wc.items())
wclist.sort(key=lambda x: x[1], reverse=True)
for i in stopwords:
    for j in wclist:
        if i == j[0]:
            wclist.remove(j)
# 去除单个字母
for i in wclist:
    if len(i[0]) == 1:
        wclist.remove(i)
# 判断文件是否存在
if os.path.exists(output_file):
    os.remove(output_file)
# 写入文件
wf = open(output_file, "a")
for i in range(50):
    word, count = wclist[i]
    wcout = "{0:<10}{1:>5}".format(word, count)
    wf.write(wcout+"\n")
wf.close()
# 查看输出文件
os.system("powershell cat "+output_file)