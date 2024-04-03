import colorlog
import logging

log_colors_config = {
    'DEBUG':    'cyan',
    'INFO':     'green',
    'WARNING':  'yellow',
    'ERROR':    'red',
    'CRITICAL': 'bold_red',
}

def set_logger(name=None, log_file=None):
    logger = logging.getLogger(name)

    console_handler  = logging.StreamHandler()

    # 日志输出的格式(控制台)
    console_formatter = colorlog.ColoredFormatter(
        fmt='%(log_color)s[%(asctime)s] [%(levelname)s]:%(reset)s %(message)s',
        datefmt='%Y-%m-%d::%H:%M:%S',
        log_colors=log_colors_config
    )
    console_handler.setFormatter(console_formatter)


    if log_file is not None:
        file_handler     = logging.FileHandler(filename=log_file, mode='a', encoding='utf8')  

        # 日志输出的格式(文件)
        file_formatter   = logging.Formatter(
            fmt='[%(asctime)s] [%(levelname)s]: %(message)s',
            datefmt='%Y-%m-%d::%H:%M:%S'
        )
        file_handler.setFormatter(file_formatter)

    

    if not logger.handlers:
        logger.addHandler(console_handler)
        console_handler.close()
        if log_file is not None:
            logger.addHandler(file_handler)
            file_handler.close()
    
    if  log_file is not None:
        return logger, file_handler, console_handler
    return logger, console_handler
