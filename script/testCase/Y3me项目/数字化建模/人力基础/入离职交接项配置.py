# coding=utf-8
from time import time, sleep

from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from script.common import utils
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


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
        sleep(1)
        # 进入财务管理
        driver.find_element_by_xpath('//*[text()="人力资源"]').click()
        sleep(1)
        # 进入一级节点
        menu2 = driver.find_element_by_css_selector('span[title="人力设置"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()
        sleep(1)
        # 进入二级节点
        menu3 = driver.find_element_by_css_selector('li[class="bottomBar"][title="入离职交接项配置"]')
        actions.move_to_element(menu3)
        actions.click(menu3)
        actions.perform()

        sleep(2)
        titleName = driver.find_element_by_css_selector(
            '#home_header > div > div.tab--38iB- > ul > li > p').get_attribute('title')
        assert u"入离职交接项配置" in titleName, u"页面源码中不存在该关键字！"
        sleep(2)
        iframe = driver.find_element_by_id('HRSZ030050')
        driver.switch_to.frame(iframe)

        # 新增
        driver.find_element_by_xpath('//*[contains(text(),"新增")]').click()
        sleep(2)
        driver.find_element_by_xpath(
            '//label[text()="组织"]/following-sibling::div//span[@class="el-input__suffix"]').click()
        sleep(0.5)
        driver.find_element_by_xpath(
            '//*[@id="ref-tree-container"]/div/div/div/div[1]/div/div/div[1]/div[2]/div/div[1]/span[1]').click()
        sleep(0.5)
        driver.find_element_by_xpath('//span//span[text()="仓储中心-北京"]').click()

        driver.find_element_by_xpath('//div[@class="op-button"]/button[2]').click()

        driver.find_element_by_xpath(
            '//label[text()="合同主体"]/following-sibling::div//span[@class="el-input__suffix"]').click()

        # 选择条目
        driver.find_element_by_xpath('//div[@class="el-table__body-wrapper is-scrolling-none"]//tbody/tr[1]').click()

        # 点击确定按钮
        driver.find_element_by_xpath('//div[@class="op-button"]/button[2]').click()

        # 输入工作地点
        driver.find_element_by_xpath(
            '//label[text()="工作地点"]/following-sibling::div//span[@class="el-input__suffix"]').click()

        # 选择一个条目
        driver.find_element_by_xpath('//div[@class="el-table__body-wrapper is-scrolling-none"]//tbody/tr[1]').click()

        # 点击确定按钮
        driver.find_element_by_xpath('//div[@class="op-button"]/button[2]').click()

        # 输入员工类别
        driver.find_element_by_xpath(
            '//label[text()="员工类别"]/following-sibling::div//span[@class="el-input__suffix"]').click()

        # 选择一个条目
        driver.find_element_by_xpath('//div[@class="el-table__body-wrapper is-scrolling-none"]//tbody/tr[1]').click()

        # 点击确定按钮
        driver.find_element_by_xpath('//div[@class="op-button"]/button[2]').click()

        driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div[2]/form/div[3]/div/div/div[1]//div[@class="el-col el-col-3"]//input[@placeholder="负责人"]').click()
        driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div[2]/form/div[3]/div/div/div[1]//div[@class="el-col el-col-3"]//input[@placeholder="负责人"]').send_keys(
            '黄俊涛')
        sleep(2)
        driver.find_element_by_xpath('//span[text()="黄俊涛(A00001)-仓储中心-北京"]').click()
        # # 点击第一条的负责人
        # driver.find_element_by_xpath(
        #     '//form/div[3]/div/div/div[1]/div[2]//i[@class="el-input__icon wui-liebiao"]').click()
        # sleep(2)
        #
        # # 点击展开按钮d
        # driver.find_element_by_xpath('//span[text()="yontest云创股份"]/parent::span/preceding-sibling::span').click()
        # sleep(0.5)
        #
        # # 选择仓储中心北京
        # driver.find_element_by_xpath('//span[text()="仓储中心-北京"]/parent::span').click()
        # sleep(1)
        # # 点击全选按钮
        # driver.find_element_by_xpath(
        #     '//div[@style="height: 340px;"]//div[text()="名称"]/ancestor::tr//span[@class="el-checkbox__inner"]').click()
        #
        # # 点击确定按钮
        # driver.find_element_by_xpath(
        #     '//button[@class="el-button el-button--primary"]/span[contains(text(),"确定")]').click()
        sleep(1)
        # 点击保存按钮
        driver.find_element_by_xpath('//div[@class="control-btn el-row"]/button[1]').click()
        sleep(2)
        # 点击删除按钮
        driver.find_element_by_xpath(
            '//div[@element-loading-spinner="iconfont wui-Loading"]//tbody/tr[1]//i[@class="el-tooltip iconfont wui-Dustbin_bold"]').click()
        sleep(1)
        # 点击确定按按钮
        driver.find_element_by_xpath(
            '//button[@class="el-button el-button--default el-button--small el-button--primary "]').click()

        # driver.find_element_by_xpath('//*[text()="取消"]').click()
        # driver.find_element_by_xpath('//div[@class="el-message-box__btns"]/button[2]').click()
        # driver.find_element_by_xpath('//div[@class="ant-confirm-btns"]//span[text()="确 定"]').click()

        driver.switch_to.default_content()
        driver.find_element_by_class_name('u-button').click()
        sleep(1)
        driver.find_element_by_class_name('u-dropdown-menu-item').click()
