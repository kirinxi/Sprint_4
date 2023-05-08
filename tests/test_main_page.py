import allure
import pytest
from pages.main_page import MainPage
from pages.base_page import BasePage
from data.data import YandexScooterQuestions
from data.urls import DataUrls

@pytest.mark.usefixtures("driver")
class TestQuestions:

    @allure.title('Выпадающий список вопросов-ответов в разделе "Вопросы о важном"')
    @allure.description('На главной странице перейти к разделу FAQ, нажать на вопрос,'
                        'проверяем, что открывается корректный ответ.')
    @pytest.mark.parametrize("index,text", YandexScooterQuestions.QUESTIONS_LIST)
    def test_get_answer_on_question_FAQ_passed(self, driver, index, text):
        page = BasePage(driver)
        page.open_page(DataUrls.MAIN_PAGE)
        questions = MainPage(driver)
        questions.scroll_to_questions()
        questions.click_on_question(index)
        answer = questions.get_answer_text()
        questions.wait_for_get_answer()
        assert answer == text