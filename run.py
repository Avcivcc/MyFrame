#!/bin/bash
# vim: set fileencoding=utf-8

from untils.HTMLTestRunner_PY3 import HTMLTestRunner
from untils.log_cn import *
from untils.tools import sendMailAttach
import unittest, time

suit = unittest.defaultTestLoader.discover('./case', pattern='creat_*.py')


if __name__ == '__main__':
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    mkdir('./report/' + now[:-8] + 'TestReport')
    filename = './report/' + now[:-8] + 'TestReport/html/' + now + '.html'
    runner = HTMLTestRunner(open(filename, 'wb'), title='测试报告', description='一共5份')
    runner.run(suit)
    # sendMailAttach(filename)
