from selenium.webdriver import ActionChains
import time
import math
from selenium.webdriver.common.keys import Keys

def get_successful_toast(driver):
    return driver.find_element_by_css_selector('div.uretail-notification > span > div > div > div > div.anticon-circle','findAssert').text


def search_organize_deparment(driver,term):
    driver.find_element_by_css_selector('input.ant-select-search__field').clear()
    driver.find_element_by_css_selector('input.ant-select-search__field').send_keys(term)
    driver.find_element_by_css_selector('ul.ant-select-dropdown-menu.ant-select-dropdown-menu-vertical.ant-select-dropdown-menu-root>li:nth-child(1)','findAssert').click()

def get_head(driver):
    return driver.find_element_by_css_selector('div.form-base > div:nth-child(2) > div > div > h1','findAssert').text


# 门店等级、门店职位保存按钮
def save_button_level(driver):
    driver.find_element_by_css_selector(
        'div.ant-row-flex.ant-row-flex-start.btn-toolbar-bottom.btn-group-bottom > div > button:nth-child(1)').click()
    return get_successful_toast(driver)

############仓库、门店档案查询条件-编码、名称、新增、搜索、查询条件更多

# 选择区域
def choose_area(driver):
    # 选择中国
    driver.find_element_by_css_selector(
        'div.ant-cascader-menus.ant-cascader-menus-placement-bottomLeft>div>ul:nth-child(1) > li').click()
    # 选择北京
    driver.find_element_by_css_selector(
        'div.ant-cascader-menus.ant-cascader-menus-placement-bottomLeft>div>ul:nth-child(2) > li').click()
    # 选择北京市
    driver.find_element_by_css_selector(
        'div.ant-cascader-menus.ant-cascader-menus-placement-bottomLeft>div>ul:nth-child(3) > li').click()
    # 选择东城
    driver.find_element_by_css_selector(
        'div.ant-cascader-menus.ant-cascader-menus-placement-bottomLeft>div>ul:nth-child(4) > li').click()


# 显示编辑、删除、停用按钮
def show_oper_button(driver):
    chain = ActionChains(driver)
    implement = driver.find_element_by_css_selector(
        "div.fixedDataTableLayout_rowsContainer > div:nth-child(3) > div:nth-child(1)")  # 鼠标悬浮到第一行
    time.sleep(2)
    chain.move_to_element(implement).perform()

# 显示编辑、删除、停用按钮
def show_oper_button_fenye(driver,index):
    page=math.ceil(float(index)/15)
    row=int(index-(page-1)*15)
    driver.find_element_by_css_selector('div.ant-pagination-options>div:nth-child(2)>input').send_keys(page)
    driver.find_element_by_css_selector('div.ant-pagination-options>div:nth-child(2)>input').send_keys(Keys.ENTER)
    chain = ActionChains(driver)
    implement = driver.find_element_by_css_selector(
        "div.fixedDataTableLayout_rowsContainer > div:nth-child(3) > div:nth-child("+str(row)+")")  # 鼠标悬浮到第一行
    time.sleep(2)
    chain.move_to_element(implement).perform()

def click_oper_button(driver, tag):
    if tag == 'edit':
        driver.find_element_by_css_selector(
            'div.meta-table.listTable > div:nth-child(1) > div.acticonCell > div > span:nth-child(1) > a').click()
    if tag == 'del':
        driver.find_element_by_css_selector(
            'div.meta-table.listTable > div:nth-child(1) > div.acticonCell > div > span:nth-child(2) > a').click()
    if tag == 'ty':
        driver.find_element_by_css_selector(
            'div.meta-table.listTable > div:nth-child(1) > div.acticonCell > div > span:nth-child(3) > a').click()

# 确定
def ok_button(driver):
    driver.find_element_by_css_selector('button.ant-btn.ant-btn-primary.ant-btn-lg').click()


# 查询条件编码名称
def query_cname(driver, cname):
    driver.find_element_by_css_selector(
        'div.ant-row.listheadRow > div:nth-child(1) > div > div > div:nth-child(1) > div > div > div:nth-child(1) > div > div > div.input-control > div > span > input').clear()
    driver.find_element_by_css_selector(
        'div.ant-row.listheadRow > div:nth-child(1) > div > div > div:nth-child(1) > div > div > div:nth-child(1) > div > div > div.input-control > div > span > input').clear()
    driver.find_element_by_css_selector(
        'div.ant-row.listheadRow > div:nth-child(1) > div > div > div:nth-child(1) > div > div > div:nth-child(1) > div > div > div.input-control > div > span > input').send_keys(
        cname)


# 查询条件更多
def query_more(driver):
    driver.find_element_by_css_selector('button.ant-btn.showMore.ant-btn-ghost.ant-btn-sm').click()


# 查询按钮
def query_button(driver):
    driver.find_element_by_css_selector('button.ant-btn.up-search.ant-btn-ghost').click()

######周边门店、门店经营范围选择门店、仓库、品牌
def choose_around_store(driver):
    # 选择第一个门店
    time.sleep(2)
    driver.find_element_by_css_selector(
        'div.ant-modal-body > div > div > div:nth-child(2) > div > div:nth-child(1) > div.fixedDataTableLayout_main.public_fixedDataTable_main > div > div:nth-child(3) > div:nth-child(1) > div > div > div:nth-child(1) > div > div > div > div > div > div > div > label > span > input').click()
    time.sleep(2)
    driver.find_element_by_css_selector(
        'div.ant-modal-content > div.ant-modal-footer > button.ant-btn.ant-btn-primary.ant-btn-lg').click()


# 界面弹出多个相同的窗口的情况
def choose_warehouse(driver, index,xuhao=1):
    time.sleep(2)
    # 选择第一个范围
    driver.find_elements_by_css_selector(
        'div.ant-modal-body > div > div > div:nth-child(2) > div > div:nth-child(1) > div.fixedDataTableLayout_main.public_fixedDataTable_main > div > div:nth-child(3) > div:nth-child('+str(xuhao)+') > div > div > div:nth-child(1) > div > div > div > div > div > div > div > label > span > input').pop(
        index - 1).click()
    time.sleep(2)
    driver.find_elements_by_css_selector(
        'div.ant-modal-content > div.ant-modal-footer > button.ant-btn.ant-btn-primary.ant-btn-lg').pop(
        index - 1).click()

# 切换页签
def switch_tab(driver, tag):
    driver.find_element_by_css_selector('div.ant-row.line-tabs > div.ant-row > ul > li:nth-child('+str(tag)+')').click()


# 获取列表字段值
def get_value(driver, ids):
    element = driver.find_elements_by_css_selector(
        'div.meta-table.listTable>div:nth-child(1)>div:nth-child(3)>div:nth-child(1)>div:nth-child(2)>div>div:nth-child(1)>div:nth-child(2)>div>div>div:nth-child(2)>div>div>div>div')
    for ele in element:
        if ele.get_attribute("id") == ids:
            col = element.index(ele)
            return driver.find_element_by_css_selector(
                'div.meta-table.listTable > div:nth-child(1) > div:nth-child(3)> div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div > div > div:nth-child(2) > div > div:nth-child(' + str(
                    col+1) + ') > div > div > div > div > div').get_attribute("title")
