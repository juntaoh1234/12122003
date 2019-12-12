import time

from SRC.param.unitls_table import row_size


#新增商品、客户调价单按钮
def add_gc_modify_price_button(driver):
    driver.find_element_by_css_selector('div.row.space10 > div.text-right > a:nth-child(1)').click()
#点击选择商品或客户图标
def select_gc_img(driver,index):
    time.sleep(3)
    driver.find_element_by_css_selector('tbody > tr:last-child > td:nth-child('+str(index)+') > a > span').click()

#搜索客户或商品
def search_gc(driver,name):
    time.sleep(3)
    # 在搜索框中输入商品名称
    driver.find_element_by_css_selector('#exampleInputAmount').send_keys(name)
    # 点击搜索按钮
    driver.find_element_by_css_selector('i.glyphicon.glyphicon-search').click()
    time.sleep(2)
#选择客户或客户级别
def select_customer_jb(driver,c_name):
    search_gc(driver,c_name)
    #统计客户个数
    count_tr=row_size(driver,'div.row.space20 > div > table > tbody>tr')
    for i in range(0,int(count_tr)):
        if driver.find_element_by_css_selector('div.row.space20 > div > table > tbody > tr:nth-child('+str(i+1)+') > td:nth-child(3)').text==c_name:
            #选择客户
            driver.find_element_by_css_selector('div.row.space20 > div > table > tbody > tr:nth-child('+str(i+1)+') > td.text-center > input').click()
            break
    time.sleep(2)
    # 点击确定
    ok_button(driver)
    time.sleep(2)
#选择商品
def select_goods(driver,goods_name,sku):
    search_gc(driver,goods_name)
    # 统计商品个数
    count_tr = row_size(driver, 'div.col-xs-10 > div:nth-child(2) > table > tbody>tr')
    for i in range(0, int(count_tr)):
        if driver.find_element_by_css_selector('table > tbody > tr:nth-child(' + str(
                        i + 1) + ') > td.wordBreak.ng-binding').text == goods_name:
            # 选择商品
            driver.find_element_by_css_selector(
                'tbody > tr:nth-child(' + str(i + 1) + ') > td.wordBreak.ng-binding').click()
            break
    time.sleep(2)
    # 商品属性
    if sku != '无':
        sku_list = sku.split('+')
        # 获取属性个数
        count_property = row_size(driver, 'div.col-xs-12.propertyPop.space15>dl')
        for i in range(0, int(count_property)):
            count_property_value = row_size(driver, 'div.col-xs-12.propertyPop.space15 > dl:nth-child(' + str(
                i + 1) + ') > dd > a')
            for j in range(0, int(count_property_value)):
                for m in range(len(sku_list)):
                    if driver.find_element_by_css_selector('div.col-xs-12.propertyPop.space15 > dl:nth-child(' + str(
                                    i + 1) + ') > dd > a:nth-child(' + str(j + 1) + ')').text == sku_list[m]:
                        driver.find_element_by_css_selector('div.col-xs-12.propertyPop.space15 > dl:nth-child(' + str(
                            i + 1) + ') > dd > a:nth-child(' + str(j + 1) + ')').click()
                        break
    # 点击确定
    ok_button(driver)
#确定按钮
def ok_button(driver):
    # 点击确定
    driver.find_element_by_css_selector('button.btn.btn-save.btn-warning').click()

#数量下限按钮
def limit_num_button(driver,td):
    time.sleep(2)
    driver.find_element_by_css_selector('tbody > tr:nth-child(1) > td:nth-child('+str(td)+') > a > span').click()

#添加数量下限
def limit_num(driver,limitnum,price):
    time.sleep(2)
    driver.find_element_by_css_selector('tbody > tr:nth-child(1) > td:nth-child(1) > input').clear()
    driver.find_element_by_css_selector('tbody > tr:nth-child(1) > td:nth-child(1) > input').send_keys(str(limitnum))
    time.sleep(2)
    #添加价格
    driver.find_element_by_css_selector('tbody > tr:nth-child(1) > td:nth-child(2) > input').clear()
    driver.find_element_by_css_selector('tbody > tr:nth-child(1) > td:nth-child(2) > input').send_keys(str(price))
    time.sleep(2)
    #点击确定
    ok_button(driver)

