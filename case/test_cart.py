"""
购物车-测试用例
"""
import unittest

from page.goods_detail_page import GoodsDetailProxy
from page.index_page import IndexProxy
from page.search_list_page import SearchListProxy
from utlis import DriverUtil


class TestCart(unittest.TestCase):
    """购物车测试类"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverUtil.get_driver()  # 获取浏览器对象
        cls.index_proxy = IndexProxy()  # 首页业务执行对象
        cls.search_list_proxy = SearchListProxy()  # 搜索列表页业务执行对象
        cls.goods_detail_proxy = GoodsDetailProxy()  # 商品详情业务执行对象

    @classmethod
    def tearDownClass(cls) -> None:
        DriverUtil.quit_driver()  # 退出浏览器对象

    def setUp(self) -> None:
        self.driver.get('http://127.0.0.1')  # 跳转首页

    def test_cart(self):
        """购物车测试方法"""
        goods_name = '小米手机5'
        self.index_proxy.go_to_search_list(goods_name)  # 搜索商品
        self.search_list_proxy.go_to_goods_detail(goods_name)  # 跳转商品详情
        self.goods_detail_proxy.add_cart_func()  # 添加购物车
        result = self.goods_detail_proxy.get_result()  # 获取添加结果
        # 断言判断测试结果
        self.assertIn('添加成功', result)


if __name__ == '__main__':
    unittest.main()
