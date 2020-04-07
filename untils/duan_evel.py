import unittest
from untils.printScreen import jietu
from untils.log_cn import write_log
from selenium.common.exceptions import InvalidSelectorException, NoSuchElementException


def duan_in(dr, expectation, actual, description):
    try:
        unittest.TestCase().assertIn(expectation, actual)
    except AssertionError as e:
        write_log('预期: %r 实际: %r' % (expectation, expectation) + '，错误原因：元素未找到')
        jietu(dr, description)
    except SyntaxError as e:
        print('语法错误')
        jietu(dr, description)
    except NoSuchElementException as e:
        print('元素未找到')
        jietu(dr, description)
    else:
        print('执行通过')
        jietu(dr, description)
