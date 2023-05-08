import allure
import pytest

from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.urls import DataUrls
from data.data import TextData, RentalData
from data.data import ConsumerData

@pytest.mark.usefixtures("driver", "get_phone_number", "get_date_today", "get_date_tomorrow")
class TestOrderButton:
    @allure.title('Оформление заказа по кнопке "Заказать" в шапке страницы')
    @allure.description('Корректное заполнение всех полей заказа,'
                        ' после подтверждения отображается {TextData.SUCCESSFUL_ORDER_TEXT}')
    def test_order_button_on_header_passed(self, driver, get_phone_number, get_date_today):
        page = BasePage(driver)
        page.open_page(DataUrls.MAIN_PAGE)
        click_order_button = MainPage(driver)
        click_order_button.click_order_button_in_header()
        order = OrderPage(driver)
        order.filling_form(ConsumerData.CONSUMER_1, get_phone_number)
        order.wait_for_rent_form()
        order.input_rental_information(get_date_today, RentalData.RENTALDATA_1)
        order.wait_for_confirm()
        order.click_confirmation_order()
        order_title = order.get_new_order_title()
        order.wait_for_order_completed()

        assert TextData.SUCCESSFUL_ORDER_TEXT in order_title

    @allure.title('Оформление заказа по кнопке "Заказать" на главной странице')
    @allure.description('Корректное заполнение всех полей заказа,'
                        ' после подтверждения отображается {TextData.SUCCESSFUL_ORDER_TEXT}')
    def test_order_page_correct_user_data_passed(self, driver, get_phone_number, get_date_tomorrow):
        page = BasePage(driver)
        page.open_page(DataUrls.MAIN_PAGE)
        click_order_button = MainPage(driver)
        click_order_button.click_order_button_in_header()
        order = OrderPage(driver)
        order.filling_form(ConsumerData.CONSUMER_2, get_phone_number)
        order.wait_for_rent_form()
        order.input_rental_information(get_date_tomorrow, RentalData.RENTALDATA_2)
        order.wait_for_confirm()
        order.click_confirmation_order()
        order_title = order.get_new_order_title()
        order.wait_for_order_completed()

        assert TextData.SUCCESSFUL_ORDER_TEXT in order_title

    @allure.title('Оформление заказа с некорректными данными по кнопке "Заказать" на главной странице')
    @allure.description('Некорректное Имя пользователя')
    def test_order_page_first_name_incorrect_show_error_message_failed(self, driver, get_phone_number):
        page = BasePage(driver)
        page.open_page(DataUrls.MAIN_PAGE)
        click_order_button = MainPage(driver)
        click_order_button.click_order_button_in_header()
        order = OrderPage(driver)
        order.filling_form(ConsumerData.CONSUMER_3, get_phone_number)
        firstname_error_text = order.wait_for_error_message_firstname()

        assert firstname_error_text == TextData.FIRSTNAME_ERROR

    @allure.title('Оформление заказа с некорректными данными по кнопке "Заказать" на главной странице')
    @allure.description('Некорректная Фамилия пользователя')
    def test_order_page_last_name_incorrect_show_error_message_failed(self, driver, get_phone_number):
        page = BasePage(driver)
        page.open_page(DataUrls.MAIN_PAGE)
        click_order_button = MainPage(driver)
        click_order_button.click_order_button_in_header()
        order = OrderPage(driver)
        order.filling_form(ConsumerData.CONSUMER_4, get_phone_number)
        lastname_error_text = order.wait_for_error_message_lastname()

        assert lastname_error_text == TextData.LASTNAME_ERROR

    @allure.title('Оформление заказа с некорректными данными по кнопке "Заказать" на главной странице')
    @allure.description('Некорректный адрес пользователя')
    def test_order_page_address_incorrect_show_error_message_failed(self, driver, get_phone_number):
        page = BasePage(driver)
        page.open_page(DataUrls.MAIN_PAGE)
        click_order_button = MainPage(driver)
        click_order_button.click_order_button_in_header()
        order = OrderPage(driver)
        order.filling_form(ConsumerData.CONSUMER_5, get_phone_number)
        address_error_text = order.wait_for_error_message_address()

        assert address_error_text == TextData.ADDRESS_ERROR

    @allure.title('Оформление заказа с некорректными данными по кнопке "Заказать" на главной странице')
    @allure.description('Некорректный номер телефона пользователя')
    def test_order_page_phone_number_incorrect_show_error_message_failed(self, driver, get_incorrect_phone_number):
        page = BasePage(driver)
        page.open_page(DataUrls.MAIN_PAGE)
        click_order_button = MainPage(driver)
        click_order_button.click_order_button_in_header()
        order = OrderPage(driver)
        order.filling_form(ConsumerData.CONSUMER_6, get_incorrect_phone_number)
        phonenumber_error_text = order.wait_for_error_message_phonenumber()

        assert phonenumber_error_text == TextData.PHONENUMBER_ERROR