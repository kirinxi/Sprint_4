import allure
from selenium.webdriver.support import expected_conditions as exp_cond
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys

class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    def set_first_name(self, firstname):
        self.driver.find_element(*OrderPageLocators.NAME_FIELD).send_keys(firstname)

    def set_last_name(self, lastname):
        self.driver.find_element(*OrderPageLocators.LAST_NAME_FIELD).send_keys(lastname)

    def set_address(self, address):
        self.driver.find_element(*OrderPageLocators.ADDRESS_FIELD).send_keys(address)

    def set_subway_station(self, station):
        self.driver.find_element(*OrderPageLocators.STATION_FIELD).send_keys(station)
        WebDriverWait(self.driver, 10).until(exp_cond.visibility_of_element_located(OrderPageLocators.STATION_DROPDOWN))
        self.driver.find_element(*OrderPageLocators.STATION_DROPDOWN).click()
        WebDriverWait(self.driver, 10).until(exp_cond.invisibility_of_element(OrderPageLocators.STATION_DROPDOWN))

    def set_phone_number(self, number):
        WebDriverWait(self.driver, 10).until(exp_cond.visibility_of_element_located(OrderPageLocators.PHONE_NUMBER_FIELD))
        self.driver.find_element(*OrderPageLocators.PHONE_NUMBER_FIELD).send_keys(number)

    def click_next_button(self):
        WebDriverWait(self.driver, 10).until(exp_cond.element_to_be_clickable(OrderPageLocators.NEXT_BUTTON))
        self.driver.find_element(*OrderPageLocators.NEXT_BUTTON).click()

    @allure.step('Заполнить поля раздела "Для кого самокат?"')
    def filling_form(self, consumer, number):
        self.set_first_name(consumer.get("firstname"))
        self.set_last_name(consumer.get("lastname"))
        self.set_address(consumer.get("address"))
        self.set_subway_station(consumer.get("subway_station"))
        self.set_phone_number(number)
        self.click_next_button()

    def wait_for_rent_form(self):
        WebDriverWait(self.driver, 10).until(exp_cond.visibility_of_element_located(OrderPageLocators.RENT_FORM))

    def set_date(self, date):
        self.driver.find_element(*OrderPageLocators.DATE_FIELD).send_keys(date)
        WebDriverWait(self.driver, 10).until(exp_cond.visibility_of_element_located(OrderPageLocators.CALENDAR))
        self.driver.find_element(*OrderPageLocators.DATE_FIELD).send_keys(Keys.ENTER)
        WebDriverWait(self.driver, 10).until(exp_cond.invisibility_of_element(OrderPageLocators.CALENDAR))

    def select_rental_period(self, period):
        self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD).click()
        WebDriverWait(self.driver, 10).until(exp_cond.visibility_of_element_located(OrderPageLocators.RENTAL_PERIOD_DROPDOWN))
        self.driver.find_element(*period).click()
        WebDriverWait(self.driver, 10).until(exp_cond.invisibility_of_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN))

    def click_checkbox(self, color):
        self.driver.find_element(*color).click()

    def set_comment(self, comment):
        self.driver.find_element(*OrderPageLocators.COMMENT_FIELD).send_keys(comment)

    def click_order_button(self):
        WebDriverWait(self.driver, 10).until(exp_cond.element_to_be_clickable(OrderPageLocators.ORDER_BUTTON))
        self.driver.find_element(*OrderPageLocators.ORDER_BUTTON).click()

    @allure.step('Заполнить раздел "Про аренду"')
    def input_rental_information(self, date, rental_data):
        color_checkbox = {"black": OrderPageLocators.BLACK_CHECKBOX, "grey": OrderPageLocators.GREY_CHECKBOX}
        day_period = {"one": OrderPageLocators.ONE_DAY, "two": OrderPageLocators.TWO_DAY}
        self.set_date(date)
        self.select_rental_period(day_period.get(rental_data.get('rental_period')))
        self.click_checkbox(color_checkbox.get(rental_data.get('scooter_color')))
        self.set_comment(rental_data.get('comment'))
        self.click_order_button()

    def wait_for_confirm(self):
        WebDriverWait(self.driver, 10).until(exp_cond.visibility_of_element_located(OrderPageLocators.CONFIRM))

    @allure.step('Клик по кнопке "Да" в диалоге подтверждения')
    def click_confirmation_order(self):
        self.driver.find_element(*OrderPageLocators.YES_BUTTON).click()

    def wait_for_order_completed(self):
        WebDriverWait(self.driver, 10).until(exp_cond.visibility_of_element_located(OrderPageLocators.ORDER_COMPLETED))

    @allure.step('Получить текст диалога успешного заказа')
    def get_new_order_title(self):
        new_order_text = self.driver.find_element(*OrderPageLocators.ORDER_COMPLETED).text
        return new_order_text

    def click_order_status_button(self):
        self.driver.find_element(*OrderPageLocators.ORDER_STATUS_BUTTON).click()

    @allure.step('Получить текст ошибки при вводе некорректного имени')
    def wait_for_error_message_firstname(self):
        WebDriverWait(self.driver, 10).until(exp_cond.visibility_of_element_located(OrderPageLocators.INCORRECT_FIRST_NAME_MESSAGE))
        firstname_error_text = self.driver.find_element(*OrderPageLocators.INCORRECT_FIRST_NAME_MESSAGE).text
        return firstname_error_text

    @allure.step('Получить текст ошибки при вводе некорректной фамилии')
    def wait_for_error_message_lastname(self):
        WebDriverWait(self.driver, 10).until(exp_cond.visibility_of_element_located(OrderPageLocators.INCORRECT_LAST_NAME_MESSAGE))
        lastname_error_text = self.driver.find_element(*OrderPageLocators.INCORRECT_LAST_NAME_MESSAGE).text
        return lastname_error_text

    @allure.step('Получить текст ошибки при вводе некорректного адреса')
    def wait_for_error_message_address(self):
        WebDriverWait(self.driver, 10).until(
            exp_cond.visibility_of_element_located(OrderPageLocators.INCORRECT_ADDRESS_MESSAGE))
        address_error_text = self.driver.find_element(*OrderPageLocators.INCORRECT_ADDRESS_MESSAGE).text
        return address_error_text

    @allure.step('Получить текст ошибки при вводе некорректного номера телефона')
    def wait_for_error_message_phonenumber(self):
        WebDriverWait(self.driver, 10).until(
            exp_cond.visibility_of_element_located(OrderPageLocators.INCORRECT_PHONENUMBER_MESSAGE))
        phonenumber_error_text = self.driver.find_element(*OrderPageLocators.INCORRECT_PHONENUMBER_MESSAGE).text
        return phonenumber_error_text

