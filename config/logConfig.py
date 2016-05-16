# _*_coding=UTF-8_*_
import logging
import os
from logging.handlers import TimedRotatingFileHandler

def logConfigInit():
    # 设置logger等级
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # 创建一个FileHandler，用于写入日志文件
    logFilePath = "log/system.log"
    fileHandler = TimedRotatingFileHandler(logFilePath,when="d",interval=1,backupCount=100)
    fileHandler.setLevel(logging.INFO)

    # 创建一个StreamHandler，用于在控制台输出信息
    streamHandler = logging.StreamHandler()
    streamHandler.setLevel(logging.DEBUG)

    # 格式化
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fileHandler.setFormatter(formatter)
    streamHandler.setFormatter(formatter)

    # 设置handler
    logger.addHandler(fileHandler)
    logger.addHandler(streamHandler)


