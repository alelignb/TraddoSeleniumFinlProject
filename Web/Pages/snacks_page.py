import time
import allure
from selenium.webdriver.common.by import By
import re

from Web.Data.data import Data
from Web.Locators.snacks_locators import SnackLocators
from Web.Pages.utilities import Utilities


class SnacksPage(Utilities, SnackLocators, Data):
    def select_option1(self):
        self._click(self.option1)

    def select_option2(self):
        self._click(self.option2)

    def click_save_button(self):
        self._click(self.save)

    @allure.step
    def clicking_snacks_link(self):
        self._click(self.snacks_link)
        time.sleep(2)

    @allure.step
    def product_number_on_page_title(self):
        title2 = self._find(self.page_title2).text.split(" ")
        pro_num = []
        for i in title2:
            if i.isnumeric():
                pro_num.append(int(i))
        return pro_num[0]

    @allure.step
    def expected_product_number(self):
        title2 = self._find(self.page_title2).text.split(" ")
        pro_num = []
        for i in title2:
            if i.isnumeric():
                pro_num.append(int(i))
        return pro_num[0]

    @allure.step
    def color(self, location):
        element_color = self._find(location).value_of_css_property("background-color")
        return element_color

    @allure.step
    def check_that_there_is_no_duplicated_products(self):
        products = self._find_elements(self.products_path)
        product_list = []
        for i in range(len(products)):
            location = (By.XPATH, f"//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div["
                                  f"2]/div[2]/a[{i+1}]/div[1]/div[2]/div[2]/div[1]")
            title1 = self._find(location).text
            product_list.append(title1)
        len(product_list)
        if len(product_list) == len(set(product_list)):
            return True
        else:
            return False

    @allure.step
    def price_checking(self):
        products = self._find_elements(self.products_path)
        incorrect_price = []
        for i in range(len(products)):
            location = (By.XPATH, f'/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div['
                                  f'2]/div[3]/a[{i + 1}]/div[1]/div[2]/div[2]/div[1]')
            bolded = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div["
                                f"3]/a[{i+1}]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/span[1]/span[1]")
            unbolded = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[3]/a["
                                  f"{i+1}]/div[1]/div[2]/div[2]/div[3]/span[2]")
            pr1 = self._find(bolded).text
            pr1_num = re.findall("\d+\.\d+", f"Current Level: {pr1}")
            pr2_str = self._find(unbolded).text
            pr2_num = re.findall("\d+\.\d+", f"Current Level: {pr2_str}")
            product_name = self._find(location).text
            if pr1_num[0] != pr2_num[0]:
                incorrect_price.append(product_name)
        return incorrect_price

    @allure.step
    def write_g_on_search_field(self):
        entry = self.searchhh_dataa
        return entry

    @allure.step
    def checking_font_size(self, location):
        return self._find(location).value_of_css_property("font-size")

    @allure.step
    def checking_font_weight(self, location):
        return self._find(location).value_of_css_property("font-weight")

    @allure.step
    def clicking_the_button(self, locate):
        self._click(locate)

    @allure.step
    def checking_sorting_options(self):
        sorting_options = self._find_elements(self.sorting_options)
        return len(sorting_options)

    @allure.step
    def text_reading(self, locate):
        return self._find(locate).text

    @allure.step
    def click_all_products(self):
        products = self._find_elements(self.products_path)
        for i in range(len(products)):
            location = (By.XPATH, f'/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div['
                                  f'2]/div[2]/a[{i+1}]/div[1]/div[2]/div[2]/div[1]')
            title1 = self._find(location).text
            self._click(location)
            title2 = self._find(self.product_title).text
            assert title1 == title2
            self._driver.back()
            time.sleep(2)

    @allure.step
    def check_sorting_with_from_lowest_price(self):
        products = self._find_elements(self.products_path)
        incorrect_order = []
        for i in range(len(products)-1):
            first_order = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div["
                                     f"2]/div[2]/a[{i+1}]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/span[1]/span[1]")
            second_order = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div["
                                     f"2]/div[2]/a[{i+2}]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/span[1]/span[1]")
            pr1 = self._find(first_order).text
            pr2 = self._find(second_order).text
            pr1_num = re.findall("\d+\.\d+", f"Current Level: {pr1}")
            pr2_num = re.findall("\d+\.\d+", f"Current Level: {pr2}")
            if pr1_num > pr2_num:
                incorrect_order.append(False)
        return len(incorrect_order)





