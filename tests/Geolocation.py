from Welcome.conftest import geo
from Welcome.pages.home_page import go_to
from Welcome.pages.Geolocation_page import GeolocationPage


def test_geolocation(geo):
    go_to('Geolocation', geo) # переход на нужную страницу

    geoloc = GeolocationPage(geo) # создаем обьект страницу
    geoloc.click_button() # нажимаем кнопку
    geoloc.wait_for_coordinates() # ждем появления координат

    lat = float(geoloc.get_latitude())
    lon = float(geoloc.get_longitude())

    print(f"\nШирота: {lat}\nДолгота: {lon}")

    assert float(lat - 40.712) < 0.1
    assert float(lon + 74.005) < 0.1


    # geo_link = geo.locator("//a[text()='Geolocation']")
    # assert geo_link.text_content() == 'Geolocation'
    #
    # geo_link.click()
    # geo.wait_for_load_state('networkidle')

    # работаем с геолокацией
    #button_page = geo.locator("//button")
    # assert button_page.text_content() == 'Where am I?'

    #button_page.click()
    #geo.wait_for_selector('#lat-value', state='visible')

    #lat = geo.locator('#lat-value').text_content()
    #lon = geo.locator('#long-value').text_content()

    # print('\nШирота:', lat)
    # print('Долгота', lon)
    #
    # assert float(lat) - 40.712 < 0.1
    # assert float(lon) + 74.005 < 0.1


