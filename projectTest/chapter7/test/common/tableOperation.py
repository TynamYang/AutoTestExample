# coding=utf-8

from selenium.webdriver.common.by import By
from time import sleep


class TableOperation(object):
    """表格操作"""
    def __init__(self, driver):
        self.driver = driver

    def get_table(self):
        """获取table
            返回table的headers、body_rows和body_rows_column
        """
        sleep(1)

        # table、header、body_rows、body_rows_columns
        table_header_body = [{'table #dataArea>table': By.CSS_SELECTOR,
                              'table #dataArea>table>.header>td': By.CSS_SELECTOR,
                              "table #dataArea>table>tr:not(.header)": By.CSS_SELECTOR,
                              "table #dataArea>table>tr:not(.header)>td": By.CSS_SELECTOR},
                       ]

        # 获取画面显示的table
        for table in table_header_body:
            keys = list(table.keys())
            values = list(table.values())

            # 如果找到的父节点为空，则父节点不存在，则查找的table不匹配,在页面中不存在
            if len(self.driver.find_elements(values[0], keys[0])) > 0:
                    table = self.driver.find_element(values[0], keys[0])
                    headers = table.find_elements(values[1], keys[1])
                    body_rows = table.find_elements(values[2], keys[2])
                    rows = []
                    for body_rows in body_rows:
                        body_rows_column = body_rows.find_elements(values[3], keys[3])
                        rows.append(body_rows_column)
                    return headers, rows
            else:
                print("table定位失败")
                return

    def select_row(self, header_text, row_text):
        """
        根据header中的列获取对应的body中的行
        :param header_text: header 中列内容
        :param body_text: leader列对应的body列内容
        :return: 返回body中的行
        """
        headers, rows = self.get_table()

        # 获取传入的header的index
        idx = int()
        for header in headers:
            if header.text == header_text:
                idx = headers.index(header)

        # 通过index在body中寻找相应index的内容
        for row in rows:
            if row[idx].text == row_text:
                return row

    def row_click(self, header_text, row_text):
        """选择表格中行并且点击"""
        row = self.select_row(header_text, row_text)
        # 返回的row是一个list，driver不能进行点击操作，所有需要给具体的值
        # 如果返回的row中有button，可以给出button的index实现row中button点击
        return row[0].click()


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://localhost:35524/#/')
    sleep(1)
    driver.find_element(By.CLASS_NAME, "email").send_keys('admin@tynam.com')
    driver.find_element(By.CLASS_NAME, "password").send_keys('tynam123')
    driver.find_element(By.CSS_SELECTOR, ".login-btn>input[value='登  录']").click()
    sleep(1)
    table = TableOperation(driver)
    table.row_click("姓 名", "严寒")

