from page.main_page import *
from page.locators import *
import allure


class TestMainPage:
    @allure.title("Редирект на главную страницу яндекса")
    @allure.description(f"Проверяем переход на {MainPageLocators.yandex_url}")
    def test_yandex_redirect_to_main_page(self, browser_mozilla):
        page = MainPage(browser_mozilla)
        page.open()
        page.yandex_redirect_to_main_page()
        assert browser_mozilla.current_url == MainPageLocators.yandex_url

    @allure.title("Редирект на страницу заказа с верхней кнопки Заказ")
    @allure.description("Проверяем переход на страницу заказа с верхней кнопки Заказ")
    def test_redirect_to_order_page_from_header_order_button(self, browser_mozilla):
        page = MainPage(browser_mozilla)
        page.open()
        page.redirect_to_order_page_from_header_order_button()
        assert browser_mozilla.current_url == OrderPageLocators.order_url

    @allure.title("Редирект на страницу заказа со средней кнопки Заказ")
    @allure.description("Проверяем переход на страницу заказа со средней кнопки Заказ")
    def test_redirect_to_order_page_from_middle_order_button(self, browser_mozilla):
        page = MainPage(browser_mozilla)
        page.open()
        page.redirect_to_order_page_from_middle_order_button()
        assert browser_mozilla.current_url == OrderPageLocators.order_url


class TestQuestions:
    @allure.title("Вопрос о стоимости")
    def test_how_much_cost(self, browser_mozilla):
        page = MainPage(browser_mozilla)
        page.open()
        page.how_much_cost()
        assert "Сутки — 400 рублей. Оплата курьеру — наличными или картой." in browser_mozilla.find_element(
            *MainPageLocators.answer_how_much_cost).text

    @allure.title("Вопрос о нескольких самокатах")
    def test_couple_scooters(self, browser_mozilla):
        page = MainPage(browser_mozilla)
        page.open()
        page.couple_scooters()
        assert "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто " \
               "сделать несколько заказов — один за другим." in browser_mozilla.find_element(
            *MainPageLocators.answer_couple_scooters).text

    @allure.title("Вопрос о времени аренды")
    def test_rent_time(self, browser_mozilla):
        page = MainPage(browser_mozilla)
        page.open()
        page.rent_time()
        assert "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени " \
               "аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, " \
               "суточная аренда закончится 9 мая в 20:30." in browser_mozilla.find_element(
            *MainPageLocators.answer_rent_time).text

    @allure.title("Вопрос о аренде на сегодня")
    def test_rent_today(self, browser_mozilla):
        page = MainPage(browser_mozilla)
        page.open()
        page.rent_today()
        assert "Только начиная с завтрашнего дня. Но скоро станем расторопнее." in browser_mozilla.find_element(
            *MainPageLocators.answer_rent_today).text

    @allure.title("Вопрос о продлении аренды")
    def test_prolongation_rent(self, browser_mozilla):
        page = MainPage(browser_mozilla)
        page.open()
        page.prolongation_rent()
        assert "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010." \
               in browser_mozilla.find_element(
            *MainPageLocators.answer_prolongation_rent).text

    @allure.title("Вопрос о зарядке для самоката")
    def test_charger_with_scooter(self, browser_mozilla):
        page = MainPage(browser_mozilla)
        page.open()
        page.charger_with_scooter()
        assert "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься " \
               "без передышек и во сне. Зарядка не понадобится." in browser_mozilla.find_element(
            *MainPageLocators.answer_charger_with_scooter).text

    @allure.title("Вопрос о отмене заказа")
    def test_cancel_order(self, browser_mozilla):
        page = MainPage(browser_mozilla)
        page.open()
        page.cancel_order()
        assert "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои." \
               in browser_mozilla.find_element(
            *MainPageLocators.answer_cancel_order).text

    @allure.title("Вопрос о заМКАДье")
    def test_behind_MKAD(self, browser_mozilla):
        page = MainPage(browser_mozilla)
        page.open()
        page.behind_MKAD()
        assert "Да, обязательно. Всем самокатов! И Москве, и Московской области." in browser_mozilla.find_element(
            *MainPageLocators.answer_behind_MKAD).text
