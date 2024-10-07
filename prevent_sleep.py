import ctypes

# 定义常量
ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001

# 调用系统 API 防止电脑进入睡眠模式
ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED)

# 你的程序代码
try:
    while True:
        # 模拟长时间运行的任务
        pass
except KeyboardInterrupt:
    # 恢复系统默认的睡眠模式设置
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)