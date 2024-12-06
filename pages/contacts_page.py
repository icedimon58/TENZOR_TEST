import allure

from data import REGION_TO_FIND
from locators.contacts_page_locator import OBLAST_PAGE_LOCATOR, SITY_LOCATOR, CLIENTS_LOCATOR, \
    REGION_CHANGE_FIELD_LOCATOR, CLICK_ON_FIND_REGION
from pages.base_page import BasePage


class ContasctPage(BasePage):

    @allure.step("Получаем текст региона")
    def get_text_sity(self):
        return self._get_text_from_element(OBLAST_PAGE_LOCATOR)

    @allure.step("Ожидаем когда изменится текст выбранного региона")
    def wait_update_page(self):
        self._wait_text_on_element_change(OBLAST_PAGE_LOCATOR, REGION_TO_FIND)

    @allure.step("Получаем URL страницы")
    def get_page_url(self):
        return self._get_page_url()

    @allure.step("Получаем название города")
    def get_text_sites_clients(self):
        return self._get_text_from_element(SITY_LOCATOR)

    @allure.step("Меняем регион")
    def change_sity(self):
        self._click_on_element(OBLAST_PAGE_LOCATOR)
        self._wait_visability_of_element_loading(REGION_CHANGE_FIELD_LOCATOR)
        self._set_text_to_element(REGION_CHANGE_FIELD_LOCATOR, REGION_TO_FIND)
        self._wait_visability_of_element_loading(CLICK_ON_FIND_REGION)
        self._click_on_element(CLICK_ON_FIND_REGION)

    @allure.step("Получаем количество клиентов в регионе")
    def get_clients_counts(self):
        return len(self._find_elements(CLIENTS_LOCATOR))
