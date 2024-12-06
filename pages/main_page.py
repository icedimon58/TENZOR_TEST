import allure

from locators.main_page_locators import CONTAKTS_LOCATOR
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Ожидание загрузки страницы")
    def load_page(self):
        self._wait_visability_of_element_loading(CONTAKTS_LOCATOR)

    @allure.step("Клик по элементу 'Контакты'")
    def click_on_element_on_page(self):
        self._click_on_element(CONTAKTS_LOCATOR)


