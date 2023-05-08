import allure
from selenium.webdriver.support import expected_conditions as exp_cond
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажимаем на логотип "Яндекс"')
    def click_yandex_logo(self):
        self.driver.find_element(*BasePageLocators.YANDEX_LOGO).click()

    def wait_for_new_tab(self, number):
        WebDriverWait(self.driver, 10).until(exp_cond.number_of_windows_to_be(number))

    def wait_for_page_load(self, url):
        WebDriverWait(self.driver, 20).until(exp_cond.url_to_be(url))

    @allure.step('Нажимаем на логотип "Самокат"')
    def click_scooter_logo(self):
        self.driver.find_element(*BasePageLocators.SCOOTER_LOGO).click()

    @allure.step('Открыть страницу {page}')
    def open_page(self, page):
        self.driver.get(page)