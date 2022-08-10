from page.order_page import *
import allure


class TestOrder:
    @allure.title("Редирект на главную страницу со страницы Заказа")
    @allure.description("Проверяем переход на главную страницу со страницы Заказ")
    def test_redirect_to_main_page_from_order_page(self, browser_mozilla):
        page = OrderPage(browser_mozilla)
        page.open()
        page.redirect_to_main_page_from_order_page()
        assert browser_mozilla.current_url == MainPageLocators.main_url

    @allure.title("Оформление заказа с верхней кнопки Заказ")
    def test_order_from_header_button(self, browser_mozilla):
        page = OrderPage(browser_mozilla)
        page.open()
        page.order_from_header_button()
        message_success_order = browser_mozilla.find_element(*OrderPageLocators.success_order)
        assert "Заказ оформлен" in message_success_order.text

    @allure.title("Оформление заказа со средней кнопки Заказ")
    def test_order_from_middle_button(self, browser_mozilla):
        page = OrderPage(browser_mozilla)
        page.open()
        page.order_from_middle_button()
        message_success_order = browser_mozilla.find_element(*OrderPageLocators.success_order)
        assert "Заказ оформлен" in message_success_order.text
