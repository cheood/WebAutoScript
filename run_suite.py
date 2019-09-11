"""
测试套件(项目运行入口)
"""
import time
import unittest
from case.test_cart import TestCart
from case.test_login import TestLogin
from case.test_order import TestOrder
from config import BASE_DIR
from utlis import DriverUtil
from tools.HTMLTestRunnerCN import HTMLTestReportCN

# 初始化套件对象
suite = unittest.TestSuite()

# 关闭浏览器退出方法
DriverUtil.change_quit_status(False)

# 调用方法组装测试用例
suite.addTest(unittest.makeSuite(TestLogin))  # 登录
suite.addTest(unittest.makeSuite(TestCart))  # 添加商品
suite.addTest(unittest.makeSuite(TestOrder))  # 提交订单&订单支付

# 初始化执行对象并调用执行方法
# unittest.TextTestRunner().run(suite)

# 设置报告存放路径及文件名
report_name = BASE_DIR + '/report/report_{}.html'.format(time.strftime('%Y%m%d_%H%M%S'))

# 生成测试报告
with open(report_name, 'wb') as f:
    runner = HTMLTestReportCN(stream=f,
                              verbosity=2,
                              title='Web 自动化测试报告',
                              description='系统: macOS, 语言: Python, 浏览器: 谷歌浏览器',
                              tester='QA14')
    runner.run(suite)

# 打开浏览器退出方法
DriverUtil.change_quit_status(True)

# 退出浏览器对象
DriverUtil.quit_driver()
