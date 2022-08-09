from page.base_page import *


class MainPage(Base):
    def yandex_redirect_to_main_page(self):
        self.close_cookies()
        self.browser.find_element(*MainPageLocators.yandex_button).click()
        self.browser.switch_to.window(self.browser.window_handles[1])
        WebDriverWait(self.browser, 5).until(expected_conditions.url_contains("https://yandex.ru/"))

    def redirect_to_order_page_from_header_order_button(self):
        self.close_cookies()
        self.browser.find_element(*MainPageLocators.order_button_header).click()

    def redirect_to_order_page_from_middle_order_button(self):
        self.close_cookies()
        self.scroll_till_middle()
        self.browser.find_element(*MainPageLocators.order_button_middle).click()

    def how_much_cost(self):
        self.close_cookies()
        self.scroll_till_questions_block()
        WebDriverWait(self.browser, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.how_much_cost))
        self.browser.find_element(*MainPageLocators.how_much_cost).click()
        WebDriverWait(self.browser, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.answer_how_much_cost))

    def couple_scooters(self):
        self.close_cookies()
        self.scroll_till_questions_block()
        WebDriverWait(self.browser, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.couple_scooters))
        self.browser.find_element(*MainPageLocators.couple_scooters).click()
        WebDriverWait(self.browser, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.answer_couple_scooters))

    def rent_time(self):
        self.close_cookies()
        self.scroll_till_questions_block()
        WebDriverWait(self.browser, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.rent_time))
        self.browser.find_element(*MainPageLocators.rent_time).click()
        WebDriverWait(self.browser, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.answer_rent_time))

    def rent_today(self):
        self.close_cookies()
        self.scroll_till_questions_block()
        WebDriverWait(self.browser, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.rent_today))
        self.browser.find_element(*MainPageLocators.rent_today).click()
        WebDriverWait(self.browser, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.answer_rent_today))

    def prolongation_rent(self):
        self.close_cookies()
        self.scroll_till_questions_block()
        WebDriverWait(self.browser, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.prolongation_rent))
        self.browser.find_element(*MainPageLocators.prolongation_rent).click()
        WebDriverWait(self.browser, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.answer_prolongation_rent))

    def charger_with_scooter(self):
        self.close_cookies()
        self.scroll_till_questions_block()
        WebDriverWait(self.browser, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.charger_with_scooter))
        self.browser.find_element(*MainPageLocators.charger_with_scooter).click()
        WebDriverWait(self.browser, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.answer_charger_with_scooter))

    def cancel_order(self):
        self.close_cookies()
        self.scroll_till_questions_block()
        WebDriverWait(self.browser, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.cancel_order))
        self.browser.find_element(*MainPageLocators.cancel_order).click()
        WebDriverWait(self.browser, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.answer_cancel_order))

    def behind_MKAD(self):
        self.close_cookies()
        self.scroll_till_questions_block()
        WebDriverWait(self.browser, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.behind_MKAD))
        self.browser.find_element(*MainPageLocators.behind_MKAD).click()
        WebDriverWait(self.browser, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.answer_behind_MKAD))
