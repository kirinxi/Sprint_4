# Sprint_4

## Проект автотестов для сервиса "Яндекс Самокат"

1. Фреймворк - Selenium
2. Браузер - Firefox
3. Запуск всех тестов: pytest -v tests
4. Сгенерировать Allure-отчёт: pytest tests --alluredir=allure_results 
5. Сформировать отчёт в формате веб: allure serve allure_results 

## Сценарии, покрытые тавтотестами:
* test_base_page.py - Основные переходы по логотипам со страниц
* test_main_page.py - Проверка Вопросов и Ответов на Главной странице
* test_order_page.py - Страница и заполнение Заказа

## Test Cases:
### Тесты на переходы по логотипам
#### class TestLogo
1. test_main_page_open_by_scooter_logo_passed - проверяет, что по лого 
    "Самокат" переходим на Главную страницу;
2. test_dzen_page_open_by_yandex_logo_passed - проверяет, что по лого
    "Яндекс" переходит на ресурс Я.Дзен.

### Тест проверяет Вопросы и ответы в разделе "Вопросы о важном"
#### TestQuestions

1. test_get_answer_on_question_FAQ_passed - проверяет, что вопросу 
    соотвествует корректный ответ.

### Тест страницы заказа и заполнение формы заказа
#### TestOrderButton

1. test_order_button_on_header_passed - проверяет переход на страницу 
    с формой заказа из шапки страницы;
2. test_order_page_correct_user_data_passed - проверяет корректность 
    заполненных данных и сообщение об успешно созданном заказе;
3. test_order_page_first_name_incorrect_show_error_message_failed - проверяет
    ошибку некорректно введённого имени пользователя;
4. test_order_page_last_name_incorrect_show_error_message_failed - проверяет
    ошибку некорректно введённой фамилии пользователя;
5. test_order_page_address_incorrect_show_error_message_failed - проверяет
    ошибку некорректно введённого адреса;
7. test_order_page_phone_number_incorrect_show_error_message_failed - проверяет
    ошибку некорректно введённого телефона

# Спасибо за внимание! :)
