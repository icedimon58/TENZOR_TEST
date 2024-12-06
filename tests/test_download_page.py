import allure
from pages.main_page import MainPage
from pages.redir_page import RedirectPage
from pages.download_page import DowloadPage


class TestDownloadPage:
    @allure.description('Сравниваем размер скаченного файла с указанным на сайте')
    @allure.title('Скачиваем дистрибутив')
    def test_load_page(self, page_driver):
        main_page = MainPage(page_driver)
        redir_page = RedirectPage(page_driver)
        software_page = DowloadPage(page_driver)
        main_page.load_page()
        redir_page.go_to_download_page()
        assert software_page.download_installer() == software_page.get_size_from_text()
