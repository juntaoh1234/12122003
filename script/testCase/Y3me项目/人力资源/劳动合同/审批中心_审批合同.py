# coding=utf-8
from time import sleep

from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from SRC.webdriver.switchTo import SwitchTo


class EasyCase(TestCase):
	def __init__(self, webDriver, paramsList):
		# 请不要修改该方法124421
		super(EasyCase, self).__init__(webDriver, paramsList)

	@codeException_dec('3')
	def runTest(self):
		driver = self.getDriver()
		driver.implicitly_wait(30)
		driver.refresh()
		# driver.find_element_by_xpath('//*[@id="_dropdown_popcontainer"]/div/i').click()
		# driver.find_element_by_xpath('//*[@id="home_header"]//div[text()="UI测试专属"]').click()
		# driver.find_element_by_xpath('//button[@class="u-button btn__style___37bsb u8c_primary__style___RFibc  btn__style___20DQM "]').click()
		# sleep(2)

		# 第一次审批********************************
		driver.find_element_by_xpath('//div[text()="审批中心"]').click()

		# 跳转iframe
		iframe = driver.find_element_by_id('XTSPZX0001')
		SwitchTo(driver).frame(iframe)
		sleep(2)

		# 点击同意按钮
		driver.find_element_by_xpath('//div[@class="listContainer"]/div[1]//div[text()="同意"]').click()

		# # 点击审批中心关闭按钮
		# driver.find_element_by_xpath('//div[@class="close--MQT19"]//i').click()

		sleep(2)
		# 关闭当前页面
		driver.switch_to.default_content()
		sleep(1)
		driver.find_element_by_xpath('//*[@id="home_header"]/div/div[3]/ul/li/div').click()



