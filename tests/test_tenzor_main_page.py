import allure

from data import POWER_IN_PEOPLES, ABOUT_URL
from pages.about_page import AboutPage
from pages.main_page import MainPage
from pages.redir_page import RedirectPage
from pages.tensor_page import TensorPage


class TestTenzorMainPage:

    @allure.description('Ищем текст "Сила в людях"')
    @allure.title('Проверка текста на странице')
    def test_find_power_in_people_text_on_tenzor_page(self, page_driver):
        main_page = MainPage(page_driver)
        redir_page = RedirectPage(page_driver)
        tensor_page = TensorPage(page_driver)
        main_page.load_page()
        main_page.click_on_element_on_page()
        redir_page.go_to_contact_page()
        redir_page.go_to_tenzor_page()
        redir_page.switch_window_after_redir()
        tensor_page.find_element_()
        assert tensor_page.get_text() == POWER_IN_PEOPLES

    @allure.description('Проверяем переход на страницу "https://tensor.ru/about"')
    @allure.title('Проверка перехода со страницы Тензор')
    def test_check_redirect_from_additional_link_from_tenzor_page(self, page_driver):
        main_page = MainPage(page_driver)
        redir_page = RedirectPage(page_driver)
        tensor_page = TensorPage(page_driver)
        about_page = AboutPage(page_driver)
        main_page.load_page()
        main_page.click_on_element_on_page()
        redir_page.go_to_contact_page()
        redir_page.go_to_tenzor_page()
        redir_page.switch_window_after_redir()
        tensor_page.find_element_()
        redir_page.go_to_additional()
        about_page.load_page()
        assert about_page.get_url() == ABOUT_URL

    @allure.description('Проверяем, что у фотографий одинаковая высота и ширина. Тест для разрешения 1920х1080')
    @allure.title('Проверка ширины и высоты фотографий')
    def test_check_width_and_heigth_of_photos_on_tenzor_page(self, page_driver):
        main_page = MainPage(page_driver)
        redir_page = RedirectPage(page_driver)
        tensor_page = TensorPage(page_driver)
        about_page = AboutPage(page_driver)
        main_page.load_page()
        main_page.click_on_element_on_page()
        redir_page.go_to_contact_page()
        redir_page.go_to_tenzor_page()
        redir_page.switch_window_after_redir()
        tensor_page.find_element_()
        redir_page.go_to_additional()
        about_page.load_page()
        assert about_page.check_width_and_height()
