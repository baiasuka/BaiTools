# 列表（list）的工具类及函数

def dround(array, decimals=1):
    """
    对字典的值取n位小数
    :param array:
    :param decimals:
    :return:
    """
    for i in array.keys():
        array[i] = round(array[i], decimals)
    return array

def slice(ori_dict, start, end):
    """
    用于对字典进行切片，返回下标从start到end-1范围内的字典
    :param ori_dict: 原字典
    :param start:
    :param end:
    :return:
    """
    return {k: ori_dict[k] for k in list(ori_dict.keys())[start:end]}

if __name__ == "__main__":
    print(slice({"name":"hong","id":111,"num":222}, 0, 2))
