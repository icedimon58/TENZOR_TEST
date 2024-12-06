import allure

from data import SITY, SITY_CHANGE, SITY_CHANGE_URL
from pages.main_page import MainPage
from pages.redir_page import RedirectPage
from pages.contacts_page import ContasctPage


class TestContactsPage:

    @allure.description('Меняем регион и проверяем, что он корректно изменился')
    @allure.title('Проверка изменения города после смены региона')
    def test_check_change_sity_name_after_change_region(self, page_driver):
        main_page = MainPage(page_driver)
        redir_page = RedirectPage(page_driver)
        contact_page = ContasctPage(page_driver)
        main_page.load_page()
        main_page.click_on_element_on_page()
        redir_page.go_to_contact_page()
        contact_page.change_sity()
        contact_page.wait_update_page()
        assert SITY_CHANGE in contact_page.get_text_sity() and contact_page.get_clients_counts() > 0

    @allure.description('Меняем регион и проверяем, что изменились клиенты и их количество')
    @allure.title('Проверка изменения клиентов после смены региона')
    def test_check_change_clients_after_change_region(self, page_driver):
        main_page = MainPage(page_driver)
        redir_page = RedirectPage(page_driver)
        contact_page = ContasctPage(page_driver)
        main_page.load_page()
        main_page.click_on_element_on_page()
        redir_page.go_to_contact_page()
        contact_page.change_sity()
        contact_page.wait_update_page()
        assert SITY_CHANGE in contact_page.get_text_sites_clients() and contact_page.get_clients_counts() > 0

    @allure.description('Меняем регион и проверяем, что он корректно изменился')
    @allure.title('Проверка изменения URL-страницы после смены региона')
    def test_check_change_page_url_after_change_region(self, page_driver):
        main_page = MainPage(page_driver)
        redir_page = RedirectPage(page_driver)
        contact_page = ContasctPage(page_driver)
        main_page.load_page()
        main_page.click_on_element_on_page()
        redir_page.go_to_contact_page()
        contact_page.change_sity()
        contact_page.wait_update_page()
        assert SITY_CHANGE_URL in contact_page.get_page_url()

    @allure.description('Ищем название города на странице')
    @allure.title('Проверка названия города')
    def test_check_my_sity_name(self, page_driver):
        main_page = MainPage(page_driver)
        redir_page = RedirectPage(page_driver)
        contact_page = ContasctPage(page_driver)
        main_page.load_page()
        main_page.click_on_element_on_page()
        redir_page.go_to_contact_page()
        assert SITY in contact_page.get_text_sity()

    @allure.description('Ищем клиентов в регионе')
    @allure.title('Проверка клиентов города')
    def test_check_my_sity_clients(self, page_driver):
        main_page = MainPage(page_driver)
        redir_page = RedirectPage(page_driver)
        contact_page = ContasctPage(page_driver)
        main_page.load_page()
        main_page.click_on_element_on_page()
        redir_page.go_to_contact_page()
        assert SITY in contact_page.get_text_sites_clients() and contact_page.get_clients_counts() > 0
