# coding=utf-8
from SRC.param.yls_navigation_base import jigoudangan_navigation
from SRC.param.yls_base import get_successful_toast,choose_around_store
import time

######################################角色##########################################
# 进入角色界面
def log_role(driver):
    jigoudangan_navigation(driver ,'i.iconfont.icon-jichushezhi')
    # 点击角色
    driver.find_element_by_css_selector(
        'ul.ant-menu.ant-menu-vertical.ant-menu-light.ant-menu-root>li:nth-child(9)>ul>li:nth-child(1)>ul>li:nth-child(2)').click()

def add_role_button(driver):
    # 点击新增按钮
    driver.find_element_by_id('sys_rolelist|btnAdd').click()


# 角色信息
def role_info(driver ,code ,name):
    # 角色编码
    driver.find_element_by_css_selector('div.roleBody > div:nth-child(1) > div.col-float.width-400 > input').clear()
    driver.find_element_by_css_selector('div.roleBody > div:nth-child(1) > div.col-float.width-400 > input').send_keys \
        (code)
    # 角色名称
    driver.find_element_by_css_selector('div.roleBody > div:nth-child(2) > div.col-float.width-400 > input').clear()
    driver.find_element_by_css_selector('div.roleBody > div:nth-child(2) > div.col-float.width-400 > input').send_keys \
        (name)

def save_role_button(driver,save_btn):
    driver.find_element_by_css_selector(save_btn).click()
    return get_successful_toast(driver)

#添加功能权限
def add_functional_permissions(driver,first,second,third=0):
    target = driver.find_element_by_css_selector('div.ant-row.roleRow.function-limit > div > div:nth-child('+str(first+1)+')> div:nth-child(2) > div:nth-child('+str(second)+')> div.second-auth > label > span.ant-checkbox > input')
    driver.execute_script("arguments[0].scrollIntoView();", target)
    if third==0:
        driver.find_element_by_css_selector('div.ant-row.roleRow.function-limit > div > div:nth-child('+str(first+1)+')> div:nth-child(2) > div:nth-child('+str(second)+')> div.second-auth > label > span.ant-checkbox > input').click()

    else:
        driver.find_element_by_css_selector('div.ant-row.roleRow.function-limit > div > div:nth-child('+str(first+1)+')> div:nth-child(2) > div:nth-child('+str(second)+')> div.last-auth > label:nth-child('+str(third)+') > span.ant-checkbox > input').click()

#切换权限页签
def switch_function_xczk(driver,tab):
    driver.find_element_by_css_selector('div.ant-row.roleRow.function-limit > div > div.role-tabs.clearfix > div.tabs-control > div:nth-child('+str(tab)+')').click()


