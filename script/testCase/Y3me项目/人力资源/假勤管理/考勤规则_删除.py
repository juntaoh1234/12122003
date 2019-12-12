# coding=utf-8
import random
from time import sleep

from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from SRC.webdriver.switchTo import SwitchTo
from script.common import utils
from selenium.webdriver import ActionChains


class EasyCase(TestCase):
    str_regular = None

    def __init__(self, webDriver, paramsList):
        # 请不要修改该方法124421
        super(EasyCase, self).__init__(webDriver, paramsList)

    @codeException_dec('3')
    def runTest(self):
        driver = self.getDriver()
        driver.implicitly_wait(30)
        param = self.param
        tool = utils
        driver.refresh()
        # driver.find_element_by_xpath('//*[@id="_dropdown_popcontainer"]/div/i').click()
        # driver.find_element_by_xpath('//*[@id="home_header"]//div[text()="UI测试专属"]').click()
        # driver.find_element_by_xpath(
        #     '//button[@class="u-button btn__style___37bsb u8c_primary__style___RFibc  btn__style___20DQM "]').click()
        # sleep(2)
        # 左上方公共节点
        driver.find_element_by_class_name('lebra-navbar-left-icon').click()
        sleep(2)
        # 进入社交协同
        driver.find_element_by_xpath('//*[text()="人力资源"]').click()
        sleep(2)
        # 进入一级节点
        menu2 = driver.find_element_by_css_selector('span[title="假勤管理"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()
        sleep(2)
        # 进入二级节点
        driver.find_element_by_xpath('//li[@title="考勤规则"]').click()

        sleep(2)
        # 跳转劳动合同签订iframe
        iframe = driver.find_element_by_id('HRJQ020010')
        # # driver.switch_to.frame(iframe)
        SwitchTo(driver).frame(iframe)
        sleep(2)
        source = driver.page_source
        str1 = 'new规则'
        # 点击新建规则按钮
        driver.find_element_by_xpath('//*[@id="attendance-rules-add"]//button/span[text()="新建规则"]').click()
        sleep(3)
        # 点击组织右侧按钮
        driver.find_element_by_xpath(
            '//div[@class="el-autocomplete reference-com formInput"]/div/span/span/span/i[2]').click()
        sleep(3)

        # 选中组织
        driver.find_element_by_xpath(
            '//*[@id="ref-tree-container"]/div/div/div/div[1]/div/div/div[1]/div[2]/div[1]/div/span[2]/span').click()

        # 点击确认
        driver.find_element_by_xpath(
            '//div[@class="el-dialog__wrapper custom-ref-dialog"]//button[@class="el-button el-button--primary"]').click()

        # 输入规则名称
        num = random.randint(10000, 99999)
        str_regular = "new规则{}".format(num)

        driver.find_element_by_xpath('//label[text()="规则名称"]/parent::div//div[@class="el-input"]/input').send_keys(
            str_regular)

        #  点击组织按钮
        driver.find_element_by_xpath('//div[@class="el-autocomplete reference-com"]//span[text()="选组织"]').click()
        sleep(3)
        # 选择北京仓储中心
        driver.find_element_by_xpath('//div[@role="dialog"]//span[text()="仓储中心-北京"]').click()

        # 点击确定按钮
        driver.find_element_by_xpath('//div[@role="dialog"]//button[@class="el-button el-button--primary"]').click()

        # 点击人员
        driver.find_element_by_xpath('//div[@class="el-autocomplete reference-com"]//span[text()="选人员"]').click()
        sleep(3)

        # 选择人员
        driver.find_element_by_xpath('//div[@role="dialog"]//span[text()="仓储中心-北京"]').click()
        sleep(2)
        # 点击全选按钮
        driver.find_element_by_xpath(
            '//div[@role="dialog"]//div[@style="height: 340px;"]//div[text()="名称"]//ancestor::tr//span[@class="el-checkbox__input"]').click()

        # 点击确定按钮
        driver.find_element_by_xpath('//div[@role="dialog"]//button[@class="el-button el-button--primary"]').click()

        # 点击班次，选择班次
        driver.find_element_by_xpath('//div[@class="el-autocomplete reference-com"]//span[text()="选班次"]').click()
        driver.find_element_by_xpath('//div[@role="dialog"]//tbody/tr[1]').click()

        # 点击确定按钮
        driver.find_element_by_xpath('//div[@role="dialog"]//button[@class="el-button el-button--primary"]').click()

        # 点击添加地理位置
        driver.find_element_by_xpath('//div[@class="el-autocomplete reference-com"]//span[text()="添加地理位置"]').click()

        #  选择一项
        driver.find_element_by_xpath('//div[@role="dialog"]//tbody/tr[1]//span[@class="el-checkbox__inner"]').click()

        # 点击确定按钮
        driver.find_element_by_xpath('//div[@role="dialog"]//button[@class="el-button el-button--primary"]').click()

        # 点击保存
        driver.find_element_by_xpath(
            '//*[@id="attendance-rules-add-edit"]//button[@class="el-button el-button--primary"]').click()
        sleep(2)
        if source.find(str1) >= 0:
            driver.find_element_by_xpath('//div[@class="el-message-box__btns"]/button[2]').click()
        # 组织没有被引用时，不需要覆盖。
        # sleep(2)
        # # 点击覆盖按钮
        # driver.find_element_by_xpath('//div[@class="el-message-box"]//button[@class="el-button el-button--default el-button--small el-button--primary "]').click()

        sleep(3)
        # 断言
        self.assertIn(str_regular, driver.page_source)

        # 编辑考勤规则
        driver.find_element_by_xpath(
            '//*[@id="attendance-rules-add"]//table/tbody//div[text()="{}"]/ancestor::tr//span[text()="编辑"]'.format(
                str_regular)).click()
        sleep(3)
        # 点击保存按钮
        driver.find_element_by_xpath('//button[@class="el-button el-button--primary"]').click()

        # 点击停用按钮
        driver.find_element_by_xpath(
            '//*[@id="attendance-rules-add"]//table/tbody//div[text()="{}"]/ancestor::tr//span[text()="停用"]'.format(
                str_regular)).click()
        sleep(1)
        # 点击确认
        driver.find_element_by_xpath(
            '//div[@class="el-message-box"]//button[@class="el-button el-button--default el-button--small el-button--primary "]').click()
        sleep(1)
        # 点击启用按钮
        driver.find_element_by_xpath(
            '//*[@id="attendance-rules-add"]//table/tbody//div[text()="{}"]/ancestor::tr//span[text()="启用"]'.format(
                str_regular)).click()
        sleep(1)

        # 点击停用按钮
        driver.find_element_by_xpath(
            '//*[@id="attendance-rules-add"]//table/tbody//div[text()="{}"]/ancestor::tr//span[text()="停用"]'.format(
                str_regular)).click()
        sleep(1)

        # 点击确认
        driver.find_element_by_xpath(
            '//div[@class="el-message-box"]//button[@class="el-button el-button--default el-button--small el-button--primary "]').click()
        sleep(1)

        # 点击删除按钮
        driver.find_element_by_xpath(
            '//*[@id="attendance-rules-add"]//table/tbody//div[text()="{}"]/ancestor::tr//span[text()="删除"]'.format(
                str_regular)).click()

        # 点击确定
        driver.find_element_by_xpath(
            '//div[@class="el-message-box"]//button[@class="el-button el-button--default el-button--small el-button--primary "]').click()
        print(str_regular)

        # 断言是否删除成功
        sleep(2)
        self.assertNotIn(str_regular, driver.page_source)

        # 关闭当前页面
        driver.switch_to.default_content()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="home_header"]/div/div[3]/ul/li/div').click()