
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Insta():
        def __init__(self):
            self.driver= webdriver.Chrome()


        def Login(self):
            self.driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
            sleep(2)
            user_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
            user_input.send_keys('stelios_vrdks')
            password_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')
            password_input.send_keys('1313as13ste13gr')

            log_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div')
            log_btn.click()

            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".aOOlW.HoLwm"))).click()


            profile = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a')
            profile.click()
            sleep(2)
            followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
            followers.click()
            sleep(2)
            scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
            last_ht, ht = 0, 1
            while last_ht != ht:
                last_ht = ht
                sleep(1)
                ht = self.driver.execute_script("""
                    arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                    # return arguments[0].scrollHeight;
                    """, scroll_box)
            links = scroll_box.find_elements_by_tag_name('a')
            names = [name.text for name in links if name.text != '']
            print(names)


