
import requests
from bs4 import BeautifulSoup

def test_web():
    #Открыть страницу
    url = 'https://the-internet.herokuapp.com/'
    responses = requests.get(url)

    # Найти заголовок h1
    soup = BeautifulSoup(responses.text, 'html.parser')
    title = soup.find('h1')

    # Получить текст заголовка
    actual_text = title.text

    # Сравнить с ожидаемым
    sravnenie_text = 'Welcome to the-internet'

    assert actual_text == sravnenie_text

    # Найти подзаголовок
    soup = BeautifulSoup(responses.text, 'html.parser')
    title_2 = soup.find('h2')

    # Получить текст подзаголовка
    actual_text_2 = title_2.text

    # Сравнить подзаголовок с ожидаемым
    sravnenie_2_text = 'Available Examples'

    assert actual_text_2 == sravnenie_2_text

