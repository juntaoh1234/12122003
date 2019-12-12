# coding=utf-8
from time import sleep

from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from SRC.webdriver.switchTo import SwitchTo
from script.common import utils
from selenium.webdriver import ActionChains


class EasyCase(TestCase):
	def __init__(self, webDriver, paramsList):
		# 请不要修改该方法124421
		super(EasyCase, self).__init__(webDriver, paramsList)

	@codeException_dec('3')
	def runTest(self):
		driver = self.getDriver()
		driver.implicitly_wait(30)
		param = self.param
		tool  = utils
		driver.refresh()
		driver.find_element_by_xpath('//*[@id="_dropdown_popcontainer"]/div/i').click()
		driver.find_element_by_xpath('//*[@id="home_header"]//div[text()="UI测试专属"]').click()
		driver.find_element_by_xpath('//button[@class="u-button btn__style___37bsb u8c_primary__style___RFibc  btn__style___20DQM "]').click()
		sleep(2)
		#左上方公共节点
		driver.find_element_by_class_name('lebra-navbar-left-icon').click()
		sleep(2)
		#进入社交协同
		driver.find_element_by_xpath('//*[text()="社交协同"]').click()
		sleep(2)
		#进入一级节点
		menu2 = driver.find_element_by_css_selector('span[title="社交沟通"]')
		actions = ActionChains(driver)
		actions.move_to_element(menu2)
		actions.click(menu2)
		actions.perform()
		sleep(2)
		# 进入二级节点
		driver.find_element_by_xpath('//li[@title="云直播"]').click()
		cookie = driver.get_cookies()
		print(cookie)
		print(driver.get_cookie('acw_tc'))

		sleep(2)
		# 跳转我的申请iframe

		iframe = driver.find_element_by_id('XTYUNZHIBO001')
		# print(response.json())
		# # driver.switch_to.frame(iframe)
		SwitchTo(driver).frame(iframe)
		driver
		print(driver.title)
		print(driver.current_url)
