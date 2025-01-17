# coding=utf-8

from projectTest.chapter7.test.pages.loginPage import LoginPage
import unittest


class TestLogout(unittest.TestCase):
    """测试退出登录功能"""

    @classmethod
    def setUpClass(cls):
        cls.login = LoginPage()
        cls.login.login()

    @classmethod
    def tearDownClass(cls):
        cls.login.quit_driver()

    def test_logout01(self):
        """测试退出登录"""
        self.login.log_out()


if __name__ == '__main__':
    unittest.main()
