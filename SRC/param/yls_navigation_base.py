from selenium.webdriver import ActionChains
import time

def jigoudangan_navigation(driver,daohang):
    '''
    chain = ActionChains(driver)
    implement = driver.find_element_by_css_selector(daohan)  # 鼠标悬浮到**处
    time.sleep(2)
    chain.move_to_element(implement).perform()
    time.sleep(3)
    '''
    driver.find_element_by_css_selector(daohang).click()