#添加现场折扣权限
def add_xczk(driver,flname,hyzk,zkl):
    #点击新增行
    driver.find_element_by_css_selector('div.ant-row.roleRow.function-limit > div > div.role-tabs.clearfix > div.tabs-button > button > span').click()
    #获取行号
    xh=driver.find_element_by_css_selector('div.ant-row.roleRow.function-limit > div > div.meta-table.listTable > div:nth-child(1) > div > div > div:nth-child(3) > div:last-child > div > div > div:nth-child(1) > div > div > div > div > div > div').text
    driver.find_element_by_css_selector('div.ant-row.roleRow.function-limit > div > div.meta-table.listTable > div:nth-child(1) > div > div > div:nth-child(3) > div:nth-child('+xh+') > div > div > div:nth-child(2) > div > div:nth-child(1) > div > div > div > div > div').click()
    driver.find_element_by_css_selector('div.ant-row.roleRow.function-limit > div > div.meta-table.listTable > div:nth-child(1) > div > div > div:nth-child(3) > div:nth-child('+xh+') > div > div > div:nth-child(2) > div > div:nth-child(1) > div > div > div > div > div > div > span > span > span.ant-select-arrow').click()
    element=driver.find_elements_by_css_selector('div.ant-popover-inner > div > div > div > ul > li> span:nth-child(3)')
    for ele in element:
        if element.index(ele)%8==0:
            target = driver.find_element_by_css_selector("div.ant-popover-inner > div > div > div > ul > li:nth-child("+str(element.index(ele)+1)+")> span.ant-tree-checkbox > span")
            driver.execute_script("arguments[0].scrollIntoView();", target)
        if ele.get_attribute("title")==flname:
            driver.find_element_by_css_selector('div.ant-popover-inner > div > div > div > ul > li:nth-child('+str(element.index(ele)+1)+') > span.ant-tree-checkbox > span').click()
            break
    #点击确定
    driver.find_element_by_css_selector('button.ant-btn.ant-btn.ant-btn-primary.ant-btn-sm.lf-margin').click()
    #已执行会员折扣
    driver.find_element_by_css_selector('div.ant-row.roleRow.function-limit > div > div.meta-table.listTable > div:nth-child(1) > div > div > div:nth-child(3) > div:nth-child('+xh+') > div > div > div:nth-child(2) > div > div:nth-child(2) > div > div > div > div > div').click()
    driver.find_element_by_css_selector('div.ant-row.roleRow.function-limit > div > div.meta-table.listTable > div:nth-child(1) > div > div > div:nth-child(3) > div:nth-child('+xh+') > div > div > div:nth-child(2) > div > div:nth-child(2) > div > div > div > div > div > div > div.ant-select.ant-select-enabled > div > span').click()
    for i in range(0,2):
        if driver.find_element_by_css_selector('ul.ant-select-dropdown-menu.ant-select-dropdown-menu-vertical.ant-select-dropdown-menu-root>li:nth-child('+str(i+1)+')').text==hyzk:
            driver.find_element_by_css_selector('ul.ant-select-dropdown-menu.ant-select-dropdown-menu-vertical.ant-select-dropdown-menu-root>li:nth-child('+str(i+1)+')').click()
    #折扣率下限
    driver.find_element_by_css_selector('div.ant-row.roleRow.function-limit > div > div.meta-table.listTable > div:nth-child(1) > div > div > div:nth-child(3) > div:nth-child('+xh+') > div > div > div:nth-child(2) > div > div:nth-child(3) > div > div > div > div > div').click()
    #driver.find_element_by_css_selector('div.ant-row.roleRow.function-limit > div > div.meta-table.listTable > div:nth-child(1) > div > div > div:nth-child(3) > div:nth-child(' + xh + ') > div > div > div:nth-child(2) > div > div:nth-child(3) > div > div > div > div > div > div > div.ant-input-number > div.ant-input-number-input-wrap > input').clear()
    driver.find_element_by_css_selector('div.ant-row.roleRow.function-limit > div > div.meta-table.listTable > div:nth-child(1) > div > div > div:nth-child(3) > div:nth-child('+xh+') > div > div > div:nth-child(2) > div > div:nth-child(3) > div > div > div > div > div > div > div.ant-input-number > div.ant-input-number-input-wrap > input').send_keys(zkl)


#####################################操作员##########################################

# 进入操作员界面
def log_operator(driver):
    jigoudangan_navigation(driver, 'i.iconfont.icon-jichushezhi')
    # 点击操作员
    driver.find_element_by_css_selector(
        'ul.ant-menu.ant-menu-vertical.ant-menu-light.ant-menu-root>li:nth-child(9)>ul>li:nth-child(1)>ul>li:nth-child(1)').click()


def add_oper_button(driver):
    # 点击新增按钮
    driver.find_element_by_id('aa_userlist|btnAdd').click()


