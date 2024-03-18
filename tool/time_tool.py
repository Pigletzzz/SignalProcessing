# 时间相关的方法
def ms_to_min_sec(milliseconds):
    seconds = milliseconds // 1000  # 整除得到秒数
    minutes = seconds // 60  # 整除得到分钟数
    remaining_seconds = seconds % 60  # 求余得到剩余的秒数
    return f"{int(minutes)}:{remaining_seconds:02d}"