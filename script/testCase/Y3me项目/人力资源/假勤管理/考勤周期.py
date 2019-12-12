# coding=utf-8
import random
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
		driver.find_element_by_xpath('//li[@title="考勤周期"]').click()

		sleep(2)
		# 跳转劳动合同签订iframe
		iframe = driver.find_element_by_id('HRJQ020100')
		# # driver.switch_to.frame(iframe)
		SwitchTo(driver).frame(iframe)
		sleep(1)
		# 点击新建考勤周期
		driver.find_element_by_xpath('//ul[@class="attend_type_list___header"]/li[1]').click()
		sleep(2)
		# 输入考勤名称
		num = random.randint(1000,9999)
		name = "考勤{}".format(num)
		driver.find_element_by_xpath('//label[text()="考勤周期名称"]/parent::div//input').send_keys(name)
		# 选择组织按钮
		driver.find_element_by_xpath('//label[text()="所属组织"]/parent::div//i[2]').click()
		sleep(3)
		# 选择北京仓储中心
		driver.find_element_by_xpath('//div[@class="el-tree-node__content"]//span[text()="仓储中心-北京"]').click()
		sleep(1)

		# 点击确定按钮
		driver.find_element_by_xpath('//div[@class="op-button"]//button[@class="el-button el-button--primary"]').click()
		sleep(2)
		# 点击保存按钮
		driver.find_element_by_xpath('//div[@aria-label="新增考勤周期方案"]//button[@class="el-button el-button--primary"]').click()

		#  断言
		self.assertIn(name,driver.page_source)

		# 点击新增
		driver.find_element_by_xpath('//*[@id="attend-period"]//button/span[text()="新增"]').click()

		sleep(2)
		# 点击保存按钮
		driver.find_element_by_xpath('//div[@aria-label="生成考勤周期"]//span[text()="保存"]').click()

		# 点击编辑
		driver.find_element_by_xpath('//*[@id="attend-period"]/div/div[1]/div/div[1]/ul/li[3]').click()
		sleep(1)

		# 点击保存
		driver.find_element_by_xpath('//div[@aria-label="编辑考勤周期方案"]//button/span[text()="保存"]').click()
		sleep(0.5)
		# 断言
		text = driver.find_element_by_xpath('/html/body//p[text()="操作成功"]').text

		self.assertEqual("操作成功",text)

		# 点击删除
		driver.find_element_by_xpath('//*[@id="attend-period"]/div/div[1]/div/div[1]/ul/li[2]').click()

		# 弹出框点击确认
		driver.find_element_by_xpath('//div[@aria-label="提示"]//button[@class="el-button el-button--default el-button--small el-button--primary "]').click()
		sleep(0.5)

		text_dele = driver.find_element_by_xpath('/html/body//p[text()="操作成功"]').text

		self.assertEqual("操作成功",text_dele)

		# 关闭当前页面
		driver.switch_to.default_content()
		sleep(1)
		driver.find_element_by_xpath('//*[@id="home_header"]/div/div[3]/ul/li/div').click()