#保存返回列表并点击整单生效
def order_list_zdsx(driver,tag):
    time.sleep(2)
    driver.find_element_by_css_selector('button.btn.btn-lg.btn-warning.m-l-20.ng-scope').click()
    time.sleep(3)
    #点击返回按钮
    driver.find_element_by_css_selector('a.btn.btn-default.pull-left.btn-sm ').click()
    time.sleep(2)
    if tag!='sp':
        #点击整单生效
        choose_price_dimension(driver,tag)
        time.sleep(1)
        #点击查询
        driver.find_element_by_css_selector('div.text-right > button').click()
        time.sleep(2)
    driver.find_element_by_css_selector('#secondtable > tbody > tr:nth-child(1) > td > a.btn.btn-default.btn-sm.ng-scope').click()

#点击进入订货/企业端按钮
def switch_to_dh(driver):
    driver.find_element_by_css_selector('div.pull-right.m-l-20.enter-companys-d > div').click()

def switch_to_qy(driver):
    driver.find_element_by_css_selector("div.pull-right.m-l-20.enter-companys-d.ng-scope > a > span").click()
#选择日期
def choose_date(driver,s_td,e_td,start,end):
    js='$("tbody > tr > td:nth-child('+str(s_td)+') > p > input").removeAttr("readonly")'
    driver.execute_script(js)
    driver.find_element_by_css_selector('tbody > tr > td:nth-child('+str(s_td)+') > p > input').send_keys(start)
    #选择终止日期
    js='$("tbody > tr > td:nth-child('+str(e_td)+') > p > input").removeAttr("readonly")'
    driver.execute_script(js)
    driver.find_element_by_css_selector('tbody > tr > td:nth-child('+str(e_td)+') > p > input').send_keys(end)



#选择定价维度
def price_dimension(driver,index):
    time.sleep(2)
    driver.find_element_by_css_selector('div.col-xs-11.orderList_form > a:nth-child('+str(index)+')').click()
    #点击确定
    driver.find_element_by_css_selector('button.btn.btn-primary.btn-save').click()
    time.sleep(2)

#选择定价维度--查询
def choose_price_dimension(driver,tag):
    driver.find_element_by_css_selector('form > div:nth-child(2) > div:nth-child(4) > select').click()
    if tag=='fl':
        driver.find_element_by_css_selector('form > div:nth-child(2) > div:nth-child(4) > select>option[label="客户分类"]').click()
    elif tag=='jb':
        driver.find_element_by_css_selector('form > div:nth-child(2) > div:nth-child(4) > select>option[label="客户级别"]').click()
    elif tag=='qy':
        driver.find_element_by_css_selector('form > div:nth-child(2) > div:nth-child(4) > select>option[label="区域"]').click()
    else:
        driver.find_element_by_css_selector('form > div:nth-child(2) > div:nth-child(4) > select>option[label="客户"]').click()
#选择客户分类或客户区域
def select_fl_qy_spfl(driver,td,li,name):
    time.sleep(2)
    driver.find_element_by_css_selector('table > tbody > tr > td:nth-child('+str(td)+')>div>div.col-xs-12.upDropDownTree > div > input').click()
    count_li=row_size(driver,li)
    for i in range(0,int(count_li)):
        li_text=driver.find_element_by_css_selector('table > tbody > tr > td:nth-child('+str(td)+')>div>div.col-xs-12.upDropDownTree > div > ul > li:nth-child('+str(i+1)+') > div > span.itemtxt.ng-binding').text
        if li_text==name:
            driver.find_element_by_css_selector('table > tbody > tr > td:nth-child('+str(td)+')>div>div.col-xs-12.upDropDownTree > div > ul > li:nth-child('+str(i+1)+') > div > span.itemtxt.ng-binding').click()
            break

