import allure

from data import PLUGIN_NAME
from locators.software_locators import WEB_INSTALLER, WEB_INSTALLER_LOCATOR
from pages.base_page import BasePage


class DowloadPage(BasePage):

    @allure.step("Возвращаем текст ссылки на скачивание")
    def get_size_from_text(self):
        text = self._get_text_from_element(WEB_INSTALLER_LOCATOR)
        MB = text.find('МБ', 13)
        return text[13:MB-1]

    @allure.step("Загружаем Веб-установщик")
    def download_installer(self):
        return self._download_file(WEB_INSTALLER, PLUGIN_NAME)

