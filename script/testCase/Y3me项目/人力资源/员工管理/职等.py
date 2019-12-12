from time import time, sleep

from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from script.common import utils
from selenium import webdriver
from selenium.webdriver import ActionChains


class EasyCase(TestCase):
    def __init__(self, webDriver, paramsList):
        # 请不要修改该方法124421
        super(EasyCase, self).__init__(webDriver, paramsList)

    @codeException_dec('3')
    def runTest(self):
        driver = self.getDriver()
        param = self.param
        tool = utils
        driver.refresh()

        # 左上方公共节点
        driver.find_element_by_class_name('lebra-navbar-left-icon').click()

        menu2 = driver.find_element_by_css_selector('span[title="组织管理"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()
        sleep(1)
        # 进入二级节点
        menu3 = driver.find_element_by_css_selector('li[title="职等"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu3)
        actions.click(menu3)
        actions.perform()
        assert u"职等" in driver.page_source, u"页面源码中不存在该关键字！"
        sleep(3)

        # 切换iframe
        iframe = driver.find_element_by_id('HRSZ020040')
        driver.switch_to.frame(iframe)
        # sleep(5)

        # 新增
        driver.find_element_by_id('gradelist|btnAdd').click()
        # 职等编号
        driver.find_element_by_xpath('//label[text()="职等编号"]/../..//input').send_keys("ZD001")
        # 职等名称
        driver.find_element_by_xpath('//label[text()="职等名称"]/../..//input').send_keys("正高职")
        # 保存
        driver.find_element_by_id('grade|btnSave').click()

        # 新增
        driver.find_element_by_id('gradelist|btnAdd').click()
        # 职等编号
        driver.find_element_by_xpath('//label[text()="职等编号"]/../..//input').send_keys("ZD002")
        # 职等名称
        driver.find_element_by_xpath('//label[text()="职等名称"]/../..//input').send_keys("副高职")
        # 保存并新增
        driver.find_element_by_id('grade|btnSaveAndAdd').click()
        # 取消
        driver.find_element_by_id("grade|btnAbandon").click()

        # 启用/停用
        driver.find_element_by_xpath('//div[text()="ZD001"]').click()
        ActionChains(driver).move_to_element(driver.find_element_by_xpath('//span[text()="启 用"]/../..//i')).perform()
        driver.find_element_by_xpath('//li[text()="启用"]').click()
        driver.find_element_by_xpath('//div[text()="名称/编码"]').click()

        # 编辑
        ActionChains(driver).move_to_element(driver.find_element_by_xpath('//div[text()="ZD001"]')).perform()
        driver.find_element_by_xpath('//a[text()="编辑"]').click()
        # 备注
        driver.find_element_by_xpath('//label[text()="备注"]/../..//input').send_keys("大学教师最高等级")
        # 保存
        driver.find_element_by_id('grade|btnSave').click()

        # 删除
        driver.find_element_by_xpath('//div[text()="ZD002"]').click()
        driver.find_element_by_id('gradelist|btnBatchDelete').click()
        sleep(3)
        driver.find_element_by_xpath('//div[@class="ant-confirm-btns"]//span[text()="确 定"]').click()

        # 搜索
        driver.find_element_by_xpath('//div[text()="名称/编码"]/..//input').send_keys("ZD001")
        driver.find_element_by_xpath('//span[text()="搜 索"]').click()
        sleep(5)

        # 返回主窗体
        driver.switch_to.default_content()

        # 关闭页签
        driver.find_element_by_css_selector('button[class="u-button"]').click()
        driver.find_element_by_css_selector('li[title="关闭全部页签"]').click()

