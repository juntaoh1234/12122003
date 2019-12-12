from selenium.webdriver import ActionChains
from time import sleep

from selenium.webdriver.common.keys import Keys

from SRC.param.yls_navigation_base import jigoudangan_navigation

def login_bill(driver):
    jigoudangan_navigation(driver ,'i.iconfont.icon-lingshouguanli')
    # 点击开单
    driver.find_element_by_css_selector('ul.ant-menu.ant-menu-vertical.ant-menu-sub>li:nth-child(1)>ul>li:nth-child(1)').click()
    driver.switch_to.window(driver.window_handles[1])
    sleep(3)

#在商品条码框输入商品名称并按回车
def bar_code_input(driver,name):
    driver.find_element_by_css_selector('div.ant-row.billing-member-goods > div.ant-col-12.billing-goods > div > div > span > input').send_keys(name)
    driver.find_element_by_css_selector('div.ant-row.billing-member-goods > div.ant-col-12.billing-goods > div > div > span > input').send_keys(Keys.ENTER)

#商品条码框(搜索商品添加记录)
def add_goods(driver,name):
    driver.find_element_by_css_selector('div.ant-col-12.billing-goods > div > div > span > span > i').click()
    element=driver.find_elements_by_css_selector('div.ant-tabs-bar > div > div > div > div > div.ant-tabs-tab')
    for ele in element:
        if driver.find_elements_by_css_selector('div.ant-tabs-bar > div > div > div > div > div.ant-tabs-tab')[element.index(ele)].text=='商品':
            driver.find_elements_by_css_selector('div.ant-tabs-bar > div > div > div > div > div.ant-tabs-tab').pop(element.index(ele)).click()
            break
    #输入搜索商品名称
    driver.find_element_by_css_selector('div.ant-modal-title> div > div > div:nth-child(2) > div > span > input').send_keys(name)
    driver.find_element_by_css_selector('div.ant-modal-title > div > div > div:nth-child(2) > div > span > span > i.anticon.anticon-search.ant-input-search-icon').click()
    #选择第一个商品
    driver.find_element_by_css_selector('table > tbody > tr:nth-child(1) > td.ant-table-selection-column > span > label > span > input').click()

#弹出框确定按钮
def dialog_ok_button(driver,index):
    sleep(3)
    #选择确定
    driver.find_elements_by_css_selector('button.ant-btn.ant-btn-primary.ant-btn-lg').pop(index-1).click()

#选择行记录
def choose_row(driver,tr):
    sleep(2)
    driver.find_element_by_css_selector(
        'div.ant-table-content>div>div.ant-table-body>table>tbody>tr:nth-child(' + str(tr) + ')').click()

#修改每行记录的营业员
def modify_shop_assistant(driver,tr,index):
    #选择行
    choose_row(driver,tr)
    #鼠标滑到...
    chain = ActionChains(driver)
    implement = driver.find_element_by_css_selector("button.ant-btn.isMoreButton")  # 鼠标悬浮到...按钮
    sleep(2)
    chain.move_to_element(implement).perform()
    #点击营业员
    driver.find_element_by_css_selector('div.billing-btn-popup>button:nth-child(5)').click()
    #选择营业员
    driver.find_element_by_css_selector('div.sales-check-list>div>div:nth-child('+str(index)+')>div.avatar>img').click()

#现场折扣
def xczk_button(driver):
    #点击现场折扣按钮
    driver.find_element_by_css_selector('#bottomButtonsId > div > button:nth-child(3)').click()

#当前行和整单进行切换
def switch_line_order(driver,tagname):
    element=driver.find_elements_by_css_selector('div.ant-tabs-bar > div > div > div > div > div.ant-tabs-tab')
    for ele in element:
        if driver.find_elements_by_css_selector('div.ant-tabs-bar > div > div > div > div > div.ant-tabs-tab')[element.index(ele)].text==tagname:
            driver.find_elements_by_css_selector('div.ant-tabs-bar > div > div > div > div > div.ant-tabs-tab').pop(element.index(ele)).click()
            break

