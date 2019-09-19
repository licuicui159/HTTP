import logging

# 获取logging的实例
import sys
# 形成一个logger对象
logger=logging.getLogger("APPname")

# 制定logger的输出格式
formatter=logging.Formatter("%(asctime)s %(levelname)-8s %(message)s")

# 文件日志
file_handler=logging.FileHandler("testLogger.log")
file_handler.setFormatter(formatter)

# 控制台日志
# console_handler = logging.StreamHandler(sys.stdout)
# console_handler.formatter = formatter  # 也可以直接给formatter赋值

# 指定日志的最低输出级别，默认为WARN级别
logger.setLevel(logging.INFO)

# 把文件日志与控制台日志添加到日志处理器中
logger.addHandler(file_handler)
# logger.addHandler(console_handler)

if __name__=='__main__':
    logger.debug('this is debug info')
    logger.info('this is information')
    logger.warning('this is warning message')
    logger.error('this is error message')
    logger.critical('this is critical message')

# CRITICAL：特别糟糕的事情，如内存耗尽、磁盘空间为空，一般很少使用
# ERROR：发生错误时，如IO操作失败或者连接问题
# WARNING：发生很重要的事件，但是并不是错误时，如用户登录密码错误
# INFO：处理请求或者状态变化等日常事务
# DEBUG：调试过程中使用DEBUG等级，如算法中每个循环的中间状态


# 在目标程序中使用logger来采集错误信息
# try:
#     1 / 0
# except:
#     # 等同于error级别，但是会额外记录当前抛出的异常堆栈信息，括号内可以提示哪个模块哪一行
#     logger.exception('this is an exception message')
