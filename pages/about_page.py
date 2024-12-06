import allure

from data import ICON_HEIGTH, ICON_WIDTH
from locators.about_page_locator import TEXT_ABOUT_PAGE_LOCATOR, ABOUT_PAGE_ICON

from pages.base_page import BasePage


class AboutPage(BasePage):
    @allure.step("Ожидание загрузки страницы")
    def load_page(self):
        self._wait_visability_of_element_loading(TEXT_ABOUT_PAGE_LOCATOR)

    @allure.step("Проверка ширины и высоты фотографий")
    def check_width_and_height(self):
        element = self._find_elements(ABOUT_PAGE_ICON)
        for i in element:
            if (i.get_attribute('height') != ICON_HEIGTH
                    or i.get_attribute('width') != ICON_WIDTH):
                return False
        return True

    @allure.step("Получаем URL страницы")
    def get_url(self):
        return self._get_page_url()
