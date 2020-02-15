from selenium import webdriver
from time import sleep
from secrets import pw

class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(1)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]")\
            .click()
        sleep(1)

        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)


        # 2 ways of doing it
        # self.driver.find_element_by_xpath('//button[@type="submit"]')\
        #     .click()
        self.driver.find_element_by_xpath("//div[contains(text(), 'Log In')]")\
            .click()
        sleep(2)

        # self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
        #     .click()
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
        sleep(1)

    def get_unfollowers(self):
        # self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
        #     .click()
        self.driver.find_element_by_xpath("//a[@href=\"/kon.soursos/\"]") \
            .click()
        sleep(2)

        # self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
        #     .click()
        # self.driver.find_element_by_xpath("//a[contains(@href, '/kon.soursos/following')]")\
        #     .click()
        # self.driver.find_element_by_xpath("//a[@href=\"/kon.soursos/following/\"]") \
        #     .click()
        self.driver.find_element_by_xpath("//a[@href='/kon.soursos/following/']") \
            .click()

        following = self._get_names()

        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()
        followers = self._get_names()

        not_following_back = [user for user in following if user not in followers]

        # print(following)
        print(not_following_back)

    def _get_names(self):
        sleep(2)
        # sugs = self.driver.find_element_by_xpath('//h4[contains(text(), Suggestions)]')
        # self.driver.execute_script('arguments[0].scrollIntoView()', sugs)
        # sleep(2)

        # scroll_box = self.driver.find_element_by_xpath("/html/body/div[6]/div/div[2]")
        scroll_box = self.driver.find_element_by_xpath("//div[@class=\"isgrP\"]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # close button
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button")\
            .click()
        return names

# /html/body/div[6]/div/div[1]/div/div[2]/button/svg
my_bot = InstaBot('kon.soursos', pw)
my_bot.get_unfollowers()