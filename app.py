import selenium
from selenium import webdriver
from time import sleep


class TinderBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe')     #open chrome browser
        self.driver.get('https://www.tinder.com')                              #go to url
        sleep(3)

    def login(self):                                                           #find login_button in the web page
        login_button = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
        sleep(3)
        login_button.click()
        sleep(3)

    def login_method(self):                                                     #choose the phone number to login
        enter_button = self.driver.find_element_by_xpath(
        '//*[@id="o-1268705039"]/div/div/div[1]/div/div[3]/span/div[3]/button')
        sleep(1)
        enter_button.click()
        sleep(1)

    def waiting_for_manual_input(self):  
        while True:
            print("Are you on the tinder page? (y/n)")
            var = input()

            if var == "y":
                break
            else:
                pass
        
    def localization_pop_up(self):
        enable_localization = self.driver.find_element_by_xpath(
            '//*[@id="o-1268705039"]/div/div/div/div/div[3]/button[2]')
        sleep(3)
        enable_localization.click()
        sleep(3)

    def notifications_pop_up(self):
        disable_notifications = self.driver.find_element_by_xpath(
            '//*[@id="o-1268705039"]/div/div/div/div/div[3]/button[2]')
        sleep(3)
        disable_notifications.click()
        sleep(3)

    def dar_like(self):
        try:
            sleep(3)
            botao_like = self.driver.find_elements_by_xpath(
                '//div[@class="Mx(a) Fxs(0) Sq(70px) Sq(60px)--s"]//button')[1]
        except:
            try:
                sleep(3)
                botao_like = self.driver.find_element_by_xpath(
                    '//div[@class="Mx(a) Fxs(0) Sq(70px) Sq(60px)--s Bd Bdrs(50%) Bdc($c-like-green)"]')
            except:
                pass
        finally:
            sleep(3)
            botao_like.click()
            try:
                sleep(3)
                if self.driver.find_element_by_xpath("//label[text()='Say something nice!']") is not None:
                    sleep(3)
                    fechar_janela_match = self.driver.find_element_by_xpath(
                        "//button[@title='Back to Tinder']")
                    sleep(3)
                    fechar_janela_match.click()
                    sleep(3)
            except:
                pass

if __name__ == '__main__':
    
    bot = TinderBot()
    bot.login()
    bot.login_method()
    bot.waiting_for_manual_input()
    bot.localization_pop_up()
    bot.notifications_pop_up()

    while True:
        bot.dar_like()
