import time

def jietu(dr, description):
    now = time.strftime('%Y_%m_%d')
    now1 = time.strftime('%H_%M_%S')
    dr.get_screenshot_as_file('D:/PycharmProjects/MyFrame/report/' + now + '_TestReport/png/' + now1 + description + '.png')
    print('D:/PycharmProjects/MyFrame/report/' + now + 'TestReport/' + now1 + description + '.png')
    print(dr.get_screenshot_as_file('D:/PycharmProjects/MyFrame/report/' + now + 'TestReport/png/' + now1 + description + '.png'))
