import time, os

'''
每一次运行报告创建目录
执行断言时写入log
'''


def mkdir(path):
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path + '/html')
        os.makedirs(path + '/png')

    else:
        print('该目录已存在')

def write_log(info):
    now = time.strftime('%Y_%m_%d')
    now1 = time.strftime('%H_%M_%S')
    with open('D:/PycharmProjects/MyFrame/log/' + now + '.log' , 'a+', encoding='utf-8')as f:
        f.write(now1 + ':' + info)
        f.write('\n')
