# 列表（list）的工具类及函数

import heapq

def CartesianProduct(fst_list, snd_list):
    """
    计算两个列表的笛卡尔积
    :param list1:
    :param list2:
    :return: 元组列表
    """
    return [(a, b) for a in fst_list for b in snd_list]

def getDifference(fst_list, snd_list):
    """
    求两个列表的差集
    :param list1:
    :param list2:
    :return:
    """
    dif = set(fst_list) - set(snd_list)
    return list(dif)

def getTopN(data, num=1, desc=True):
    """
    求列表的最大/最小的N个值
    :param data: 列表
    :param num: 前N个值
    :param desc: Bool类型，True为求最大值的top
    :return:
    """
    if desc:
        return heapq.nlargest(num, data)
    else:
        return heapq.nsmallest(num, data)


if __name__ == '__main__':
    result = getDifference([('hong',1),('pan',2),('hou',3)], ['hong','pan','tong'])
    print(result)
