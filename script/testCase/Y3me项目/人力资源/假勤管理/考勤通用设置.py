# -*-CodeIng:utf-8 -*-
# @time :2019/10/22 19:42
# @author:HuangJunTao
# @email:1341890679@qq.com
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
		# driver.find_element_by_xpath('//*[@id="_dropdown_popcontainer"]/div/i').click()
		# driver.find_element_by_xpath('//*[@id="home_header"]//div[text()="UI测试专属"]').click()
		# driver.find_element_by_xpath('//button[@class="u-button btn__style___37bsb u8c_primary__style___RFibc  btn__style___20DQM "]').click()
		# sleep(2)
		#左上方公共节点
		driver.find_element_by_class_name('lebra-navbar-left-icon').click()
		sleep(2)
		#进入社交协同
		driver.find_element_by_xpath('//*[text()="人力资源"]').click()
		sleep(1)
		#进入一级节点
		menu2 = driver.find_element_by_css_selector('span[title="假勤管理"]')
		actions = ActionChains(driver)
		actions.move_to_element(menu2)
		actions.click(menu2)
		actions.perform()
		sleep(1)
		# 进入二级节点
		driver.find_element_by_xpath('//li[@title="考勤通用设置"]').click()
		sleep(2)

		# 跳转考勤通用规则iframe
		iframe = driver.find_element_by_id('HRJQ020140')
		# # driver.switch_to.frame(iframe)
		SwitchTo(driver).frame(iframe)
		sleep(1)

		# 点击编辑按钮
		driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div/button').click()
		sleep(2)
		# 点击保存按钮
		driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/button[2]').click()

		sleep(0.5)
		text = driver.find_element_by_xpath('/html/body/div[2]/p[text()="操作成功"]').text
		self.assertEqual("操作成功",text)

		# 关闭当前页面
		driver.switch_to.default_content()
		sleep(1)
		driver.find_element_by_xpath('//*[@id="home_header"]/div/div[3]/ul/li/div').click()