# 操作员信息
def operator_info(driver, zh, name, mail, tel):
    count = len(driver.find_elements_by_css_selector(
        'div.uretail-right-content.ant-layout-content>div>div>div:nth-child(2)>div:nth-child(2)>div>div:nth-child(2)>div:nth-child(2)>div>div>div.ant-row'))
    if count == 2:
        element = driver.find_elements_by_css_selector('div.ant-row.group-container>div>div>div:nth-child(2)>div>div')
        for ele in element:
            if ele.get_attribute("id") == 'aa_user|code':
                user_code(driver, zh)
            if ele.get_attribute("id") == 'aa_user|name':
                user_name(driver, name)
            if ele.get_attribute("id") == 'aa_user|email':
                user_email(driver, mail)
            if ele.get_attribute("id") == 'aa_user|mobile':
                user_mobile(driver, tel)


# 账号
def user_code(driver, zh):
    driver.find_element_by_css_selector(
        'div[id="aa_user|code"] > div > div.ant-row > div.col-float.input-control.control-width > span > input').clear()
    driver.find_element_by_css_selector(
        'div[id="aa_user|code"] > div > div.ant-row > div.col-float.input-control.control-width > span > input').clear()
    driver.find_element_by_css_selector(
        'div[id="aa_user|code"] > div > div.ant-row > div.col-float.input-control.control-width > span > input').send_keys(
        zh)


# 姓名
def user_name(driver, name):
    driver.find_element_by_css_selector(
        'div[id="aa_user|name"] > div > div.ant-row > div.col-float.input-control.control-width > span > input').clear()
    driver.find_element_by_css_selector(
        'div[id="aa_user|name"] > div > div.ant-row > div.col-float.input-control.control-width > span > input').clear()
    driver.find_element_by_css_selector(
        'div[id="aa_user|name"] > div > div.ant-row > div.col-float.input-control.control-width > span > input').send_keys(
        name)


# 邮箱
def user_email(driver, mail):
    driver.find_element_by_css_selector(
        'div[id="aa_user|email"] > div > div.ant-row > div.col-float.input-control.control-width > span > input').clear()
    driver.find_element_by_css_selector(
        'div[id="aa_user|email"] > div > div.ant-row > div.col-float.input-control.control-width > span > input').send_keys(
        mail)


# 手机号
def user_mobile(driver, tel):
    driver.find_element_by_css_selector(
        'div[id="aa_user|mobile"] > div > div.ant-row > div.col-float.input-control.control-width > span > input').clear()
    driver.find_element_by_css_selector(
        'div[id="aa_user|mobile"] > div > div.ant-row > div.col-float.input-control.control-width > span > input').clear()
    driver.find_element_by_css_selector(
        'div[id="aa_user|mobile"] > div > div.ant-row > div.col-float.input-control.control-width > span > input').send_keys(
        tel)


# 增行按钮
def add_oper_role_button(driver):
    driver.find_element_by_id('aa_user|btnAddRow_role').click()


def add_organ_button(driver):
    driver.find_element_by_id('aa_user|btnAddRow_org').click()


def add_store_role_button(driver):
    driver.find_element_by_id('aa_user|btnAddRow_store').click()


# 添加角色
def add_role(driver):
    element = driver.find_elements_by_css_selector(
        'div[id="aa_user|aa_usertabrole"]>div>div.meta-table.listTable>div:nth-child(1)>div:nth-child(2)>div>div:nth-child(2)>div>div>div:nth-child(2)>div>div>div:nth-child(2)>div>div>div>div')
    for ele in element:
        if ele.get_attribute("id") == 'aa_user|aa_userrole|role_name':
            col = element.index(ele)
            driver.find_element_by_css_selector(
                'div[id="aa_user|aa_usertabrole"]>div>div>div:nth-child(1)>div:nth-child(2)>div>div:nth-child(3)>div>div>div>div:nth-child(2)>div>div:nth-child(' + str(
                    col + 1) + ')>div>div>div>div>div').click()
            driver.find_element_by_css_selector(
                'div[id="aa_user|aa_usertabrole"]>div>div>div:nth-child(1)>div:nth-child(2)>div>div:nth-child(3)>div>div>div>div:nth-child(2)>div>div:nth-child(' + str(
                    col + 1) + ')>div>div>div>div>div>div>div:nth-child(1)>div>div>span>span>div>i.anticon.anticon-canzhao').click()
            choose_around_store(driver)

