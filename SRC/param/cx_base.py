import re

def zdyh_cx_weidu(driver,weidu):
    driver.find_element_by_css_selector('div.form-horizontal > div:nth-child(3) > div:nth-child(2) > select').click()
    if weidu=='无':
        driver.find_element_by_css_selector('div.form-horizontal > div:nth-child(3) > div:nth-child(2) > select>option:nth-child(1)').click()
    elif weidu == '客户':
        driver.find_element_by_css_selector(
            'div.form-horizontal > div:nth-child(3) > div:nth-child(2) > select>option[label="客户"]').click()
    elif weidu == '客户分类':
        driver.find_element_by_css_selector(
            'div.form-horizontal > div:nth-child(3) > div:nth-child(2) > select>option[label="客户分类"]').click()
    elif weidu == '客户级别':
        driver.find_element_by_css_selector(
            'div.form-horizontal > div:nth-child(3) > div:nth-child(2) > select>option[label="客户级别"]').click()
    elif weidu == '区域':
        driver.find_element_by_css_selector(
            'div.form-horizontal > div:nth-child(3) > div:nth-child(2) > select>option[label="区域"]').click()

def spcx_weidu(driver,weidu):
    driver.find_element_by_css_selector('form.form-horizontal> div:nth-child(3) > div:nth-child(2) > select').click()
    if weidu=='无':
        driver.find_element_by_css_selector('form.form-horizontal> div:nth-child(3) > div:nth-child(2) > select>option:nth-child(1)').click()
    elif weidu == '客户':
        driver.find_element_by_css_selector(
            'form.form-horizontal> div:nth-child(3) > div:nth-child(2) > select>option[label="客户"]').click()
    elif weidu == '客户分类':
        driver.find_element_by_css_selector(
            'form.form-horizontal > div:nth-child(3) > div:nth-child(2) > select>option[label="客户分类"]').click()
    elif weidu == '客户级别':
        driver.find_element_by_css_selector(
            'form.form-horizontal > div:nth-child(3) > div:nth-child(2) > select>option[label="客户级别"]').click()
    elif weidu == '区域':
        driver.find_element_by_css_selector(
            'form.form-horizontal > div:nth-child(3) > div:nth-child(2) > select>option[label="区域"]').click()

def zdyh_cx_name(driver,name):
    driver.find_element_by_css_selector('input[ng-model="pName"]').clear()
    driver.find_element_by_css_selector('input[ng-model="pName"]').send_keys(name)

def search_button(driver):
    driver.find_element_by_css_selector('button[ng-click="search()"]').click()

def qy_zdyh_fa(driver,name,tag):
    text=driver.find_element_by_css_selector('div.pagination.m-l-15.ng-binding').text
    str1 = text.split('，')
    str2 = ''.join(str1[:1])
    count=re.sub("\D", "", str2)
    temp_name=''
    for i in range(0,int(count)):
        count_tr=len(driver.find_elements_by_css_selector('table > tbody > tr'))
        for j in range(0,count_tr):
            temp_name=driver.find_element_by_css_selector('table > tbody > tr:nth-child('+str(j+1)+') > td:nth-child(2) > span').text
            if temp_name==name:
                if driver.find_element_by_css_selector('table > tbody > tr:nth-child('+str(j+1)+') > td:nth-child(7) > div > div').get_attribute('class')=='toggle-switch-animate switch-off' and tag=='qy':
                    driver.find_element_by_css_selector('table > tbody > tr:nth-child('+str(j+1)+') > td:nth-child(7) > div > div > span.switch-right.ng-binding').click()
                if driver.find_element_by_css_selector('table > tbody > tr:nth-child('+str(j+1)+') > td:nth-child(7) > div > div').get_attribute('class')=='toggle-switch-animate switch-on' and tag=='ty':
                    driver.find_element_by_css_selector('table > tbody > tr:nth-child('+str(j+1)+') > td:nth-child(7) > div > div > span.switch-right.ng-binding').click()
                break
        if temp_name==name:
            break
        if i>=0 and i<int(count) and int(count)>1:
            driver.find_element_by_css_selector('ul.pagination > li>a[ng-click="pager.selectNext()"]').click()

