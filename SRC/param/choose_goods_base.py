import re
import time

from SRC.param.unitls_table import row_size

#搜索商品
def search_goods(driver,goods_name):
    # 在输入框中输入商品名称进行搜索
    driver.find_element_by_css_selector('div.col-xs-9.p-r-0 > div > input').clear()
    driver.find_element_by_css_selector('div.col-xs-9.p-r-0 > div > input').send_keys(goods_name)
    driver.find_element_by_css_selector('div.col-xs-9.p-r-0 > div > span > button').click()
    # 统计搜索出来商品的数量
    count_goods = row_size(driver, 'div.col-xs-12 > ul>li')
    for i in range(0, int(count_goods)):
        if driver.find_element_by_css_selector('div.col-xs-12 > ul > li:nth-child(' + str(
                        i + 1) + ') > div.shopListTxt > p > a').text == goods_name:
            driver.find_element_by_css_selector(
                'div.col-xs-12 > ul > li:nth-child(' + str(i + 1) + ') > div.listimg > a > img').click()
            break
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

#搜索商品并立即订购
def select_goods_order_now(driver,goods_name,sku,order_num,):
    search_goods(driver,goods_name)
    if sku == '无':
        # 输入订货数量
        driver.find_element_by_css_selector('table > tbody > tr > td.model-body-btn > div > input').click()
        driver.find_element_by_css_selector('table > tbody > tr > td.model-body-btn > div > input').send_keys(str(order_num))
    else:
        sku_list = str(sku).split('+')
        if '+' in sku:
            # 获取第一个属性个数
            count_first_property_value = row_size(driver, 'div.col-xs-10.p-0 > ul > li')
            for i in range(0, int(count_first_property_value)):
                for j in range(len(sku_list)):
                    if driver.find_element_by_css_selector('div.col-xs-10.p-0 > ul > li:nth-child(' + str(
                                    i + 1) + ') > a > span').text == sku_list[j]:
                        driver.find_element_by_css_selector(
                            'div.col-xs-10.p-0 > ul > li:nth-child(' + str(i + 1) + ') > a > span').click()
                        break
        count_second_property_value = row_size(driver, 'div.col-dt-dtnum.m-t-15.p-t-15 >table > tbody>tr')
        for m in range(0, int(count_second_property_value)):
            for n in range(len(sku_list)):
                if driver.find_element_by_css_selector(
                                        'div.col-dt-dtnum.m-t-15.p-t-15 >table > tbody > tr:nth-child('+str(m + 1)+') > td:nth-child(2)').text == sku_list[n]:
                    driver.find_element_by_css_selector(
                        'div.col-dt-dtnum.m-t-15.p-t-15 >table > tbody > tr:nth-child(' + str(m + 1) + ') > td.model-body-btn > div > input').click()
                    driver.find_element_by_css_selector(
                        'div.col-dt-dtnum.m-t-15.p-t-15 >table > tbody > tr:nth-child(' + str(m + 1) + ') > td.model-body-btn > div > input').send_keys(str(order_num))
                    break
    time.sleep(3)
    # 点击立即订购
    driver.find_element_by_css_selector('button.btn.btn-objoder-orange.ng-scope').click()

#订单中添加商品
def order_add_goods(driver,name,num,index):
    #点击添加商品
    driver.find_element_by_css_selector('a.btn.btn-warning.m-r-15.pull-right').click()
    #输入商品名称
    driver.find_element_by_css_selector('#exampleInputAmount').send_keys(name)
    #点击搜索
    driver.find_element_by_css_selector('div.btn.input-group-addon.btn-sm').click()
    element=driver.find_elements_by_css_selector('div.modal-body > div.col-xs-10 > div:nth-child(2) > table > tbody > tr> td.wordBreak.ng-binding')
    for ele in element:
        if driver.find_element_by_css_selector('div.modal-body > div.col-xs-10 > div:nth-child(2) > table > tbody > tr:nth-child('+str(element.index(ele)+1)+')> td.wordBreak.ng-binding').text==name:
            driver.find_element_by_css_selector('div.modal-body > div.col-xs-10 > div:nth-child(2) > table > tbody > tr:nth-child('+str(element.index(ele)+1)+') > td.text-center.ng-scope > input').click()
            break
    #点击确定
    driver.find_element_by_css_selector('div.modal-footer > div > button.btn.btn-save.btn-warning').click()
    time.sleep(4)
    #输入数量
    driver.find_elements_by_css_selector('div.row.m-t-10 > div > div > table > tbody > tr[ng-repeat="product in group.lsOrderDetails"] > td:nth-child(8) > div > input').pop(index).clear()
    driver.find_elements_by_css_selector('div.row.m-t-10 > div > div > table > tbody > tr[ng-repeat="product in group.lsOrderDetails"] > td:nth-child(8) > div > input').pop(index).send_keys(num)