#选择相应的客户、客户分类、区域、级别进入订货端
def select_fl_qy_jb(driver,tag,name):
    count_page=row_size(driver,'div.modal-body.modal-body-top > div:nth-child(3) > div > nav> ul> li')
    for j in range(0,int(count_page)-4):
        count_tr = row_size(driver, 'div.row.space20.select-item > div > table > tbody > tr')
        temp=''
        for i in range(0,int(count_tr)):
            if tag=='fl':
                td_text=driver.find_element_by_css_selector('div.row.space20.select-item > div > table > tbody > tr:nth-child('+str(i+1)+') > td:nth-child(4)').text
                if td_text==name:
                    driver.find_element_by_css_selector('div.row.space20.select-item > div > table > tbody > tr:nth-child('+str(i+1)+') > td:nth-child(4)').click()
                    temp=td_text
                    break
            elif tag=='qy':
                td_text=driver.find_element_by_css_selector('div.row.space20.select-item > div > table > tbody > tr:nth-child('+str(i+1)+') > td:nth-child(3)').text
                if td_text==name:
                    driver.find_element_by_css_selector('div.row.space20.select-item > div > table > tbody > tr:nth-child('+str(i+1)+') > td:nth-child(3)').click()
                    temp = td_text
                    break
            elif tag == 'jb':
                td_text=driver.find_element_by_css_selector('div.row.space20.select-item > div > table > tbody > tr:nth-child('+str(i+1)+') > td:nth-child(5)').text
                if td_text==name:
                    driver.find_element_by_css_selector('div.row.space20.select-item > div > table > tbody > tr:nth-child('+str(i+1)+') > td:nth-child(5)').click()
                    temp = td_text
                    break
            else:
                td_text=driver.find_element_by_css_selector('div.row.space20.select-item > div > table > tbody > tr:nth-child('+str(i+1)+') > td:nth-child(2)').text
                if td_text==name:
                    driver.find_element_by_css_selector('div.row.space20.select-item > div > table > tbody > tr:nth-child('+str(i+1)+') > td:nth-child(2)').click()
                    temp = td_text
                    break
        if int(count_page)-4==1:
            break
        else:
            if temp==name:
                break
            else:
                driver.find_element_by_css_selector('div.modal-body.modal-body-top > div:nth-child(3) > div > nav > ul > li:nth-child(5) > a').click()



#客户折扣定价维度
def khzk_price_dimension(driver,index):
    time.sleep(2)
    driver.find_element_by_css_selector('div[ng-controller="customerdisrate"] > div:nth-child(2) > div.col-xs-4.orderList_form > a:nth-child('+str(index)+')').click()

#折扣类型
def khzk_type(driver,index):
    time.sleep(1)
    driver.find_element_by_css_selector('div[ng-controller="customerdisrate"] > div:nth-child(3) > div.col-xs-4.orderList_form > a:nth-child('+str(index)+')').click()

#新增折扣按钮
def add_zk_button(driver):
    time.sleep(1)
    driver.find_element_by_css_selector('a.btn.btn-warning.colorfff').click()

#折扣保存状态
def zk_save_status(driver,index):
    time.sleep(1)
    driver.find_element_by_css_selector('table > tbody > tr:last-child > td.ng-scope > a:nth-child('+str(index)+')').click()
    if index==3:
        driver.find_element_by_css_selector('button.btn.btn-primary.btn-save').click()
#输入折扣率
def input_zkl(driver,zkl,td):
    time.sleep(2)
    driver.find_element_by_css_selector('table > tbody > tr:last-child > td:nth-child('+str(td)+') > input').send_keys(str(float(zkl)*100))


#判断商品价格表中是否存在此变价单
def check_googs_single_valence(driver,goods_name,sx,slxx,jg,sxrq):
    time.sleep(1)
    result='false'
    driver.find_element_by_css_selector('form > div:nth-child(1) > div:nth-child(4) > input').send_keys(goods_name)
    #点击搜索
    driver.find_element_by_css_selector('form > div:nth-child(3) > div.text-right > button').click()
    count=row_size(driver,'ul.pagination>li')
    count_row=row_size(driver,'#firsttable > tbody > tr')
    count_page=int(count)-4
    for i in range(0,count_page):
        for j in range(0,count_row):
            table_sx=''
            count_sx=row_size(driver,'#firsttable> tbody > tr:nth-child('+str(j+1)+') > td.no-border.p-0 > table > tbody > tr > td.wProductPro.ng-scope > span > upmark')
            for m in range(0,int(count_sx)):
                temp=driver.find_element_by_css_selector('#firsttable> tbody > tr:nth-child('+str(j+1)+') > td.no-border.p-0 > table > tbody > tr > td.wProductPro.ng-scope > span:nth-child('+str(m+1)+') > upmark','findAssert').text
                if m==0:
                    table_sx = ''.join(temp.split(':')[1:])
                else:
                    table_sx=table_sx+'+'+''.join(temp.split(':')[1:])
            table_slxx=driver.find_element_by_css_selector('#firsttable> tbody > tr:nth-child('+str(j+1)+') > td.no-border.p-0 > table > tbody > tr > td:nth-child(3)').text
            table_jg=driver.find_element_by_css_selector('#firsttable> tbody > tr:nth-child('+str(j+1)+') > td.no-border.p-0 > table > tbody > tr > td:nth-child(4)').text
            table_sxrq=driver.find_element_by_css_selector('#firsttable> tbody > tr:nth-child('+str(j+1)+') > td.no-border.p-0 > table > tbody > tr > td:nth-child(5)').text
            if table_sx==sx and table_slxx==slxx and table_jg==jg and table_sxrq==sxrq :
                result='true'
                break
        if count_page==1:
            break
        else:
            if result=='true':
                break
            else:
                driver.find_element_by_css_selector('div.row.space20 > div > div.col-xs-12 > nav > ul > li:nth-child(5) > a > span').click()
    return result

