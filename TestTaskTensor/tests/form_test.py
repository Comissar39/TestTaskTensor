from pages.about_page import AboutPage
from pages.contacts_page import ContactsPage
from tests.conftest import driver


class TestFormPage:

    def test_scenario_1(self, driver):
        about_page = AboutPage(driver, 'https://tensor.ru/about')
        about_page.open()
        attributes = about_page.check_height_and_width()
        if attributes[0:1] == attributes[2:3] == attributes[4:5] == attributes[6:7]:
            print('image1 == image2 == image3 == image4 is TRUE')
            print('Сценарий 1 проверку прошёл!')
        else:
            print('image1 == image2 == image3 == image4 is FALSE')
            print('Сценарий 1 проверку НЕ прошёл!')

    def test_scenario_2(self, driver):
        contacts_page = ContactsPage(driver, 'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients')
        contacts_page.open()
        attributes = contacts_page.check_partners_list()
        if attributes[0] == 'Камчатский край':
            span1 = bool(1)
            print("span1 == 'Камчатский край' is TRUE")
        else:
            span1 = bool(0)
            print("span1 == 'Камчатский край' is FALSE")
        if attributes[1] == "СБИС - Камчатка":
            div1 = bool(1)
            print("div1 == 'СБИС - Камчатка' is TRUE")
        else:
            div1 = bool(0)
            print("div1 == 'СБИС - Камчатка' is FALSE")
        if attributes[2] == 'mailto:info@kamchatka.tensor.ru':
            a1 = bool(1)
            print("a1 == 'mailto:info@kamchatka.tensor.ru' is TRUE")
        else:
            a1 = bool(0)
            print("a1 == 'mailto:info@kamchatka.tensor.ru' is FALSE")
        if span1 == div1 == a1 == 1:
            print('Сценарий 2 проверку прошёл!')
        else:
            print('Сценарий 2 проверку НЕ прошёл!')
