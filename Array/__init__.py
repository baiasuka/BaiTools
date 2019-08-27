def format_data(data,columns):
    """
    用于将没有字段名的元组列表转化为字典列表
    :param columns: 表头list["id","name","age"]
    :param data: 表数据list，形如[(a,b,c),(d,e,f),(g,h,i)]
    :return:
    """
    if data:
        result = []
        for item in data:
            result.append(dict(zip(columns, item)))
        return result
    else:
        return []
