# coding=utf-8
from time import time, sleep

from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from script.common import utils
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import random


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
        driver.find_element_by_xpath('//*[text()="财务管理"]').click()
        sleep(1)
        # 进入一级节点
        menu2 = driver.find_element_by_css_selector('span[title="费用管理"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()
        sleep(1)
        # 进入二级节点
        menu3 = driver.find_element_by_css_selector('li[class="bottomBar"][title="费用预算"]')
        actions.move_to_element(menu3)
        actions.click(menu3)
        actions.perform()

        sleep(1)
        titleName = driver.find_element_by_css_selector(
            '#home_header > div > div.tab--38iB- > ul > li > p').get_attribute('title')
        assert u"费用预算" in titleName, u"页面源码中不存在该关键字！"
        sleep(1)
        iframe = driver.find_element_by_id('FICO_FYYS')
        driver.switch_to.frame(iframe)

        # 点击新增
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//button[text()="新增"]')))
        driver.find_element_by_xpath('//*[text()="新增"]').click()

        # 点击取消
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//button[text()="取消"]')))
        driver.find_element_by_xpath('//*[text()="取消"]').click()

        # 点击新增
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//button[text()="新增"]')))
        driver.find_element_by_xpath('//*[text()="新增"]').click()

        # 输入预算编码
        num1 = random.randint(999, 10000)
        code = '预算编码{}'.format(num1)
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//label[text()="预算编码"]/following-sibling::div//input')))
        driver.find_element_by_xpath('//label[text()="预算编码"]/following-sibling::div//input').send_keys(code)

        # 输入预算名称
        num1 = random.randint(999, 10000)
        name = '预算名称{}'.format(num1)
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//label[text()="预算名称"]/following-sibling::div//input')))
        driver.find_element_by_xpath('//label[text()="预算名称"]/following-sibling::div//input').send_keys(name)

        # 点击确定按钮
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(driver.find_element_by_xpath('//button[text()="确定"]')))
        driver.find_element_by_xpath('//button[text()="确定"]').click()

        # 点击配置按钮
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(
                driver.find_element_by_xpath('//div[text()="{}"]/ancestor::tr//a[text()="配置"]'.format(name))))
        driver.find_element_by_xpath('//div[text()="{}"]/ancestor::tr//a[text()="配置"]'.format(name)).click()

        # 点击可见员工
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(
                driver.find_element_by_xpath('//div[text()="预算可见(员工)"]/following-sibling::div//input')))
        driver.find_element_by_xpath('//div[text()="预算可见(员工)"]/following-sibling::div//input').click()

        # 选择第一条数据
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(
                driver.find_element_by_xpath('//ul[@role="listbox"]/li[1]')))
        driver.find_element_by_xpath('//ul[@role="listbox"]/li[1]').click()

        # 点击预算名称
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(
                driver.find_element_by_xpath('//div[text()="预算名称"]')))
        driver.find_element_by_xpath('//div[text()="预算名称"]').click()

        # 点击预见可见角色
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(
                driver.find_element_by_xpath('//div[text()="预算可见(角色)"]/following-sibling::div//input')))
        driver.find_element_by_xpath('//div[text()="预算可见(角色)"]/following-sibling::div//input').click()
        sleep(2)

        # 选择第一条数据
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(
                driver.find_element_by_xpath('//ul[@role="listbox"]/li[text()="文库管理员"]/i')))
        driver.find_element_by_xpath('//ul[@role="listbox"]/li[text()="文库管理员"]/i').click()

        # 点击预算名称
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(
                driver.find_element_by_xpath('//div[text()="预算名称"]')))
        driver.find_element_by_xpath('//div[text()="预算名称"]').click()

        # 点击确定按钮
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(
                driver.find_element_by_xpath('//button[text()="确定"]')))
        driver.find_element_by_xpath('//button[text()="确定"]').click()

        # 点击编制按钮
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(
                driver.find_element_by_xpath('//div[text()="{}"]/ancestor::tr//a[text()="编制"]'.format(name))))
        driver.find_element_by_xpath('//div[text()="{}"]/ancestor::tr//a[text()="编制"]'.format(name)).click()

        # 点击输入预算维度
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(
                driver.find_element_by_xpath('//span[text()="预算维度："]/following-sibling::div[1]//input')))
        driver.find_element_by_xpath('//span[text()="预算维度："]/following-sibling::div[1]//input').click()

        # 点击选择第一条数据
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(
                driver.find_element_by_xpath('//ul[@role="listbox"]/li[text()="费用承担部门"]')))
        driver.find_element_by_xpath('//ul[@role="listbox"]/li[text()="费用承担部门"]').click()

        # 点击确定
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(
                driver.find_element_by_xpath('//button[text()="确认"]')))
        driver.find_element_by_xpath('//button[text()="确认"]').click()

        # 弹出框点击修改
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(
                driver.find_element_by_xpath('//button[@class="ant-btn ant-btn-danger"]')))
        driver.find_element_by_xpath('//button[@class="ant-btn ant-btn-danger"]').click()

        # 点击费用承担部门
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(
                driver.find_element_by_xpath(
                    '//div[@class="react-bs-table-container react-bs-table-grid"]//tbody/tr[1]/td[3]')))
        driver.find_element_by_xpath(
            '//div[@class="react-bs-table-container react-bs-table-grid"]//tbody/tr[1]/td[3]').click()

        # 点击第一条
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(
                driver.find_element_by_xpath(
                    '//ul[@class="dropdown-menu bootstrap-typeahead-menu dropdown-menu-justify"]//li[1]')))
        driver.find_element_by_xpath(
            '//ul[@class="dropdown-menu bootstrap-typeahead-menu dropdown-menu-justify"]//li[1]').click()

        # 点击上半年输入预算
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(
                driver.find_element_by_xpath(
                    '//div[@class="react-bs-table-container react-bs-table-grid"]//tbody/tr[1]/td[4]')))
        driver.find_element_by_xpath(
            '//div[@class="react-bs-table-container react-bs-table-grid"]//tbody/tr[1]/td[4]').click()
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(
                driver.find_element_by_xpath(
                    '//div[@class="react-bs-table-container react-bs-table-grid"]//tbody/tr[1]/td[4]//input')))
        driver.find_element_by_xpath(
            '//div[@class="react-bs-table-container react-bs-table-grid"]//tbody/tr[1]/td[4]//input').send_keys(9000)

        # 点击上半年输入预算
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(
                driver.find_element_by_xpath(
                    '//div[@class="react-bs-table-container react-bs-table-grid"]//tbody/tr[1]/td[5]')))
        driver.find_element_by_xpath(
            '//div[@class="react-bs-table-container react-bs-table-grid"]//tbody/tr[1]/td[5]').click()
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(
                driver.find_element_by_xpath(
                    '//div[@class="react-bs-table-container react-bs-table-grid"]//tbody/tr[1]/td[5]//input')))
        driver.find_element_by_xpath(
            '//div[@class="react-bs-table-container react-bs-table-grid"]//tbody/tr[1]/td[5]//input').send_keys(9000)

        # 点击保存
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(
                driver.find_element_by_xpath('//button[text()="保存"]')))
        driver.find_element_by_xpath('//button[text()="保存"]').click()

        # 点击启用
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(
                driver.find_element_by_xpath('//button[text()="启用"]')))
        driver.find_element_by_xpath('//button[text()="启用"]').click()

        # 点击预算导入
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(
                driver.find_element_by_xpath('//button[text()="预算调整"]')))
        driver.find_element_by_xpath('//button[text()="预算调整"]').click()

        # 点击调整金额输入框
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(
                driver.find_element_by_xpath(
                    '//div[@class="react-bs-table-container react-bs-table-grid"]//tbody/tr[1]/td[9]')))
        driver.find_element_by_xpath(
            '//div[@class="react-bs-table-container react-bs-table-grid"]//tbody/tr[1]/td[9]').click()

        # 输入调整金额
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(
                driver.find_element_by_xpath(
                    '//div[@class="react-bs-table-container react-bs-table-grid"]//tbody/tr[1]/td[9]//input')))
        driver.find_element_by_xpath(
            '//div[@class="react-bs-table-container react-bs-table-grid"]//tbody/tr[1]/td[9]//input').send_keys(8000)

        # 点击保存按钮
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(
                driver.find_element_by_xpath('//button[text()="保存"]')))
        driver.find_element_by_xpath('//button[text()="保存"]').click()

        # 断言
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(
                driver.find_element_by_xpath('//span[text()="保存成功"]')))
        text = driver.find_element_by_xpath('//span[text()="保存成功"]').text
        self.assertEqual(text, '保存成功')

        # 点击返回按钮
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(
                driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]')))
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]').click()

        # # 点击关闭按钮
        # WebDriverWait(driver, 30, 0.5).until(
        #     ec.visibility_of(
        #         driver.find_element_by_xpath('//button[@aria-label="Close"]')))
        # driver.find_element_by_xpath('//button[@aria-label="Close"]').click()

        # 点击返回按钮
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(
                driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]')))
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]').click()

        # 点击删除按钮
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(
                driver.find_element_by_xpath('//div[text()="{}"]/ancestor::tr//a[text()="删除"]'.format(name))))
        driver.find_element_by_xpath('//div[text()="{}"]/ancestor::tr//a[text()="删除"]'.format(name)).click()

        # 点击确定
        WebDriverWait(driver, 30, 0.5).until(
            ec.visibility_of(
                driver.find_element_by_xpath('//button[@class="ant-btn ant-btn-danger"]')))
        driver.find_element_by_xpath('//button[@class="ant-btn ant-btn-danger"]').click()

        # 断言
        self.assertNotIn(name, driver.page_source)

        driver.switch_to.default_content()
        driver.find_element_by_class_name('u-button').click()
        sleep(1)
        driver.find_element_by_class_name('u-dropdown-menu-item').click()
