from selenium.webdriver.common.by import By

from data import REGION_TO_FIND

OBLAST_PAGE_LOCATOR = By.XPATH, "//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link']"

SITY_LOCATOR = By.ID, 'city-id-2'

CLIENTS_LOCATOR = By.XPATH, "//div[@class='sbisru-Contacts-List__name sbisru-Contacts-List--ellipsis sbisru-Contacts__text--md pb-4 pb-xm-12 pr-xm-32']"

REGION_CHANGE_FIELD_LOCATOR = By.XPATH, "//input"

CLICK_ON_FIND_REGION = By.XPATH, f"//ul[@class='sbis_ru-Region-Panel__list-l']/li[@tabindex=0]/span[@title='{REGION_TO_FIND}']"

CHANGE_REGION_WINDOW = By.XPATH, "//div[@name='dialog']"
