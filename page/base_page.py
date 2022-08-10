import allure
from page.locators import *


class Base:
    def __init__(self, browser_mozilla):
        self.browser = browser_mozilla

    @allure.step(f"Открываем браузер по ссылке {MainPageLocators.main_url}")
    def open(self):
        self.browser.get(MainPageLocators.main_url)

    @allure.step("Закрываем надоедливые куки")
    def close_cookies(self):
        self.browser.find_element(*MainPageLocators.confirm_cookies).click()

    @allure.step("Скроллим до блока с вопросами")
    def scroll_till_questions_block(self):
        self.browser.execute_script("window.scrollBy(0, 2000);")

    @allure.step("Скроллим до середины страницы")
    def scroll_till_middle(self):
        self.browser.execute_script("window.scrollBy(0, 1500);")