def qy_spcx_fa(driver,name,tag):
    text=driver.find_element_by_css_selector('div.pagination.m-l-15.ng-binding').text
    str1 = text.split('，')
    str2 = ''.join(str1[:1])
    count=re.sub("\D", "", str2)
    temp_name=''
    for i in range(0,int(count)):
        count_tr=len(driver.find_elements_by_css_selector('table > tbody > tr'))
        for j in range(0,count_tr):
            temp_name=driver.find_element_by_css_selector('table > tbody > tr:nth-child('+str(j+1)+') > td:nth-child(2) > span').text
            if temp_name==name:
                if driver.find_element_by_css_selector('table > tbody > tr:nth-child('+str(j+1)+') > td:nth-child(6) > div > div').get_attribute('class')=='toggle-switch-animate switch-off' and tag=='qy':
                    driver.find_element_by_css_selector('table > tbody > tr:nth-child('+str(j+1)+') > td:nth-child(6) > div > div > span.switch-right.ng-binding').click()
                if driver.find_element_by_css_selector('table > tbody > tr:nth-child('+str(j+1)+') > td:nth-child(6) > div > div').get_attribute('class')=='toggle-switch-animate switch-on' and tag=='ty':
                    driver.find_element_by_css_selector('table > tbody > tr:nth-child('+str(j+1)+') > td:nth-child(6) > div > div > span.switch-right.ng-binding').click()
                break
        if temp_name==name:
            break
        if i>=0 and i<int(count) and int(count)>1:
            driver.find_element_by_css_selector('ul.pagination > li>a[ng-click="pager.selectNext()"]').click()

#整单优惠状态
def zhyh_status(driver,status):
    if status=='全部':
        driver.find_element_by_css_selector('div.form-horizontal > div:nth-child(2) > div > div.orderList_form > a:nth-child(1)').click()
    elif status=='启用':
        driver.find_element_by_css_selector('div.form-horizontal > div:nth-child(2) > div > div.orderList_form > a:nth-child(2)').click()
    elif status=='禁用':
        driver.find_element_by_css_selector('div.form-horizontal > div:nth-child(2) > div > div.orderList_form > a:nth-child(3)').click()

#商品促销状态
def spcx_status(driver,status):
    if status=='全部':
        driver.find_element_by_css_selector('form.form-horizontal > div:nth-child(2) > div > div.orderList_form > a:nth-child(1)').click()
    elif status=='启用':
        driver.find_element_by_css_selector('form.form-horizontal > div:nth-child(2) > div > div.orderList_form > a:nth-child(2)').click()
    elif status=='禁用':
        driver.find_element_by_css_selector('form.form-horizontal > div:nth-child(2) > div > div.orderList_form > a:nth-child(3)').click()


#全部启用或者停用
def zdyh_qt_all(driver,tag):
    text=driver.find_element_by_css_selector('div.pagination.m-l-15.ng-binding').text
    str1 = text.split('，')
    str2 = ''.join(str1[:1])
    count=re.sub("\D", "", str2)
    for i in range(0,int(count)):
        count_tr=len(driver.find_elements_by_css_selector('table > tbody > tr'))
        for j in range(0,count_tr):
            if driver.find_element_by_css_selector('table > tbody > tr:nth-child('+str(j+1)+') > td:nth-child(7) > div > div').get_attribute('class')=='toggle-switch-animate switch-off' and tag=='qy':
                driver.find_element_by_css_selector('table > tbody > tr:nth-child('+str(j+1)+') > td:nth-child(7) > div > div > span.switch-right.ng-binding').click()
            if driver.find_element_by_css_selector('table > tbody > tr:nth-child('+str(j+1)+') > td:nth-child(7) > div > div').get_attribute('class')=='toggle-switch-animate switch-on' and tag=='ty':
                driver.find_element_by_css_selector('table > tbody > tr:nth-child('+str(j+1)+') > td:nth-child(7) > div > div > span.switch-right.ng-binding').click()
        if i>=0 and i<int(count) and int(count)>1:
            driver.find_element_by_css_selector('ul.pagination > li>a[ng-click="pager.selectNext()"]').click()

