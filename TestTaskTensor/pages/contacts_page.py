from pages.base_page import BasePage
from locators.contacts_page_locators import ContactsPageLocators as Locators


class ContactsPage(BasePage):

    def check_partners_list(self):
        span_1 = self.element_is_visible(Locators.SPAN_1).get_attribute("innerHTML")
        div_1 = self.element_is_visible(Locators.DIV_1).get_attribute("title")
        a_1 = self.element_is_visible(Locators.A_1).get_attribute("href")
        return span_1, div_1, a_1




