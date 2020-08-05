from selenium import webdriver
from common.info import InfoPart
from common.readconfig import ReadConfig


# driver = webdriver.Chrome()
class GetCookies(object):
    '''通过selenium获取cookie'''

    def __init__(self):
        self.url = InfoPart.home_page
        self.user_name = InfoPart.user_name
        self.passwd = InfoPart.passwd
        self.driver = webdriver.Chrome()

    def get_cookie(self):
        self.driver.get(self.url)
        # self.driver.maximize_window()
        self.driver.find_element_by_xpath(
            "//input[@id='username']").send_keys(self.user_name)
        self.driver.find_element_by_xpath(
            "//input[@id='password']").send_keys(self.passwd)
        self.driver.find_element_by_xpath(
            "//input[contains(@class,'loginBtn')]").click()
        cookie_items = self.driver.get_cookies()[0]
        # print(cookie_items)
        cookie = cookie_items['name'] + '=' + cookie_items['value']
        # print(type(cookie))
        ReadConfig().add_option('GetCookies', 'Cookie', cookie)


if __name__ == '__main__':
    gt = GetCookies()
    print(gt.get_cookie())
