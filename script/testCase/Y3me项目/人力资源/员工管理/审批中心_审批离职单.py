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

		# 点击进入单据详情
		driver.find_element_by_xpath('//div[@class="listContainer"]/div[1]//div[@class="remarkMsg mb-flex remarkRetract"]').click()
		sleep(5)

		# 点击编辑按钮
		driver.find_element_by_xpath('//button[text()="编辑"]').click()
		sleep(1)

		# 点击离职后人员类别右侧按钮
		driver.find_element_by_xpath('//*[@id="edit_20180601133354FRlUm5dv5k"]/div/span[1]').click()

		# 选择人员类别
		driver.find_element_by_xpath('//span[text()="人员类别参照"]/ancestor::div[@class="outerContainer"]//td[text()="1123"]').click()


		# 点击保存
		driver.find_element_by_xpath('//button[@class="btn btn-primary btn-save" and text()="保存"]').click()
		sleep(3)


		# 点击审批输入域
		driver.find_element_by_xpath('//*[@id="currentApprove"]/textarea').send_keys("同意")

		# 点击确认离职按钮
		driver.find_element_by_xpath('//button[text()="确认离职"]').click()
		sleep(5)



		# 第二次审批**********************************
		driver.refresh()
		driver.find_element_by_xpath('//div[text()="审批中心"]').click()

		# 跳转iframe
		iframe = driver.find_element_by_id('XTSPZX0001')
		SwitchTo(driver).frame(iframe)
		sleep(2)


		# 点击进入单据详情
		driver.find_element_by_xpath('//div[@class="listContainer"]/div[1]//div[@class="remarkMsg mb-flex remarkRetract"]').click()
		sleep(5)

		# 点击审批输入域
		driver.find_element_by_xpath('//*[@id="currentApprove"]/textarea').send_keys("同意")

		# 点击确认离职按钮
		driver.find_element_by_xpath('//button[text()="确认离职"]').click()
		sleep(5)


		# 第三次审批**********************************
		driver.refresh()
		driver.find_element_by_xpath('//div[text()="审批中心"]').click()

		# 跳转iframe
		iframe = driver.find_element_by_id('XTSPZX0001')
		SwitchTo(driver).frame(iframe)
		sleep(2)

		# 点击同意按钮
		driver.find_element_by_xpath('//div[@class="listContainer"]/div[1]//div[text()="同意"]').click()


		# 关闭当前页面
		driver.switch_to.default_content()
		sleep(1)
		driver.find_element_by_xpath('//*[@id="home_header"]/div/div[3]/ul/li/div').click()








