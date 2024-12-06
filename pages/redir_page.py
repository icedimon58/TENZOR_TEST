import allure

from locators.redir_page_locators import CONTACTS_REDIR_LOCATOR, TENZOR_REDIR_LOCATOR, TENZOR_ABOUT_LOCATOR, \
    DOWNLOAD_PAGE_LOCATOR
from pages.base_page import BasePage


class RedirectPage(BasePage):

    @allure.step("Переход на страницу Контакты")
    def go_to_contact_page(self):
        self._wait_visability_of_element_loading(CONTACTS_REDIR_LOCATOR)
        self._click_on_element(CONTACTS_REDIR_LOCATOR)

    @allure.step("Переход на страницу Тензор")
    def go_to_tenzor_page(self):
        self._wait_visability_of_element_loading(TENZOR_REDIR_LOCATOR)
        self._click_on_element(TENZOR_REDIR_LOCATOR)

    @allure.step("Переход на страницу Загрузки")
    def go_to_download_page(self):
        self._wait_visability_of_element_loading(DOWNLOAD_PAGE_LOCATOR)
        self._click_on_element(DOWNLOAD_PAGE_LOCATOR)

    @allure.step("Переход на страницу О компании")
    def go_to_additional(self):
        self._wait_visability_of_element_loading(TENZOR_ABOUT_LOCATOR)
        self._click_on_element(TENZOR_ABOUT_LOCATOR)

    @allure.step("Переключаем драйвер на новое окно")
    def switch_window_after_redir(self):
        self._switch_window()
