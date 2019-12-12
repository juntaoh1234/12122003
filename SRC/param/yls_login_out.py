import time


def login(driver,url,user,psw):
    driver.delete_all_cookies()  # 清楚缓存
    driver.get(url+'/login')
    time.sleep(3)
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys(user)
    driver.find_element_by_css_selector('input[type="password"]').clear()
    driver.find_element_by_css_selector('input[type="password"]').send_keys(psw)
    time.sleep(3)
    driver.find_element_by_css_selector("button.ant-btn.login-btn-lfrt").click()
    time.sleep(2)
    driver.get(url+"/portal?device=test")


def logout(driver):
    driver.find_element_by_css_selector('div.top-right > span.title-name').click()
    driver.find_element_by_css_selector("div.ant-popover-inner-content > div > p:nth-child(3) > a").click()  # 点击退出