#进入各个界面
def navigation_bar(driver,parent_node,child_node):
    driver.find_element_by_css_selector('div.col-xs-2.corp-mune > div > div > div > a').click()
    if parent_node>3:
        #点击父节点
        driver.find_element_by_css_selector("div.col-xs-2.corp-mune > div > div > ul:nth-child("+str(parent_node)+") > li.title.pointer > upmark").click()
    #点击子节点
    driver.find_element_by_css_selector("div.col-xs-2.corp-mune > div > div > ul:nth-child("+str(parent_node)+") > li:nth-child("+str(child_node)+") > a").click()

