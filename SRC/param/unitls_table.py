#获取元素个数
def row_size(driver, tr):
    js = 'var size = $("' + tr + '").size();for(i=0;i<=size;i++){$("body").append("<span style=\\\"display:none\\\" name=\\\"trs\\\"></span>");}'
    driver.execute_script(js)
    spans = driver.find_elements_by_css_selector("span[name='trs']")
    row_num = len(spans) - 1
    # 删除在页面中添加的元素
    driver.execute_script('$("span[name=\'trs\']").remove();')
    return row_num