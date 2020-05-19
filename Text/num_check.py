# 通过汉字的读音判断是否包含谐音连续数字的示例
import pypinyin
import re

def check_num_words(word):
    s = ''
    for i in pypinyin.pinyin(word, style=pypinyin.NORMAL):
        s += ''.join(i)
    return s

r = check_num_words('已而伞寺无留琦巴')
result = re.match("(yi|er|san|si|wu|liu|qi|ba|jiu){5,}", r)
if result:
    print(result.group())