#全部启用或者停用
def spcx_qt_all(driver,tag):

    text=driver.find_element_by_css_selector('div.pagination.m-l-15.ng-binding','findAssert').text
    str1 = text.split('，')
    str2 = ''.join(str1[:1])
    count=re.sub("\D", "", str2)
    for i in range(0,int(count)):
        count_tr=len(driver.find_elements_by_css_selector('table > tbody > tr'))
        for j in range(0,count_tr):
            if driver.find_element_by_css_selector('table > tbody > tr:nth-child('+str(j+1)+') > td:nth-child(6) > div > div').get_attribute('class')=='toggle-switch-animate switch-off' and tag=='qy':
                driver.find_element_by_css_selector('table > tbody > tr:nth-child('+str(j+1)+') > td:nth-child(6) > div > div > span.switch-right.ng-binding').click()
            if driver.find_element_by_css_selector('table > tbody > tr:nth-child('+str(j+1)+') > td:nth-child(6) > div > div').get_attribute('class')=='toggle-switch-animate switch-on' and tag=='ty':
                driver.find_element_by_css_selector('table > tbody > tr:nth-child('+str(j+1)+') > td:nth-child(6) > div > div > span.switch-right.ng-binding').click()
        if i>=0 and i<int(count) and int(count)>1:
            driver.find_element_by_css_selector('ul.pagination > li>a[ng-click="pager.selectNext()"]').click()


#全部启用或者停用
def zhcx_qt_all(driver,tag):
    if driver.find_element_by_css_selector('div.row.space20.ng-scope > div:nth-child(2)').get_attribute('class')=='col-xs-12':
        text=driver.find_element_by_css_selector('div.pagination.pull-right.m-l-5','findAssert').text
        str1 = text.split('，')
        str2 = ''.join(str1[:1])
        count=re.sub("\D", "", str2)
        for i in range(0,int(count)):
            count_tr=len(driver.find_elements_by_css_selector('table > tbody > tr'))
            for j in range(0,count_tr):
                if driver.find_element_by_css_selector('table > tbody > tr:nth-child('+str(j+1)+') > td:nth-child(5) > div > div').get_attribute('class')=='toggle-switch-animate switch-off' and tag=='qy':
                    driver.find_element_by_css_selector('table > tbody > tr:nth-child('+str(j+1)+') > td:nth-child(5) > div > div > span.switch-right.ng-binding').click()
                if driver.find_element_by_css_selector('table > tbody > tr:nth-child('+str(j+1)+') > td:nth-child(5) > div > div').get_attribute('class')=='toggle-switch-animate switch-on' and tag=='ty':
                    driver.find_element_by_css_selector('table > tbody > tr:nth-child('+str(j+1)+') > td:nth-child(5) > div > div > span.switch-right.ng-binding').click()
            if i>=0 and i<int(count) and int(count)>1:
                driver.find_element_by_css_selector('ul.pagination > li>a[ng-click="pager.selectNext()"]').click()


def qy_zhcx_fa(driver,name,tag):
    text=driver.find_element_by_css_selector('div.pagination.pull-right.m-l-5','findAssert').text
    str1 = text.split('，')
    str2 = ''.join(str1[:1])
    count=re.sub("\D", "", str2)
    temp_name=''
    for i in range(0,int(count)):
        count_tr=len(driver.find_elements_by_css_selector('table > tbody > tr'))
        for j in range(0,count_tr):
            temp_name=driver.find_element_by_css_selector('table > tbody > tr:nth-child('+str(j+1)+') > td:nth-child(2) > span').text
            if temp_name==name:
                if driver.find_element_by_css_selector('table > tbody > tr:nth-child('+str(j+1)+') > td:nth-child(5) > div > div').get_attribute('class')=='toggle-switch-animate switch-off' and tag=='qy':
                    driver.find_element_by_css_selector('table > tbody > tr:nth-child('+str(j+1)+') > td:nth-child(5) > div > div > span.switch-right.ng-binding').click()
                if driver.find_element_by_css_selector('table > tbody > tr:nth-child('+str(j+1)+') > td:nth-child(5) > div > div').get_attribute('class')=='toggle-switch-animate switch-on' and tag=='ty':
                    driver.find_element_by_css_selector('table > tbody > tr:nth-child('+str(j+1)+') > td:nth-child(5) > div > div > span.switch-right.ng-binding').click()
                break
        if temp_name==name:
            break
        if i>=0 and i<int(count) and int(count)>1:
            driver.find_element_by_css_selector('ul.pagination > li>a[ng-click="pager.selectNext()"]').click()