#输入现场折扣折扣率
def input_xczk(driver,zkl):
    driver.find_element_by_css_selector('div[aria-hidden="false"]>div>div.col-float.left-discount>div>div:nth-child(2)>span.num>div>div:nth-child(2)>input').clear()
    driver.find_element_by_css_selector('div[aria-hidden="false"]>div>div.col-float.left-discount>div>div:nth-child(2)>span.num>div>div:nth-child(2)>input').clear()
    driver.find_element_by_css_selector('div[aria-hidden="false"]>div>div.col-float.left-discount>div>div:nth-child(2)>span.num>div>div:nth-child(2)>input').send_keys(zkl)

#取消所有折扣按钮
def qx_all_zk_button(driver):
    driver.find_element_by_css_selector('button.ant-btn.ant-btn-lg.cancelDiscount').click()

#取消所有折扣
def qx_all_zk(driver):
    xczk_button(driver)
    qx_all_zk_button(driver)

#现场折扣
def xczk(driver,tr,zkl,tagname):
    #选择折扣行
    choose_row(driver,tr)
    #点击现场折扣按钮
    xczk_button(driver)
    switch_line_order(driver,tagname)
    #输入折扣率
    input_xczk(driver,zkl)

#录入操作员
def choose_oper(driver,user,psw):
    #点击账号
    driver.find_element_by_css_selector('div.repair-body.ant-modal-margin>div:nth-child(1)>span:nth-child(2)>div>div').click()
    #选择操作员
    element=driver.find_elements_by_css_selector('ul.ant-select-dropdown-menu.ant-select-dropdown-menu-vertical.ant-select-dropdown-menu-root>li')
    for ele in element:
        if element.index(ele)%6==0:
            target = driver.find_element_by_css_selector('ul.ant-select-dropdown-menu.ant-select-dropdown-menu-vertical.ant-select-dropdown-menu-root>li:nth-child('+str(element.index(ele)+1)+')')
            driver.execute_script("arguments[0].scrollIntoView();", target)
        if driver.find_element_by_css_selector('ul.ant-select-dropdown-menu.ant-select-dropdown-menu-vertical.ant-select-dropdown-menu-root>li:nth-child('+str(element.index(ele)+1)+')').text==user:
            driver.find_element_by_css_selector('ul.ant-select-dropdown-menu.ant-select-dropdown-menu-vertical.ant-select-dropdown-menu-root>li:nth-child('+str(element.index(ele)+1)+')').click()
            break
    #输入密码
    driver.find_element_by_css_selector('div.repair-body.ant-modal-margin>div:nth-child(2)>span:nth-child(2)>input').send_keys(psw)


#选择规格
def choose_spec(driver,tr):
    sleep(3)
    #点击选择规格按钮
    driver.find_element_by_css_selector('#container > div > div.ant-layout.ant-layout-has-sider > div.ant-layout > div > div > div.ant-col-16 > div > div.ant-row.billing-cart > div > div > div > div > div > div > div.ant-table-fixed-left > div.ant-table-body-outer > div > table > tbody > tr:nth-child('+str(tr)+') > td > div > div.specs > button > span').click()
    #选择规格
    driver.find_element_by_css_selector('div.ant-table-wrapper.billing_chang_spec>div>div>div>div>div.ant-table-fixed-left>div.ant-table-body-outer>div>table>tbody>tr:nth-child(1)').click()

#输入会员手机号
def initial_member(driver,tel):
    driver.find_element_by_css_selector('div.ant-row.billing-member-goods > div.ant-col-12.billing-member > div > div > span > input').send_keys(tel)
    driver.find_element_by_css_selector('div.ant-row.billing-member-goods > div.ant-col-12.billing-member > div > div > span > span > div > i.anticon.anticon-search').click()

