# -*-CodeIng:utf-8 -*-
# @time :2019/10/22 19:42
# @author:HuangJunTao
# @email:1341890679@qq.com
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
		driver.find_element_by_xpath('//li[@title="休假规则"]').click()
		sleep(2)

		# 跳转休假规则iframe
		iframe = driver.find_element_by_id('HRJQ020060')
		# # driver.switch_to.frame(iframe)
		SwitchTo(driver).frame(iframe)
		sleep(1)

		# 点击新建规则
		driver.find_element_by_xpath('//button[@class="el-button el-button--primary"]').click()
		sleep(2)

		# 点击组织按钮
		driver.find_element_by_xpath('//*[@id="c57"]/div/span/span/span/i[2]').click()

		# 点击组织展开按钮
		driver.find_element_by_xpath('//span[text()="所属组织"]/ancestor::div[@role="dialog"]//div[@role="group"]/div[1]/div/span[1]').click()

		# 点击组织
		driver.find_element_by_xpath('//span[text()="所属组织"]/ancestor::div[@role="dialog"]//div[@role="group"]/div[1]/div/span[2]').click()

		# 点击确定按钮
		driver.find_element_by_xpath('//span[text()="所属组织"]/ancestor::div[@role="dialog"]//button[@class="el-button el-button--primary"]').click()
		sleep(1)

		# 输入姓名
		num = random.randint(1000,9999)
		name = "假勤方案{}".format(num)
		driver.find_element_by_xpath('//label[text()="规则名称"]/parent::div//input').send_keys(name)

		# 输入备注信息
		driver.find_element_by_xpath('//*[@id="basicInfo"]//textarea').send_keys("备注信息123456")
		sleep(1)

		# 点击保存按钮
		driver.find_element_by_xpath('//button[@class="el-button el-button--primary"]/span[text()="保存"]').click()
		sleep(0.5)

		# 断言
		text = driver.find_element_by_xpath('//p[text()="操作成功！"]').text
		self.assertEqual("操作成功！",text)

		# 点击编辑
		driver.find_element_by_xpath('//*[@id="basicInfo"]//button/span[text()="编辑"]').click()


		# 点击保存按钮
		driver.find_element_by_xpath('//div[@id="basicInfo"]//button[@class="el-button el-button--primary"]/span[text()="保存"]').click()

		# 断言
		text = driver.find_element_by_xpath('//p[text()="操作成功！"]').text
		self.assertEqual("操作成功！",text)
		driver.switch_to.default_content()
		ele = driver.find_element_by_xpath('//p[text()="休假规则"]')
		actions = ActionChains(driver)
		actions.move_to_element(ele)
		actions.perform()
		driver.find_element_by_xpath('//span[text()="刷新"]').click()
		sleep(1)
		# 跳转休假规则iframe
		iframe = driver.find_element_by_id('HRJQ020060')
		# # driver.switch_to.frame(iframe)
		SwitchTo(driver).frame(iframe)
		sleep(1)
		# 点击停用按钮
		driver.find_element_by_xpath('//div[text()="{}"]/ancestor::tr/td[6]/div/div[2]'.format(name)).click()

		# 点击确定
		driver.find_element_by_xpath('//div[@class="el-message-box"]//button[@class="el-button el-button--default el-button--small el-button--primary "]').click()
		sleep(0.5)
		text = driver.find_element_by_xpath('//p[text()="操作成功"]').text
		self.assertEqual("操作成功",text)
		sleep(1)
		# 点击启用按钮
		driver.find_element_by_xpath('//div[text()="{}"]/ancestor::tr/td[6]/div/div[2]'.format(name)).click()
		sleep(0.5)
		text = driver.find_element_by_xpath('//p[text()="操作成功"]').text
		self.assertEqual("操作成功",text)
		sleep(1)
		# 点击停用按钮
		driver.find_element_by_xpath('//div[text()="{}"]/ancestor::tr/td[6]/div/div[2]'.format(name)).click()

		# 点击确定
		driver.find_element_by_xpath('//div[@class="el-message-box"]//button[@class="el-button el-button--default el-button--small el-button--primary "]').click()
		sleep(0.5)
		text = driver.find_element_by_xpath('//p[text()="操作成功"]').text
		self.assertEqual("操作成功",text)
		sleep(1)
		# 点击删除
		driver.find_element_by_xpath('//div[text()="{}"]/ancestor::tr/td[6]/div/div[3]'.format(name)).click()

		# 点击确定
		driver.find_element_by_xpath('//div[@class="el-message-box"]//button[@class="el-button el-button--default el-button--small el-button--primary "]').click()

		sleep(0.5)
		text = driver.find_element_by_xpath('//p[text()="操作成功"]').text
		self.assertEqual("操作成功",text)

		sleep(2)
		# 关闭当前页面
		driver.switch_to.default_content()
		sleep(1)
		driver.find_element_by_xpath('//*[@id="home_header"]/div/div[3]/ul/li/div').click()

