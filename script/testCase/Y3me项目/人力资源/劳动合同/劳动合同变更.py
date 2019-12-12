# coding=utf-8
from time import sleep

from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from SRC.webdriver.switchTo import SwitchTo
from script.common import utils
from selenium.webdriver import ActionChains
from SRC.param import context


class EasyCase(TestCase):
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
        # driver.find_element_by_xpath('//button[@class="u-button btn__style___37bsb u8c_primary__style___RFibc  btn__style___20DQM "]').click()
        # sleep(2)
        # 左上方公共节点
        driver.find_element_by_class_name('lebra-navbar-left-icon').click()
        sleep(2)
        # 进入社交协同
        driver.find_element_by_xpath('//*[text()="人力资源"]').click()
        sleep(2)
        # 进入一级节点
        menu2 = driver.find_element_by_css_selector('span[title="劳动合同"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()
        sleep(2)
        # 进入二级节点
        driver.find_element_by_xpath('//li[@title="劳动合同变更"]').click()

        sleep(2)
        # 跳转劳动合同签订iframe
        iframe = driver.find_element_by_id('HRGXFW100')
        # # driver.switch_to.frame(iframe)
        SwitchTo(driver).frame(iframe)
        sleep(2)

        # 点击新增按钮
        driver.find_element_by_xpath('//div[@class="staff-info-control-btn fr"]//button/span[text()="新增"]').click()
        sleep(2)

        # 点击左侧书按钮
        driver.find_element_by_xpath('//span[@class="button level0 switch noline_close"]').click()

        # 点击二级的左侧树按钮
        driver.find_element_by_xpath('//span[text()="仓储中心-北京"]/ancestor::a/preceding-sibling::span').click()

        # 选择组织信息
        driver.find_element_by_xpath('//span[text()="仓储中心-北京"]/ancestor::a/following-sibling::ul//span[text()="仓储中心-北京"]').click()
        sleep(1)

        # 搜索框输入信息

        driver.find_element_by_xpath('//*[@id="searchVal"]').send_keys(context.Name.random_name)

        # driver.find_element_by_xpath('//*[@id="searchVal"]').send_keys("戴英")

        # 点击搜索按钮
        driver.find_element_by_xpath('//*[@id="searchBtn"]/span/i[2]').click()

        # 点击全选按钮
        driver.find_element_by_xpath('//*[@id="staffAllBody"]/div[2]/table/tbody/tr[1]/td[1]/div/div/label').click()

        # 点击确定按钮
        driver.find_element_by_xpath('//*[@id="addSignsDialog"]//button[@class="btn btn-primary"]').click()

        sleep(5)

        # 选择合同主体
        driver.find_element_by_xpath('//*[@id="edit_20180621190746PpsOFg6Vnl"]/div/span[1]').click()
        driver.find_element_by_xpath('//*[@id="refContainer20180621190746PpsOFg6Vnl"]//td[text()="0001"]').click()

        # 输入合同期限
        driver.find_element_by_xpath('//*[@id="201806211908070NEwyFzolD"]').send_keys(6)

        # 合同开始日期
        driver.find_element_by_xpath('//*[@id="edit_20180621190812GDKslgUlmo"]/div/span[1]').click()
        driver.find_element_by_xpath(
            '//div[@class="u-date-panel is-visible"]//div[@class="u-date-cell current"]').click()

        # 输入地点
        driver.find_element_by_xpath('//*[@id="edit_20180621190819Z3b5koMqqu"]/div/span[1]').click()
        driver.find_element_by_xpath('//*[@id="refContainer20180621190819Z3b5koMqqu"]//td[text()="123"]').click()

        # 输入备注信息
        driver.find_element_by_xpath('//*[@id="20180621190824BP0sLbdJLa"]').send_keys(context.get_paragraph())

        # 点击保存按钮
        driver.find_element_by_xpath('//*[@id="templatePanel"]/div[4]/button//span[text()="保存"]').click()
        sleep(5)

        # 点击提交按钮
        driver.find_element_by_xpath('//span[text()="提交"]/ancestor::button[@class="btn btn-primary"]').click()
        sleep(2)
        # 关闭当前页面
        driver.switch_to.default_content()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="home_header"]/div/div[3]/ul/li/div').click()