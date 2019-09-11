"""
我的订单页面
"""
from selenium.webdriver.common.by import By
from base.base_page import BasePage, BaseHandle


class MyOrderPage(BasePage):
    """我的订单-对象库层"""

    def __init__(self):
        super().__init__()  # 获取浏览器对象

        self.wait_for_pay = (By.LINK_TEXT, '待付款')  # 待付款
        self.pay_now = (By.LINK_TEXT, '立即支付')  # 立即支付

    def find_wait_for_pay(self):
        """待支付定位方法"""
        return self.find_element_func(self.wait_for_pay)

    def find_pay_now(self):
        """立即支付定位方法"""
        return self.find_element_func(self.pay_now)


class MyOrderHandle(BaseHandle):
    """我的订单-操作层"""

    def __init__(self):
        self.my_order_page = MyOrderPage()  # 元素定位对象

    def click_wait_for_pay(self):
        """待支付点击方法"""
        self.click_element(self.my_order_page.find_wait_for_pay())

    def click_pay_now(self):
        """立即支付点击方法"""
        self.click_element(self.my_order_page.find_pay_now())


class MyOrderProxy(object):
    """我的订单-业务层"""

    def __init__(self):
        self.my_order_handle = MyOrderHandle()  # 操作对象

    def go_to_order_pay(self):
        """跳转订单支付页面"""
        self.my_order_handle.click_wait_for_pay()  # 点击待支付
        self.my_order_handle.click_pay_now()  # 点击立即支付