#结算按钮
def pay_button(driver,cha):
    #点击结算按钮
    driver.find_element_by_css_selector('button.ant-btn.ant-btn-pay').click()
    #获取界面应收金额
    num=driver.find_element_by_css_selector('div.pay-total>div>span:nth-child(2)').text
    #输入结算金额
    element=driver.find_elements_by_css_selector('div.pay-style-list>div.empty-scroll>div>div>span.payment-name-list')
    for ele in element:
        if driver.find_element_by_css_selector('div.pay-style-list>div.empty-scroll>div>div:nth-child('+str(element.index(ele)+1)+')>span.payment-name-list').text=='现金':
            driver.find_element_by_css_selector('div.pay-style-list>div.empty-scroll>div>div:nth-child('+str(element.index(ele)+1)+')>span:nth-child(4)>input').clear()
            driver.find_element_by_css_selector('div.pay-style-list>div.empty-scroll>div>div:nth-child('+str(element.index(ele)+1)+')>span:nth-child(4)>input').send_keys(str(float(num)+cha))
            break
    #点击结算
    driver.find_element_by_css_selector('button.ant-btn.checkout.ant-btn-primary').click()
    #获取找零金额
    zl=driver.find_element_by_css_selector('div.change-detail.clearfix>span:nth-child(2)','findAssert').text
    if zl=='':
        zl='0.00'
    return zl

#关闭开单界面
def close_bill(driver):
    driver.find_element_by_css_selector('i.anticon.anticon-guanbi').click()
    driver.switch_to.window(driver.window_handles[0])

#挂单
def guadan(driver):
    #鼠标滑到挂单
    chain = ActionChains(driver)
    implement = driver.find_element_by_css_selector("#menuguadan > div > span")  # 鼠标悬浮到挂单按钮
    sleep(2)
    chain.move_to_element(implement).perform()
    #点击仅挂单
    driver.find_element_by_css_selector('div.UretailBillPopoverguadan>div>div.ant-popover-inner>div>div>ul>li:nth-child(1)>span').click()

#解挂
def jiegua(driver):
    driver.find_element_by_css_selector('#menujiegua > div > span').click()
    #选择单据
    driver.find_element_by_css_selector('div.billing-cancelpending-list > div > div > div > div > div > div > table > tbody > tr:nth-child(1) > td.ant-table-selection-column > span > label > span > input').click()

#1补单
def gengduo(driver,tag):
    #鼠标滑到更多
    chain = ActionChains(driver)
    implement = driver.find_element_by_css_selector("#menugengduo > div > span")  # 鼠标悬浮到锁屏按钮
    sleep(2)
    chain.move_to_element(implement).perform()
    #点击
    driver.find_element_by_css_selector('div.UretailBillPopovergengduo>div>div.ant-popover-inner>div>div>ul>li:nth-child('+str(tag)+')>span').click()

#选择补单日期
def budan_date(driver):
    driver.find_element_by_css_selector('span.ant-calendar-picker-icon').click()
    #选择日期
    driver.find_element_by_css_selector('div.ant-calendar-date-panel > div.ant-calendar-body > table > tbody > tr:nth-child(1) > td:nth-child(1)').click()
    #点击确定
    driver.find_element_by_css_selector('a.ant-calendar-ok-btn').click()

#新开单
def new_open_bill(driver):
    driver.find_element_by_css_selector('#bottomButtonsId > div > button:nth-child(1)').click()

#添加会员按钮
def add_member_button(driver):
    a=driver.find_element_by_css_selector('div.addMember>svg>use')
    ActionChains(driver).click(a).perform()


#会员信息
def member_info(driver,name,tel):
    driver.find_element_by_id('realname').send_keys(name)
    driver.find_element_by_id('phone').send_keys(tel)
    driver.find_element_by_css_selector('div.member-btn.ant-modal-footer > button.ant-btn.ant-btn-primary').click()