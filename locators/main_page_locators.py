from selenium.webdriver.common.by import By

class MainPageLocators:
    HEADER_TEXT = By.XPATH, \
        "//div[contains(@class, 'Home_Header')]"  # Заголовок на главной странице
    HEADER_ORDER_BUTTON = \
        By.XPATH, "//*[contains(@class, 'Header_Nav')]/button[text()='Заказать']" # Кнопка "Заказать" в шапке
    ORDER_BUTTON_IN_HEADER = By.XPATH, \
        "//*[contains(@class, 'Header_Nav')]/button[text()='Заказать']" # Кнопка "Заказать" в шапке
    FAQ = By.XPATH, \
        "//div[contains(@class, 'Home_FAQ_')]"  # Раздел "Вопросы о важном"
    QUESTIONS = By.XPATH, \
        "//div[contains(@class, 'accordion__item')]"  # Вопросы
    ANSWER = By.XPATH,\
        "//div[contains(@class, 'accordion__panel') and not(@hidden)]"  # Отображаемый ответ
    COOKIES_BUTTON = By.XPATH, \
        "//button[contains(@class, 'App_CookieButton_')]"  # Кнопка "Да все привыкли"
    ORDER_BUTTON_MAIN_PAGE = By.XPATH, \
        "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']" # Кнопка "Заказать" на странице