#设置赠品
def set_zp(driver,goods_name,num):
    #点击设置赠品
    driver.find_element_by_css_selector('div.row.m-t-10 > div > div > table > tbody:nth-child(3) > tr:nth-child(1) > td > a').click()
    #删除已有赠品
    element=driver.find_elements_by_css_selector('div.modal-body > div > table > tbody > tr > td:nth-child(6) > div > div.col-xs-8 > div > a')
    for ele in element:
        driver.find_element_by_css_selector('div.modal-body > div > table > tbody > tr > td:nth-child(6) > div:nth-child(1) > div.col-xs-8 > div > a').click()
    #点击选择商品
    driver.find_element_by_css_selector('div.modal-body > div > table > tbody > tr > td:nth-child(6) > span > a > span').click()
    #输入商品名称
    driver.find_element_by_css_selector('#exampleInputAmount').send_keys(goods_name)
    #点击搜索
    driver.find_element_by_css_selector('div.btn.input-group-addon.btn-sm').click()
    element=driver.find_elements_by_css_selector('div.modal-body > div.col-xs-10 > div:nth-child(2) > table > tbody > tr> td.wordBreak.ng-binding')
    for ele in element:
        if driver.find_element_by_css_selector('div.modal-body > div.col-xs-10 > div:nth-child(2) > table > tbody > tr:nth-child('+str(element.index(ele)+1)+')> td.wordBreak.ng-binding').text==goods_name:
            driver.find_element_by_css_selector('div.modal-body > div.col-xs-10 > div:nth-child(2) > table > tbody > tr:nth-child('+str(element.index(ele)+1)+') > td.text-center.ng-scope > input').click()
            break
    #点击确定
    driver.find_element_by_css_selector('div.modal-footer > div > button.btn.btn-save.btn-warning').click()
    time.sleep(4)
    #输入数量
    driver.find_element_by_css_selector('div.modal-body > div > table > tbody > tr > td:nth-child(7) > input').clear()
    driver.find_element_by_css_selector('div.modal-body > div > table > tbody > tr > td:nth-child(7) > input').clear()
    driver.find_element_by_css_selector('div.modal-body > div > table > tbody > tr > td:nth-child(7) > input').send_keys(num)
    #点击是
    driver.find_element_by_css_selector('button.btn.btn-primary.btn-save').click()


#组合促销下单
def zhcx_order(driver,goods_name):
    search_goods(driver,goods_name)
    #点击立即订购
    driver.find_element_by_css_selector('div.btns > p:nth-child(3) > button.buy').click()
    #点击立即订购
    driver.find_element_by_css_selector('div.total > button:nth-child(2)').click()

#获取界面单价
def get_ui_price(driver):
    return driver.find_element_by_css_selector(
        'div.col-xs-12.order-add>h4>div>span:nth-child(2)>span>strong','findAssert').text

#获取赠品名称，数量
def get_name_money(driver):
    element=driver.find_elements_by_css_selector('div.row.m-t-10 > div > div > table > tbody > tr[ng-repeat="product in group.lsOrderDetails"]')
    lis=[]
    i=0
    for ele in element:
        dic = {}
        if driver.find_elements_by_css_selector('div.row.m-t-10 > div > div > table > tbody > tr[ng-repeat="product in group.lsOrderDetails"] > td:nth-child(3) > span','findAssert').pop(element.index(ele)).text=='赠品':
            dic['zp']='Y'
            num=driver.find_elements_by_css_selector('div.row.m-t-10 > div > div > table > tbody> tr[ng-repeat="product in group.lsOrderDetails"] > td:nth-child(8) > span > span.ng-binding').pop(i).text
            dic['num']=re.sub("\D", "", num)
            i=i+1
        else:
            dic['zp']='N'
        dic['name']=driver.find_elements_by_css_selector('div.row.m-t-10 > div > div > table > tbody > tr[ng-repeat="product in group.lsOrderDetails"] > td:nth-child(5) > p.text-link-info > a').pop(element.index(ele)).text
        money=driver.find_elements_by_css_selector('div.row.m-t-10 > div > div > table > tbody > tr[ng-repeat="product in group.lsOrderDetails"] > td:nth-child(14) > div').pop(element.index(ele)).text
        dic['money']=re.sub("\￥", "", money)
        lis.insert(element.index(ele),dic)
    return lis,i