def add_role1(driver,role_name):
    element = driver.find_elements_by_css_selector(
        'div[id="aa_user|aa_usertabrole"]>div>div.meta-table.listTable>div:nth-child(1)>div:nth-child(2)>div>div:nth-child(2)>div>div>div:nth-child(2)>div>div>div:nth-child(2)>div>div>div>div')
    for ele in element:
        if ele.get_attribute("id") == 'aa_user|aa_userrole|role_name':
            col = element.index(ele)
            driver.find_element_by_css_selector(
                'div[id="aa_user|aa_usertabrole"]>div>div>div:nth-child(1)>div:nth-child(2)>div>div:nth-child(3)>div>div>div>div:nth-child(2)>div>div:nth-child(' + str(
                    col + 1) + ')>div>div>div>div>div').click()
            driver.find_element_by_css_selector(
                'div[id="aa_user|aa_usertabrole"]>div>div>div:nth-child(1)>div:nth-child(2)>div>div:nth-child(3)>div>div>div>div:nth-child(2)>div>div:nth-child(' + str(
                    col + 1) + ')>div>div>div>div>div>div>div:nth-child(1)>div>div>span>span>div>i.anticon.anticon-canzhao').click()
            choose_role(driver,role_name)

def choose_role(driver,role_name):
    #搜索角色
    driver.find_element_by_css_selector('div.ant-modal-body > div > div > div:nth-child(1) > div > div:nth-child(1) > span > input').clear()
    driver.find_element_by_css_selector('div.ant-modal-body > div > div > div:nth-child(1) > div > div:nth-child(1) > span > input').send_keys(role_name)
    driver.find_element_by_css_selector('div.ant-modal-body > div > div > div:nth-child(1) > div > div:nth-child(1) > span > span > i').click()
    # 选择第一个门店
    time.sleep(2)
    driver.find_element_by_css_selector(
        'div.ant-modal-body > div > div > div:nth-child(2) > div > div:nth-child(1) > div.fixedDataTableLayout_main.public_fixedDataTable_main > div > div:nth-child(3) > div:nth-child(1) > div > div > div:nth-child(1) > div > div > div > div > div > div > div > label > span > input').click()
    time.sleep(2)
    driver.find_element_by_css_selector(
        'div.ant-modal-content > div.ant-modal-footer > button.ant-btn.ant-btn-primary.ant-btn-lg').click()


# 添加门店权限
def add_store_role(driver):
    element = driver.find_elements_by_css_selector(
        'div[id="aa_user|aa_user_tab_store"]>div>div.meta-table.listTable>div:nth-child(1)>div:nth-child(2)>div>div:nth-child(2)>div>div>div:nth-child(2)>div>div>div:nth-child(2)>div>div>div>div')
    for ele in element:
        if ele.get_attribute("id") == 'aa_user|aa_userstore|store_name':
            col = element.index(ele)
            driver.find_element_by_css_selector(
                'div[id="aa_user|aa_user_tab_store"]>div>div>div:nth-child(1)>div:nth-child(2)>div>div:nth-child(3)>div>div>div>div:nth-child(2)>div>div:nth-child(' + str(
                    col + 1) + ')>div>div>div>div>div').click()
            driver.find_element_by_css_selector(
                'div[id="aa_user|aa_user_tab_store"]>div>div>div:nth-child(1)>div:nth-child(2)>div>div:nth-child(3)>div>div>div>div:nth-child(2)>div>div:nth-child(' + str(
                    col + 1) + ')>div>div>div>div>div>div>div:nth-child(1)>div>div>span>span>div>i.anticon.anticon-canzhao').click()
            choose_around_store(driver)


def save_operation_button(driver):
    # 点击保存按钮
    driver.find_element_by_id('aa_user|btnSave').click()
    return get_successful_toast(driver)