class ConsumerData:

    CONSUMER_1 = {
	    'firstname': 'Ирина',
	    'lastname': 'Горбачева',
	    'address': 'Ленинградское ш., 5',
        'subway_station': 'Водный стадион',
    }

    CONSUMER_2 = {
	    'firstname': 'Максим',
	    'lastname': 'Иванов',
	    'address': 'Проспект Мира, 12',
        'subway_station': 'Проспект Мира',
    }

    CONSUMER_3 = {
	    'firstname': 'I',
	    'lastname': 'Петров',
	    'address': 'Проспект Мира, 12',
	    'subway_station': 'Проспект Мира',
    }

    CONSUMER_4 = {
	    'firstname': 'Иван',
	    'lastname': '  ',
	    'address': 'Проспект Мира, 12',
	    'subway_station': 'Проспект Мира',
    }

    CONSUMER_5 = {
	    'firstname': 'Иван',
	    'lastname': 'Сидоров',
	    'address': '12',
	    'subway_station': 'Проспект Мира',
    }

    CONSUMER_6 = {
	    'firstname': 'Иван',
	    'lastname': 'Сидоров',
	    'address': 'Мира пр., 12',
	    'subway_station': 'Проспект Мира',
    }


class RentalData:

		RENTALDATA_1 = {
			'rental_start_date': '12.05.2023',
			'rental_period': "one",
			'scooter_color': 'black',
			'comment': 'Позвонить за полчаса'
		}

		RENTALDATA_2 = {
			'rental_start_date': '10.01.2024',
			'rental_period': "two",
			'scooter_color': 'grey',
			'comment': 'Не звонить!'
		}

class YandexScooterQuestions:
    QUESTIONS_LIST = [
        (1, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
        (2, "Пока что у нас так: один заказ — один самокат."
            " Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
        (3, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня."
            " Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру."
            " Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
        (4, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
        (5, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
        (6, "Самокат приезжает к вам с полной зарядкой."
            " Этого хватает на восемь суток — даже если будете кататься без передышек и во сне."
            " Зарядка не понадобится."),
        (7, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
        (8, "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
    ]

class YandexScooterAnswers:
    answer1 = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
    answer2 = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
    answer3 = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
    answer4 = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
    answer5 = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
    answer6 = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
    answer7 = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
    answer8 = "Да, обязательно. Всем самокатов! И Москве, и Московской области."

class TextData:
    HEADER_TEXT = 'Самокат\nна пару дней\nПривезём его прямо к вашей двери,\nа когда накатаетесь — заберём'
    SUCCESSFUL_ORDER_TEXT = 'Заказ оформлен'
    FIRSTNAME_ERROR = 'Введите корректное имя'
    LASTNAME_ERROR = 'Введите корректную фамилию'
    ADDRESS_ERROR = 'Введите корректный адрес'
    PHONENUMBER_ERROR = 'Введите корректный номер'
