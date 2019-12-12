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
        menu3 = driver.find_element_by_css_selector('li[title="职能共享设置"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu3)
        actions.click(menu3)
        actions.perform()
        assert u"职能共享设置" in driver.page_source, u"页面源码中不存在该关键字！"
        sleep(3)

        # 切换iframe
        iframe = driver.find_element_by_id('GZTORG016')
        driver.switch_to.frame(iframe)

        # 新增
        driver.find_element_by_id('org_func_sharing_setting_list|btnAdd').click()
        # 组织单元
        driver.find_element_by_xpath('//label[text()="组织单元"]/../..//span[@class="ant-select-arrow"]').click()
        # 选择组织单元
        driver.find_element_by_xpath('//span[text()="yontest__yontest云创股份"]').click()
        # 部门
        driver.find_element_by_xpath('//label[text()="部门"]/../..//span[@class="ant-select-arrow"]').click()
        driver.find_element_by_xpath('//span[@title="12__采购部"]').click()
        # 增行
        driver.find_element_by_id('org_func_sharing_setting_card|btnAddRowItem').click()
        # 组织编码
        driver.find_element_by_xpath(
            '//div[@id="org_func_sharing_setting_card|org_func_sharing_setting_card_body_page_base_item"]//div[2]/div/div[1]//div[@class="textCol"]').click()
        driver.find_element_by_xpath('//div[@class="editCol"]//span[@class="ant-select-arrow"]').click()
        driver.find_element_by_xpath('//div[6]//span[@title="yontest__yontest云创股份"]/../span[1]').click()
        driver.find_element_by_xpath('//span[text()="bj_cczx__仓储中心-北京"]').click()

        # 业务职能
        driver.find_element_by_xpath('//div[@id="org_func_sharing_setting_card|org_func_sharing_setting_card_body_page_base_item"]//div[3]//div[3]//div[@class="textCol"]').click()
        driver.find_element_by_xpath(
            '//div[@id="org_func_sharing_setting_card|org_func_sharing_setting_card_body_page_base_item"]//div[3]//i').click()
        driver.find_element_by_xpath('//div[text()="库存"]').click()
        driver.find_element_by_xpath('//div[6]//span[text()="确 定"]').click()
        # 保存
        driver.find_element_by_id('org_func_sharing_setting_card|btnSave').click()

        # 新增
        driver.find_element_by_id('org_func_sharing_setting_list|btnAdd').click()
        # 组织单元
        driver.find_element_by_xpath('//label[text()="组织单元"]/../..//span[@class="ant-select-arrow"]').click()
        # 选择组织单元
        driver.find_element_by_xpath('//span[text()="yontest__yontest云创股份"]').click()
        # 部门
        driver.find_element_by_xpath('//label[text()="部门"]/../..//span[@class="ant-select-arrow"]').click()
        driver.find_element_by_xpath('//span[@title="bj_xssyb__销售事业部-北京"]').click()
        # 增行
        driver.find_element_by_id('org_func_sharing_setting_card|btnAddRowItem').click()
        # 组织编码
        driver.find_element_by_xpath(
            '//div[@id="org_func_sharing_setting_card|org_func_sharing_setting_card_body_page_base_item"]//div[2]/div/div[1]//div[@class="textCol"]').click()
        driver.find_element_by_xpath('//div[@class="editCol"]//span[@class="ant-select-arrow"]').click()
        driver.find_element_by_xpath('//div[6]//span[@title="yontest__yontest云创股份"]/../span[1]').click()
        driver.find_element_by_xpath('//span[text()="bj_cczx__仓储中心-北京"]').click()

        # 业务职能
        driver.find_element_by_xpath(
            '//div[@id="org_func_sharing_setting_card|org_func_sharing_setting_card_body_page_base_item"]//div[3]//div[3]//div[@class="textCol"]').click()
        driver.find_element_by_xpath(
            '//div[@id="org_func_sharing_setting_card|org_func_sharing_setting_card_body_page_base_item"]//div[3]//i').click()
        driver.find_element_by_xpath('//div[text()="其他"]').click()
        driver.find_element_by_xpath('//div[6]//span[text()="确 定"]').click()
        # 保存
        driver.find_element_by_id('org_func_sharing_setting_card|btnSave').click()

        # 启用
        driver.find_element_by_xpath('//div[@id="container"]//div[text()="bj_xssyb"]').click()
        driver.find_element_by_xpath('//span[text()="启 用"]/../..//i').click()
        driver.find_element_by_xpath('//li[text()="启用"]').click()

        # 编辑
        data = driver.find_element_by_xpath('//div[@id="container"]//div[text()="12"]')
        ActionChains(driver).move_to_element(data).perform()
        driver.find_element_by_xpath('//a[text()="编辑"]').click()
        # 保存
        driver.find_element_by_id('org_func_sharing_setting_card|btnSave').click()
        # driver.find_element_by_xpath('//label[text()="部门"]/../..//span[@class="ant-select-arrow"]').click()
        # driver.find_element_by_xpath('//span[@title="bj_xssyb__销售事业部-北京"]').click()
        # driver.find_element_by_id('org_func_sharing_setting_card|btnSave').click()

        # 停用
        driver.find_element_by_xpath('//div[text()="组织编码"]').click()
        data = driver.find_element_by_xpath('//div[@id="container"]//div[text()="12"]')
        ActionChains(driver).move_to_element(data).perform()
        driver.find_element_by_xpath('//a[text()="停用"]').click()

        # 搜索
        driver.find_element_by_xpath('//div[text()="组织编码"]/../..//input').send_keys("yon")
        driver.find_element_by_xpath('//span[text()="搜 索"]').click()

        # 删除
        driver.find_element_by_xpath('//div[@id="container"]//div[text()="12"]').click()
        driver.find_element_by_id('org_func_sharing_setting_list|btnBatchDelete').click()
        sleep(3)
        driver.find_element_by_xpath('//button/span[text()="确 定"]').click()

        # 返回主窗体
        driver.switch_to.default_content()

        # 关闭页签
        driver.find_element_by_css_selector('button[class="u-button"]').click()
        driver.find_element_by_css_selector('li[title="关闭全部页签"]').click()

