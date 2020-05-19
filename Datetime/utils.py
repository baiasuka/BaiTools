import datetime


def get_constellation(date_str):
    """
    通过生日获取星座
    :param date_str: 生日日期字符串，格式为%Y-%m-%d
    :return:
    """
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    month = date.month
    day = date.day
    n = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座', u'巨蟹座', u'狮子座',
         u'处女座', u'天秤座', u'天蝎座', u'射手座')
    d = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))
    return n[len(list(filter(lambda y: y <= (month, day), d))) % 12]

def get_current_datetime():
    """
    获取当前时间字符串
    :return:
    """
    time_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return time_str


def get_post_age(fst_date, snd_date):
    """
    用于通过两人生日判断是否为X0后或X5后
    :param fst_date: datetime.date类型
    :param snd_date: datetime.date类型
    :return:
    """
    fst_year = fst_date.year
    snd_year = snd_date.year
    if round(fst_year//100) == round(snd_year//100):
        age_half = round(fst_year//10)*10 + 5
        if fst_year > age_half and snd_year > age_half:
            return '都是' + str(age_half)[2:] + '后'
        else:
            return '都是' + str(round(fst_year//10)*10)[2:] + '后'
    else:
        return None