#获取客户价格表中是否存在此变价单
def check_customer_single_valence(driver,tag,c_name,g_name,sx,slxx,jg,sxrq):
    time.sleep(1)
    result = 'false'
    choose_price_dimension(driver, tag)
    #输入商品名称
    driver.find_element_by_css_selector('input[ng-model="proNameOrCode"]').send_keys(g_name)
    #选择客户、客户分类、客户级别、区域
    driver.find_element_by_css_selector('button[ng-click="selectAgents()"]').click()
    search_gc(driver, c_name)
    choose_customer_sx(driver, c_name, tag)
    ok_button(driver)
    #点击搜索
    driver.find_element_by_css_selector('button[ng-click="search()"]').click()
    count=row_size(driver,'ul.pagination>li')
    count_row=row_size(driver,'#firsttable > tbody> tr')
    count_page=int(count)-4
    for i in range(0,count_page):
        for j in range(0,count_row):
            table_sx = '无'
            count_sx=row_size(driver,'#firsttable> tbody > tr:nth-child('+str(j+1)+') > td.no-border.p-0 > table > tbody > tr > td.wProductPro.ng-scope > span > upmark')
            for m in range(0,int(count_sx)):
                temp=driver.find_element_by_css_selector('#firsttable> tbody > tr:nth-child('+str(j+1)+') > td.no-border.p-0 > table > tbody > tr > td.wProductPro.ng-scope > span:nth-child('+str(m+1)+') > upmark','findAssert').text
                if m==0:
                    table_sx = ''.join(temp.split(':')[1:])
                else:
                    table_sx=table_sx+'+'+''.join(temp.split(':')[1:])
            table_slxx=driver.find_element_by_css_selector('#firsttable> tbody > tr:nth-child('+str(j+1)+') > td.no-border.p-0 > table > tbody > tr > td:nth-child(4)').text
            table_jg=driver.find_element_by_css_selector('#firsttable> tbody > tr:nth-child('+str(j+1)+') > td.no-border.p-0 > table > tbody > tr > td:nth-child(5)').text
            table_sxrq=driver.find_element_by_css_selector('#firsttable > tbody> tr:nth-child('+str(j+1)+') > td.no-border.p-0 > table > tbody > tr > td:nth-child(6)').text
            if table_sx==sx and table_slxx==slxx and table_jg==jg and table_sxrq==sxrq :
                result='true'
                break
        if count_page==1:
            break
        else:
            if result=='true':
                break
            else:
                driver.find_element_by_css_selector('div.row.space20 > div > div.col-xs-12 > nav > ul > li.next.disabled > a > span').click()
    return result
