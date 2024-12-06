import allure

from locators.tensor_page_locators import TENSOR_TEXT_LOCATOR
from pages.base_page import BasePage


class TensorPage(BasePage):
    @allure.step("Ищем элемент на странице")
    def find_element_(self):
        self._wait_visability_of_element_loading(TENSOR_TEXT_LOCATOR)

    @allure.step("Возвращаем текст элемента")
    def get_text(self):
        return self._get_text_from_element(TENSOR_TEXT_LOCATOR)[:12]

