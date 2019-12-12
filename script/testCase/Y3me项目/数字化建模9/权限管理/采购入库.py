# coding=utf-8
from time import time, sleep

from selenium.webdriver.common.by import By

from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from script.common import utils
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




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
        driver.find_element_by_xpath('//*[text()="采购供应"]').click()
        # 进入一级节点
        menu2 = driver.find_element_by_css_selector('span[title="库存管理"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu2)
        actions.click(menu2)
        actions.perform()
        sleep(1)
        # 进入二级节点
        menu3 = driver.find_element_by_css_selector('li[title="采购入库"]')
        actions = ActionChains(driver)
        actions.move_to_element(menu3)
        actions.click(menu3)
        actions.perform()
        assert u"采购入库" in driver.page_source, u"页面源码中不存在该关键字！"
        sleep(1)

        # 切换iframe
        iframe = driver.find_element_by_id('st_purinrecordlist')
        driver.switch_to.frame(iframe)

        # 增加
        driver.find_element_by_xpath('//span[text()="新 增"]').click()
        # 录入数据

        text = driver.find_element_by_xpath('//*[@id="st_purinrecord|org_name"]/div/div[1]/div[2]/div/div/div/span/input').get_attribute("value")
        print(text)
        if text == "仓储中心-北京":

            driver.find_element_by_xpath('//*[text()="收货组织"]/../..//i[@class="anticon anticon-canzhao"]').click()
            driver.find_element_by_xpath('//span[text()="显示全部"]').click()
            driver.find_element_by_xpath('//*[text()="bj_cczx"]').click()
            driver.find_element_by_xpath('//*[text()="收货组织参照"]/../..//button[2]').click()
            driver.find_element_by_xpath('//div[@class="ant-modal-mask"]/..//button[2]').click()


        driver.find_element_by_xpath('//*[text()="采购组织"]/../..//i[@class="anticon anticon-canzhao"]').click()
        driver.find_element_by_xpath('//*[@id="aa_orgpur"]//div[text()="yontest"]').click()
        driver.find_element_by_xpath('//div[@class="ant-modal-mask"]/..//span[text()="确 定"]').click()
        # driver.find_element_by_xpath('//label[text()="单据编号"]/../..//input').send_keys("sg001")

        driver.find_element_by_xpath('//*[text()="仓库"]/../..//i[@class="anticon anticon-canzhao"]').click()
        driver.find_element_by_xpath('//*[@id="aa_warehouse"]//div[2]//div[1]/div[2]//div[3]/div[1]//div[1]//label/span/input').click()
        driver.find_element_by_xpath('//div[@class="ant-modal-mask"]/..//span[text()="确 定"]').click()

        driver.find_element_by_xpath('//*[text()="供应商"]/../..//i[@class="anticon anticon-canzhao"]').click()
        driver.find_element_by_xpath('//*[@id="productcenter.aa_vendor"]//div[2]//div[1]/div[2]/div[1]/div[3]//div[1]/div[1]//label/span/input').click()
        driver.find_element_by_xpath('//div[@class="ant-modal-mask"]/..//span[text()="确 定"]').click()

        driver.find_element_by_xpath('//*[text()="币种名称"]/../..//i[@class="anticon anticon-canzhao"]').click()
        driver.find_element_by_xpath('//div[text()="人民币"]').click()
        driver.find_element_by_xpath('//div[@class="ant-modal-mask"]/..//span[text()="确 定"]').click()

        # 下拉滚动条
        ele1 = driver.find_element_by_xpath('//*[@id="st_purinrecord|btnAddRow"]')
        driver.execute_script('arguments[0].scrollIntoView();', ele1)
        print("执行了拖拽操作")

        # 切换到表体
        driver.find_element_by_xpath('//*[@id="st_purinrecord|btnMax_st_purinrecord_body_page"]/i').click()

        # 物料参照
        driver.find_element_by_xpath('//div[text()="1"]/ancestor::div[@class="fixedDataTableRowLayout_rowWrapper"]//div[@class="textCol"]').click()
        driver.find_element_by_xpath('//div[text()="1"]/ancestor::div[@class="fixedDataTableRowLayout_rowWrapper"]//div[@class="editCol"]//i').click()
        driver.find_element_by_xpath('//*[@id="aa_productsku"]/div[2]/div[2]//div[1]/div[2]/div[1]/div[3]/div[1]//label/span/input').click()
        driver.find_element_by_xpath('//div[@class="ant-modal-mask"]/..//span[text()="确 定"]').click()

        driver.find_element_by_xpath('//*[@id="st_purinrecord|st_purinrecord_body_page_base"]//div[3]//div[5]//div[@class="textCol"]').click()
        driver.find_element_by_xpath('//*[@id="st_purinrecord|st_purinrecord_body_page_base"]//div[3]//div[5]//div[@class="editCol"]//input').send_keys('1000')

        # 切换到单据
        driver.find_element_by_xpath('//*[@id="st_purinrecord|btnMax_st_purinrecord_body_page"]/i').click()

        #保存
        # 用JS点击
        search_button1 = driver.find_element_by_xpath('//span[text()="保存"]')
        driver.execute_script("arguments[0].click();", search_button1)
        sleep(5)
        # 鼠标悬浮
        article = driver.find_element_by_xpath('//*[@id="container"]//div[2]//div[2]/div[1]/div[2]/div[1]/div[3]/div[1]//label/span/input')
        ActionChains(driver).move_to_element(article).perform()
        # 蓝票
        driver.find_element_by_xpath('//*[@class="table-list-btn"and text()="蓝票"]').click()
        #修改蓝票
        driver.find_element_by_xpath('//label[text()="对方发票日期"]/../..//input').click()
        driver.find_element_by_xpath('//a[text()="今天"]').click()
        driver.find_element_by_xpath('//label[text()="对方发票号"]/../..//input').send_keys("0123456")
        driver.find_element_by_xpath('//label[text()="交易类型"]/../../div[@class="col-float label-control "]/..//i[@class="anticon anticon-canzhao"]').click()
        driver.find_element_by_xpath('//div[text()="A50001"]').click()
        driver.find_element_by_xpath('//span[text()="确 定"]').click()
        driver.find_element_by_xpath('//*[text()="发票类型"]/../..//div[@class="ant-select-selection__rendered"]').click()
        driver.find_element_by_xpath('//li[text()="增值税专用发票"]').click()

        # 切换到表体
        driver.find_element_by_xpath('//*[@id="st_purinvoice|btnMax_st_purinvoice_body_page"]/i').click()

        # 拖动底部滚动条
        actions = ActionChains(driver)
        ele1 = driver.find_element_by_xpath('//*[@id="st_purinvoice|st_purinvoice_body_page_base"]/div/div/div[1]/div[2]/div[2]/div/div/div')
        actions.move_to_element(ele1)
        actions.drag_and_drop_by_offset(ele1, 628, 1)
        actions.perform()

        driver.find_element_by_xpath('//*[@id="st_purinvoice|st_purinvoice_body_page_base"]//div[3]//div[7]//div[@class="textCol"]').click()
        driver.find_element_by_xpath('//*[@id="st_purinvoice|st_purinvoice_body_page_base"]//div[3]//div[7]//div[@class="editCol"]//input').send_keys("1000")
        # 切换到单据
        driver.find_element_by_xpath('//*[@id="st_purinvoice|btnMax_st_purinvoice_body_page"]/i').click()

        # 保存
        # 用JS点击
        search_button1 = driver.find_element_by_xpath('//span[text()="保存"]')
        driver.execute_script("arguments[0].click();", search_button1)

        driver.find_element_by_xpath('//*[text()="返回"]').click()

        # # 第二个入库单
        # # 增加
        # driver.find_element_by_xpath('//*[text()="新 增"]/../..//i[@class="anticon anticon-down"]').click()
        # driver.find_element_by_xpath('//*[text()="空白单据"]').click()
		#
        # # 录入数据
        # driver.find_element_by_xpath('//*[text()="收货组织"]/../..//i[@class="anticon anticon-canzhao"]').click()
        # driver.find_element_by_xpath('//*[text()="bj_cczx"]').click()
        # driver.find_element_by_xpath('//span[text()="确 定"]').click()
		#
        # driver.find_element_by_xpath('//*[text()="采购组织"]/../..//i[@class="anticon anticon-canzhao"]').click()
        # driver.find_element_by_xpath('//*[@id="aa_orgpur"]//div[text()="yontest"]').click()
        # driver.find_element_by_xpath('//div[@class="ant-modal-mask"]/..//span[text()="确 定"]').click()
        # # driver.find_element_by_xpath('//label[text()="单据编号"]/../..//input').send_keys("sg002")
		#
        # driver.find_element_by_xpath('//*[text()="仓库"]/../..//i[@class="anticon anticon-canzhao"]').click()
        # driver.find_element_by_xpath('//*[@id="aa_warehouse"]//div[2]//div[1]/div[2]//div[3]/div[1]//div[1]//label/span/input').click()
        # driver.find_element_by_xpath('//div[@class="ant-modal-mask"]/..//span[text()="确 定"]').click()
		#
        # driver.find_element_by_xpath('//*[text()="供应商"]/../..//i[@class="anticon anticon-canzhao"]').click()
        # driver.find_element_by_xpath('//*[@id="productcenter.aa_vendor"]//div[2]//div[1]/div[2]/div[1]/div[3]//div[1]/div[1]//label/span/input').click()
        # driver.find_element_by_xpath('//div[@class="ant-modal-mask"]/..//span[text()="确 定"]').click()
		#
        # driver.find_element_by_xpath('//*[text()="币种名称"]/../..//i[@class="anticon anticon-canzhao"]').click()
        # driver.find_element_by_xpath('//div[text()="美元"]').click()
        # driver.find_element_by_xpath('//div[@class="ant-modal-mask"]/..//span[text()="确 定"]').click()
		#
		#
        # # 切换到表体
        # driver.find_element_by_xpath('//*[@id="st_purinrecord|btnMax_st_purinrecord_body_page"]/i').click()
        # sleep(5)
        # driver.find_element_by_xpath('//*[@id="st_purinrecord|st_purinrecord_body_page_base"]//div[3]//div[2]/div/div[1]//div[@class="textCol"]').click()
        # driver.find_element_by_xpath('//*[@id="st_purinrecord|st_purinrecord_body_page_base"]//div[3]//div[2]//div[1]//div/i[@class="anticon anticon-canzhao"]').click()
        # driver.find_element_by_xpath('// *[text() = "物料名称02"]').click()
        # driver.find_element_by_xpath('//div[@class="ant-modal-mask"]/..//span[text()="确 定"]').click()
		#
        # driver.find_element_by_xpath('//*[@id="st_purinrecord|st_purinrecord_body_page_base"]//div[3]//div[5]//div[@class="textCol"]').click()
        # driver.find_element_by_xpath('//*[@id="st_purinrecord|st_purinrecord_body_page_base"]//div[3]//div[5]//div[@class="editCol"]//input').send_keys('1001')
		#
        # # 切换到表体
        # driver.find_element_by_xpath('//*[@id="st_purinrecord|btnMax_st_purinrecord_body_page"]/i').click()
		#
        # # 保存
        # search_button1 = driver.find_element_by_xpath('//span[text()="保存"]')
        # driver.execute_script("arguments[0].click();", search_button1)
		#
        # # 鼠标悬浮
        # article = driver.find_element_by_xpath('//*[text()="sg002"]')
        # ActionChains(driver).move_to_element(article).perform()
        # # 编辑
        # driver.find_element_by_xpath('//*[@class="table-list-btn"and text()="编辑"]').click()
        # driver.find_element_by_xpath('//*[text()="税率"]/../..//i[@class="anticon anticon-canzhao"]').click()
        # driver.find_element_by_xpath('//div[text()="免税"]').click()
        # driver.find_element_by_xpath('//div[@class="ant-modal-mask"]/..//span[text()="确 定"]').click()
        # # 保存
        # driver.find_element_by_xpath('//span[text()="保存"]').click()
		#
        # driver.find_element_by_xpath('//div[text()="单据编号"]/..//input').send_keys("sg002")
        # driver.find_element_by_xpath('//span[text()="搜 索"]').click()
        # driver.find_element_by_xpath('//a[text()="sg002"]/ancestor::div[@class="fixedDataTableRowLayout_rowWrapper"]//input').click()
        # driver.find_element_by_xpath('//span[text()="删除"]').click()
        # driver.find_element_by_xpath('//span[text()="确 定"]').click()
		#
        # #增加第三个
        # # 增加
        # driver.find_element_by_xpath('//span[text()="新 增"]').click()
        # # 录入数据
        # driver.find_element_by_xpath('//*[text()="收货组织"]/../..//i[@class="anticon anticon-canzhao"]').click()
        # driver.find_element_by_xpath('//*[text()="bj_cczx"]').click()
        # driver.find_element_by_xpath('//span[text()="确 定"]').click()
		#
        # driver.find_element_by_xpath('//*[text()="采购组织"]/../..//i[@class="anticon anticon-canzhao"]').click()
        # driver.find_element_by_xpath('//*[@id="aa_orgpur"]//div[text()="yontest"]').click()
        # driver.find_element_by_xpath('//div[@class="ant-modal-mask"]/..//span[text()="确 定"]').click()
        # driver.find_element_by_xpath('//label[text()="单据编号"]/../..//input').send_keys("sg003")
		#
        # driver.find_element_by_xpath('//*[text()="仓库"]/../..//i[@class="anticon anticon-canzhao"]').click()
        # driver.find_element_by_xpath('//*[text()="02"]').click()
        # driver.find_element_by_xpath('//div[@class="ant-modal-mask"]/..//span[text()="确 定"]').click()
		#
        # driver.find_element_by_xpath('//*[text()="供应商"]/../..//i[@class="anticon anticon-canzhao"]').click()
        # driver.find_element_by_xpath('//*[text()="l0010001"]').click()
        # driver.find_element_by_xpath('//div[@class="ant-modal-mask"]/..//span[text()="确 定"]').click()
		#
        # driver.find_element_by_xpath('//*[text()="币种名称"]/../..//i[@class="anticon anticon-canzhao"]').click()
        # driver.find_element_by_xpath('//div[text()="人民币"]').click()
        # driver.find_element_by_xpath('//div[@class="ant-modal-mask"]/..//span[text()="确 定"]').click()
		#
        # # 切换到表体
        # driver.find_element_by_xpath('//*[@id="st_purinrecord|btnMax_st_purinrecord_body_page"]/i').click()
		#
        # sleep(5)
        # driver.find_element_by_xpath('//*[@id="st_purinrecord|st_purinrecord_body_page_base"]//div[3]//div[2]/div/div[1]//div[@class="textCol"]').click()
        # driver.find_element_by_xpath('//*[@id="st_purinrecord|st_purinrecord_body_page_base"]//div[3]//div[2]//div[1]//div/i[@class="anticon anticon-canzhao"]').click()
        # driver.find_element_by_xpath('//*[text()="物料名称02"]').click()
        # driver.find_element_by_xpath('//div[@class="ant-modal-mask"]/..//span[text()="确 定"]').click()
		#
        # driver.find_element_by_xpath('//*[@id="st_purinrecord|st_purinrecord_body_page_base"]//div[3]//div[5]//div[@class="textCol"]').click()
        # driver.find_element_by_xpath('//*[@id="st_purinrecord|st_purinrecord_body_page_base"]//div[3]//div[5]//div[@class="editCol"]//input').send_keys('1001')
		#
        # # 切换到表体
        # driver.find_element_by_xpath('//*[@id="st_purinrecord|btnMax_st_purinrecord_body_page"]/i').click()
		#
        # # 保存
        # search_button1 = driver.find_element_by_xpath('//span[text()="保存"]')
        # driver.execute_script("arguments[0].click();", search_button1)
		#
        # # 第四个入库单
        # # 增加
        # driver.find_element_by_xpath('//*[text()="新 增"]/../..//i[@class="anticon anticon-down"]').click()
        # driver.find_element_by_xpath('//*[text()="空白单据"]').click()
		#
        # # 录入数据
        # driver.find_element_by_xpath('//*[text()="收货组织"]/../..//i[@class="anticon anticon-canzhao"]').click()
        # driver.find_element_by_xpath('//*[text()="bj_cczx"]').click()
        # driver.find_element_by_xpath('//span[text()="确 定"]').click()
		#
        # driver.find_element_by_xpath('//*[text()="采购组织"]/../..//i[@class="anticon anticon-canzhao"]').click()
        # driver.find_element_by_xpath('//*[@id="aa_orgpur"]//div[text()="yontest"]').click()
        # driver.find_element_by_xpath('//div[@class="ant-modal-mask"]/..//span[text()="确 定"]').click()
        # driver.find_element_by_xpath('//label[text()="单据编号"]/../..//input').send_keys("sg004")
		#
        # driver.find_element_by_xpath('//*[text()="仓库"]/../..//i[@class="anticon anticon-canzhao"]').click()
        # driver.find_element_by_xpath('//*[text()="03"]').click()
        # driver.find_element_by_xpath('//div[@class="ant-modal-mask"]/..//span[text()="确 定"]').click()
		#
        # driver.find_element_by_xpath('//*[text()="供应商"]/../..//i[@class="anticon anticon-canzhao"]').click()
        # driver.find_element_by_xpath('//*[text()="l0010001"]').click()
        # driver.find_element_by_xpath('//div[@class="ant-modal-mask"]/..//span[text()="确 定"]').click()
		#
        # driver.find_element_by_xpath('//*[text()="币种名称"]/../..//i[@class="anticon anticon-canzhao"]').click()
        # driver.find_element_by_xpath('//div[text()="美元"]').click()
        # driver.find_element_by_xpath('//div[@class="ant-modal-mask"]/..//span[text()="确 定"]').click()
		#
        # # 切换到表体
        # driver.find_element_by_xpath('//*[@id="st_purinrecord|btnMax_st_purinrecord_body_page"]/i').click()
        # sleep(5)
        # driver.find_element_by_xpath('//*[@id="st_purinrecord|st_purinrecord_body_page_base"]//div[3]//div[2]/div/div[1]//div[@class="textCol"]').click()
        # driver.find_element_by_xpath('//*[@id="st_purinrecord|st_purinrecord_body_page_base"]//div[3]//div[2]//div[1]//div/i[@class="anticon anticon-canzhao"]').click()
        # driver.find_element_by_xpath('// *[text() = "物料名称02"]').click()
        # driver.find_element_by_xpath('//div[@class="ant-modal-mask"]/..//span[text()="确 定"]').click()
		#
        # driver.find_element_by_xpath('//*[@id="st_purinrecord|st_purinrecord_body_page_base"]//div[3]//div[5]//div[@class="textCol"]').click()
        # driver.find_element_by_xpath('//*[@id="st_purinrecord|st_purinrecord_body_page_base"]//div[3]//div[5]//div[@class="editCol"]//input').send_keys('1001')
		#
        # # 切换到表体
        # driver.find_element_by_xpath('//*[@id="st_purinrecord|btnMax_st_purinrecord_body_page"]/i').click()
		#
        # # 保存
        # search_button1 = driver.find_element_by_xpath('//span[text()="保存"]')
        # driver.execute_script("arguments[0].click();", search_button1)

        # 返回主窗体
        driver.switch_to.default_content()

        # 关闭页签
        driver.find_element_by_css_selector('button[class="u-button"]').click()
        driver.find_element_by_css_selector('li[title="关闭全部页签"]').click()








