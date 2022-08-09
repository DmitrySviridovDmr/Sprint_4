from selenium.webdriver import Keys
from page.base_page import *
import datetime
from datetime import timedelta

tomorrow_date = str(datetime.date.today() + timedelta(days=1))


class OrderPage(Base):
    def redirect_to_main_page_from_order_page(self):
        self.close_cookies()
        self.browser.find_element(*MainPageLocators.order_button_header).click()
        self.browser.find_element(*OrderPageLocators.scooter_button).click()

    def info_order(self):
        self.browser.find_element(*OrderPageLocators.first_name).send_keys("Иван")
        self.browser.find_element(*OrderPageLocators.last_name).send_keys("Иванов")
        self.browser.find_element(*OrderPageLocators.address).send_keys("Московское шоссе, 55")
        self.browser.find_element(*OrderPageLocators.station).click()
        self.browser.find_element(*OrderPageLocators.station).send_keys(Keys.ARROW_DOWN + Keys.ENTER)
        self.browser.find_element(*OrderPageLocators.phone).send_keys("99999999999")
        self.browser.find_element(*OrderPageLocators.next_button).click()
        self.browser.find_element(*OrderPageLocators.date_field).send_keys(tomorrow_date + Keys.ENTER)
        self.browser.find_element(*OrderPageLocators.rent_period).click()

    def order_from_header_button(self):
        self.close_cookies()
        self.browser.find_element(*MainPageLocators.order_button_header).click()
        self.info_order()
        self.browser.find_element(*OrderPageLocators.one_day).click()
        self.browser.find_element(*OrderPageLocators.black_color_scooter).click()
        self.browser.find_element(*OrderPageLocators.order_button).click()
        self.browser.find_element(*OrderPageLocators.yes_button).click()

    def order_from_middle_button(self):
        self.close_cookies()
        self.scroll_till_middle()
        self.browser.find_element(*MainPageLocators.order_button_middle).click()
        self.info_order()
        self.browser.find_element(*OrderPageLocators.three_days).click()
        self.browser.find_element(*OrderPageLocators.grey_color_scooter).click()
        self.browser.find_element(*OrderPageLocators.comment_for_courier).send_keys("This is autoTest")
        self.browser.find_element(*OrderPageLocators.order_button).click()
        self.browser.find_element(*OrderPageLocators.yes_button).click()
