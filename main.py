from selenium import webdriver
from time import sleep
from secrets import pw

__name__ = "__main__"

username = 'kon.soursos'

def main():
    driver = webdriver.Chrome()
    driver.get("https://instagram.com")
    sleep(1)
    driver.find_element_by_xpath("//a[contains(text(), 'Log in')]") \
        .click()
    sleep(1)

    driver.find_element_by_xpath("//input[@name=\"username\"]") \
        .send_keys(username)
    driver.find_element_by_xpath("//input[@name=\"password\"]") \
        .send_keys(pw)

    # 2 ways of doing it
    # self.driver.find_element_by_xpath('//button[@type="submit"]')\
    #     .click()
    driver.find_element_by_xpath("//div[contains(text(), 'Log In')]") \
        .click()
    sleep(2)

    # self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
    #     .click()
    driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
    sleep(1)

#     not now

    # self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
    #     .click()
    driver.find_element_by_xpath("//a[@href=\"/kon.soursos/\"]") \
        .click()
    sleep(2)

    # self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
    #     .click()
    # self.driver.find_element_by_xpath("//a[contains(@href, '/kon.soursos/following')]")\
    #     .click()
    # self.driver.find_element_by_xpath("//a[@href=\"/kon.soursos/following/\"]") \
    #     .click()
    driver.find_element_by_xpath("//a[@href='/kon.soursos/following/']") \
        .click()

    following = get_names(driver)

    driver.find_element_by_xpath("//a[contains(@href,'/followers')]") \
        .click()
    followers = get_names(driver)

    not_following_back = [user for user in following if user not in followers]

    # print(following)
    print(not_following_back)

def get_names(driver):
    sleep(2)
    # sugs = self.driver.find_element_by_xpath('//h4[contains(text(), Suggestions)]')
    # self.driver.execute_script('arguments[0].scrollIntoView()', sugs)
    # sleep(2)

    # scroll_box = self.driver.find_element_by_xpath("/html/body/div[6]/div/div[2]")
    scroll_box = driver.find_element_by_xpath("//div[@class=\"isgrP\"]")
    last_ht, ht = 0, 1
    while last_ht != ht:
        last_ht = ht
        sleep(1)
        ht = driver.execute_script("""
                    arguments[0].scrollTo(0, arguments[0].scrollHeight);
                    return arguments[0].scrollHeight;
                    """, scroll_box)
    links = scroll_box.find_elements_by_tag_name('a')
    names = [name.text for name in links if name.text != '']
    # close button
    driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button") \
        .click()
    return names

if __name__ == '__main__':
    main()