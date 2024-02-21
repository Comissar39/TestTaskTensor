from pages.base_page import BasePage
from locators.about_page_locators import AboutPageLocators as Locators


class AboutPage(BasePage):

    def check_height_and_width(self):
        img_width_1 = self.element_is_visible(Locators.IMG_1).get_attribute("width")
        img_width_2 = self.element_is_visible(Locators.IMG_2).get_attribute("width")
        img_width_3 = self.element_is_visible(Locators.IMG_3).get_attribute("width")
        img_width_4 = self.element_is_visible(Locators.IMG_4).get_attribute("width")
        img_height_1 = self.element_is_visible(Locators.IMG_1).get_attribute("height")
        img_height_2 = self.element_is_visible(Locators.IMG_2).get_attribute("height")
        img_height_3 = self.element_is_visible(Locators.IMG_3).get_attribute("height")
        img_height_4 = self.element_is_visible(Locators.IMG_4).get_attribute("height")
        return (img_width_1, img_height_1, img_width_2, img_height_2,
                img_width_3, img_height_3, img_width_4, img_height_4)