#获取客户折扣设置表中是否存在此记录ctag=1客户 2客户分类 3客户级别 4客户区域 gtag=1 商品分类 2商品
def check_customer_discount_price(driver,customer,goods,sx,ctag,gtag):
    result = 'false'
    if ctag==1:
        driver.find_element_by_css_selector('div.col-xs-10.corp-content.printlayout > div:nth-child(4) > div:nth-child(4) > div:nth-child(1) > div > input').clear()
        driver.find_element_by_css_selector('div.col-xs-10.corp-content.printlayout > div:nth-child(4) > div:nth-child(4) > div:nth-child(1) > div > input').send_keys(customer)
    elif ctag==2:
        driver.find_element_by_css_selector('div.col-xs-10.corp-content.printlayout > div:nth-child(4) > div:nth-child(4) > div:nth-child(3) > div > input').clear()
        driver.find_element_by_css_selector('div.col-xs-10.corp-content.printlayout > div:nth-child(4) > div:nth-child(4) > div:nth-child(3) > div > input').send_keys(customer)
    elif ctag==3:
        driver.find_element_by_css_selector('div.col-xs-10.corp-content.printlayout > div:nth-child(4) > div:nth-child(4) > div:nth-child(4) > div > input').clear()
        driver.find_element_by_css_selector('div.col-xs-10.corp-content.printlayout > div:nth-child(4) > div:nth-child(4) > div:nth-child(4) > div > input').send_keys(customer)
    elif ctag==4:
        driver.find_element_by_css_selector('div.col-xs-10.corp-content.printlayout > div:nth-child(4) > div:nth-child(4) > div:nth-child(2) > div > input').clear()
        driver.find_element_by_css_selector('div.col-xs-10.corp-content.printlayout > div:nth-child(4) > div:nth-child(4) > div:nth-child(2) > div > input').send_keys(customer)

    if gtag==1:
        driver.find_element_by_css_selector('div.col-xs-10.corp-content.printlayout > div:nth-child(4) > div:nth-child(4) > div:nth-child(5) > div > input').clear()
        driver.find_element_by_css_selector('div.col-xs-10.corp-content.printlayout > div:nth-child(4) > div:nth-child(4) > div:nth-child(5) > div > input').send_keys(goods)
    elif gtag==2:
        driver.find_element_by_css_selector('div.col-xs-10.corp-content.printlayout > div:nth-child(4) > div:nth-child(4) > div:nth-child(6) > div > input').clear()
        driver.find_element_by_css_selector('div.col-xs-10.corp-content.printlayout > div:nth-child(4) > div:nth-child(4) > div:nth-child(6) > div > input').send_keys(goods)
    #点击查询
    driver.find_element_by_css_selector('div.form-group.text-right.col-xs-2 > button').click()
    count=row_size(driver,'table > tbody > tr')
    if int(count)>0:
        if sx=='':
            result = 'true'
        else:
            for i in range(0,int(count)):
                table_sx = '无'
                table_temp=driver.find_element_by_css_selector('table > tbody > tr:nth-child('+str(i+1)+') > td:nth-child(5) > span').text
                if table_temp!='':
                    temp_sx=table_temp.split(';')
                    count_sx=len(temp_sx)
                    for i in range(0,count_sx):
                        if i==0:
                            table_sx=''.join(temp_sx[i].split(':')[1:])
                        else:
                            table_sx = table_sx + '+' + ''.join(temp_sx[i].split(':')[1:])
                if table_sx==sx:
                    result = 'true'
                    break
    return result


#选择客户、客户分类、客户级别、区域
def choose_customer_sx(driver,name,tag):
    temp_name=''
    if tag=='kh' or tag=='jb':
        count_page=row_size(driver,'div.modal-body > div:nth-child(3) > div > nav > ul>li')
        count_row=row_size(driver,'div.modal-body > div.row.space20 > div > table > tbody > tr')
    elif tag=='fl':
        count_page=row_size(driver,'div.modal-body > div > div.col-xs-9 > div:nth-child(3) > div > nav > ul>li')
        count_row=row_size(driver,'div.modal-body > div > div.col-xs-9 > div:nth-child(2) > div > table > tbody > tr')
    else:
        count_page=row_size(driver,'div.modal-body > div > div.col-xs-9 > div:nth-child(3) > div > div > nav > ul>li')
        count_row=row_size(driver,'div.modal-body > div > div.col-xs-9 > div:nth-child(2) > div > table > tbody > tr')
    for i in range(0,int(count_page)-4):
        for j in range(0,int(count_row)):
            if tag == 'kh' or tag == 'jb':
                text_name=driver.find_element_by_css_selector('div.modal-body > div.row.space20 > div > table > tbody > tr:nth-child('+str(j+1)+') > td:nth-child(2)').text
                if text_name==name:
                    driver.find_element_by_css_selector('div.modal-body > div.row.space20 > div > table > tbody > tr:nth-child('+str(j+1)+') > td:nth-child(2)').click()
                    temp_name=text_name
                    break

            elif tag=='fl':
                text_name = driver.find_element_by_css_selector(
                    'div.modal-body > div > div.col-xs-9 > div:nth-child(2) > div > table > tbody > tr:nth-child(' + str(
                        j + 1) + ') > td:nth-child(2)').text
                if text_name == name:
                    driver.find_element_by_css_selector(
                        'div.modal-body > div > div.col-xs-9 > div:nth-child(2) > div > table > tbody > tr:nth-child(' + str(
                            j + 1) + ') > td:nth-child(2)').click()
                    temp_name = text_name
                    break
            else:
                text_name = driver.find_element_by_css_selector('div.modal-body > div > div.col-xs-9 > div:nth-child(2) > div > table > tbody > tr:nth-child('+str(j+1)+') > td:nth-child(2)').text
                if text_name == name:
                    driver.find_element_by_css_selector('div.modal-body > div > div.col-xs-9 > div:nth-child(2) > div > table > tbody > tr:nth-child('+str(j+1)+') > td:nth-child(2)').click()
                    temp_name = text_name
                    break

        if int(count_page)-4==1:
            break
        else:
            if temp_name==name:
                break
            else:
                driver.find_element_by_css_selector('div.modal-body > div:nth-child(3) > div > nav > ul > li:nth-child(5) > a > span').click()











