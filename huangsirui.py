import re
from collections import Counter
import matplotlib.pyplot as plt
ats = open("Mansfield Park.txt", "r", encoding='utf-8')  # 导入Mansfield Park文本
alla = ats.read()      # 文件操作
ats.close()         # 关闭文件
for ch in '|"#@!$%^*()?~`,.;:[]{}_-=+<>""“”':  # 将特殊字符改为空格
    alla = alla.replace(ch, " ")
# 词频统计 将单词与数量对应起来
count_word = {}        
for word in alla.split():
    word_low = word.lower()     # 统一小写
    count_word[word_low] = count_word.get(word_low, 0)+1
result = [(v, k) for k, v in count_word.items()]   # 逆序排列
result.sort()
result.reverse()
print(result)

are = []    # 找出are 匹配
for i in re.finditer("([A-z]{1,30}) (are)", alla):
    what = i.group()
    are.append(what)
c = Counter(are)
for k, v in c.most_common():
    print(k, v)

sort_list = sorted(count_word.values(), reverse=True)
plt.title('Zipf-Law', fontsize=18)  # 标题
plt.xlabel('rank', fontsize=18)     # 排序
plt.ylabel('freq', fontsize=18)     # 数量
plt.yticks([pow(10, i) for i in range(0, 164)])  # 设置y刻度
plt.xticks([pow(10, i) for i in range(0, 4)])  # 设置x刻度
x = [i for i in range(len(sort_list))]
plt.yscale('log')                  # 设置纵坐标的缩放
plt.xscale('log')                  # 设置横坐标的缩放
plt.plot(x, sort_list, 'r')        # 绘图
plt.savefig('./Zipf_Law.jpg')      # 保存图片
plt.show()





