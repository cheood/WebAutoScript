"""
订单-测试用例
订单支付-测试用例
(此用例不能单独运行, 需要和登录和购物车脚本建立依赖关系)
"""
import unittest

from page.goods_cart_page import GoodsCartProxy
from page.index_page import IndexProxy
from page.my_order_page import MyOrderProxy
from page.order_check_page import OrderCheckProxy
from page.order_pay_page import OrderPayProxy
from utlis import DriverUtil, get_tip_text, switch_new_window


class TestOrder(unittest.TestCase):
    """订单测试类"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverUtil.get_driver()  # 获取浏览器对象
        cls.index_proxy = IndexProxy()  # 首页业务执行对象
        cls.goods_cart_proxy = GoodsCartProxy()  # 购物车业务执行对象
        cls.order_check_proxy = OrderCheckProxy()  # 订单确认业务执行对象
        cls.my_order_proxy = MyOrderProxy()  # 我的订单页面业务执行对象
        cls.order_pay_proxy = OrderPayProxy()  # 订单支付页面业务执行对象

    @classmethod
    def tearDownClass(cls) -> None:
        DriverUtil.quit_driver()  # 退出浏览器对象

    def setUp(self) -> None:
        self.driver.get('http://127.0.0.1')  # 跳转首页

    def test_order(self):
        """订单测试方法"""
        self.index_proxy.go_to_goods_cart()  # 跳转我的购物车
        self.goods_cart_proxy.go_to_order_check()  # 去结算
        self.order_check_proxy.submit_order_func()  # 提交订单
        # 获取订单结果
        result = get_tip_text('订单提交成功')
        # 设置断言判断测试结果
        self.assertTrue(result)

    def test_pay(self):
        """订单支付测试方法"""
        self.index_proxy.go_to_my_order()  # 点击我的订单

        # 切换新窗口
        switch_new_window()
        # handles = self.driver.window_handles
        # self.driver.switch_to.window(handles[-1])

        self.my_order_proxy.go_to_order_pay()  # 点击立即支付

        # 切换新窗口
        switch_new_window()
        # handles = self.driver.window_handles
        # self.driver.switch_to.window(handles[-1])

        self.order_pay_proxy.order_pay_func()  # 确认支付
        # 获取支付结果
        result = get_tip_text('订单提交成功')
        # 设置断言判断测试结果
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
