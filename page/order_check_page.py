"""
订单确认页面
"""
from selenium.webdriver.common.by import By
from base.base_page import BasePage, BaseHandle


class OrderCheckPage(BasePage):
    """订单确认-对象库层"""

    def __init__(self):
        super().__init__()  # 获取浏览器对象

        self.submit_order_btn = (By.LINK_TEXT, '提交订单')  # 提交订单按钮

    def find_submit_order_btn(self):
        """提交订单按钮定位方法"""
        return self.find_element_func(self.submit_order_btn)


class OrderCheckHandle(BaseHandle):
    """订单确认-操作层"""

    def __init__(self):
        self.order_check_page = OrderCheckPage()  # 元素定位对象

    def click_submit_order_btn(self):
        """提交订单按钮点击方法"""
        self.click_element(self.order_check_page.find_submit_order_btn())


class OrderCheckProxy(object):
    """订单确认-业务层"""

    def __init__(self):
        self.order_check_handle = OrderCheckHandle()  # 操作对象

    def submit_order_func(self):
        """提交订单方法"""
        self.order_check_handle.click_submit_order_btn()
