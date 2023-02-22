import time
from sqlite3 import ProgrammingError
import allure

from Web.Data.data import Data
from Web.Locators.promotion_locators import Promo_Locators
from selenium.webdriver.common.by import By
from Web.Pages.utilities import Utilities


class PromotionPage(Utilities, Promo_Locators, Data):

    def select_option1(self):
        self._click(self.option1)

    def select_option2(self):
        self._click(self.option2)

    def click_save_button(self):
        self._click(self.save)

    @allure.step
    def product_number_on_page_title(self):
        title2 = self._find(self.page_title2).text.split(" ")
        pro_num = []
        for i in title2:
            if i.isnumeric():
                pro_num.append(int(i))
        return pro_num[0]

    @allure.step
    def check_name_of_products(self):
        wrong_name = []
        for i in range(self.count_number_of_products(self.products_path)):
            location = (By.XPATH, f'/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div['
                                  f'2]/div[3]/a[{i + 1}]/div[1]/div[2]/div[2]/div[1]')
            title1 = self._find(location).text
            self._click(location)
            title2 = self._find(self.product_title).text
            if title1 != title2:
                wrong_name.append(title1)
                self.record_to_sql(*self.naming_query, title1, title2)
            self._driver.back()
            time.sleep(2)
        return len(wrong_name)

    @allure.step
    def check_that_there_is_no_duplicated_products(self):
        products = self._find_elements(self.products_path)
        product_list = []
        for i in range(len(products)):
            location = (By.XPATH, f'/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div['
                                  f'2]/div[3]/a[{i + 1}]/div[1]/div[2]/div[2]/div[1]')
            title1 = self._find(location).text
            product_list.append(title1)
        len(product_list)
        if len(product_list) == len(set(product_list)):
            return True
        else:
            return False

    @allure.step
    def adding_products(self):
        count_on_cart = 0
        products = self._find_elements(self.products_path)
        for i in range(len(products)):
            location = (By.XPATH, f'/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div['
                                  f'2]/div[3]/a[{i + 1}]/div[1]/div[2]/div[2]/div[1]')
            self._click(location)
            self._click(self.add_icon)
            count_on_cart = int(self._find(self.cart_counter).text)
            count_on_cart += 1
            self._driver.back()
        return count_on_cart

    @allure.step
    def expected_product_number(self):
        products = self._find_elements(self.products_path)
        return len(products)

    @allure.step
    def price_checking(self):
        products = self._find_elements(self.products_path)
        incorrect_price = []
        for i in range(len(products)):
            location = (By.XPATH, f'//body/div[@id="root"]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div['
                                  f'2]/div[3]/a[{i+1}]/div[1]/div[2]/div[2]/div[1]')
            bolded = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div["
                                f"3]/a[{i+1}]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/span[1]/span[1]")
            unbolded = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[3]/a["
                                  f"{i+1}]/div[1]/div[2]/div[2]/div[3]/span[2]")
            product_name = self._find(location).text
            price1, price2 = self.extracted_num(bolded), self.extracted_num(unbolded)
            try:
                if price1 != price2:
                    incorrect_price.append(product_name)
                    self.record_to_sql(*self.price_query, product_name, price1)
            except ProgrammingError:
                pass
        return len(incorrect_price)

    @allure.step
    def write_g_on_search_field(self):
        self._entry(self.search_field, self.finding)

    def enter_item_name(self):
        item = self.searched_name
        return item

    @allure.step
    def checking_auto_suggestion_works(self, data):
        check = []
        time.sleep(2)
        search_suggests = self._find_elements(self.suggestions)
        for i, item in enumerate(search_suggests):
            item_name = self._driver.find_element(By.XPATH, f"//header/div[1]/div[1]/div[1]/div[1]/div[1]/a[{i + 1}]/div[1]/div[2]/div[1]").text
            if data in item_name:
                check.append(True)
            else:
                check.append(False)
        if False not in check:
            return True
        else:
            return False

    @allure.step
    def check_search_functionality(self, data):
        for i in data:
            self._entry(self.search_field, i)
            time.sleep(2)
        item_name = self._find(self.searched).text
        return item_name

    @allure.step
    def clicking_the_button(self, locate):
        self._click(locate)
        time.sleep(2)

    @allure.step
    def checking_sorting_options(self):
        sorting_options = self._find_elements(self.sorting_options)
        return len(sorting_options)

    @allure.step
    def check_sorting_with_from_lowest_price(self):
        products = self._find_elements(self.products_path)
        for i in range(len(products)):
            first_order = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div["
                                f"3]/a[{i + 1}]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/span[1]/span[1]")
            second_order = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div["
                                f"3]/a[{i + 2}]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/span[1]/span[1]")
            if self.extracted_num(first_order) > self.extracted_num(second_order):
                return False

    @allure.step
    def check_header_bars(self):
        links = []
        number_of_bars = self._find_elements(self.bars)
        for i in number_of_bars:
            links.append(i.text)
        return links

    @allure.step
    def checking_unit_price_on_database(self):
        wrong_prices = []
        products = self._find_elements(self.products_path)
        for i in range(len(products)):
            unit_price = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[3]/a["
                                  f"{i+1}]/div[1]/div[2]/div[2]/div[3]/span[2]")
            location = (By.XPATH, f'//body/div[@id="root"]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div['
                                  f'2]/div[3]/a[{i + 1}]/div[1]/div[2]/div[2]/div[1]')
            product_name = self._find(location).text
            price_on_web = round(float(self.extracted_num(unit_price)), 2)
            db_price = float(self.retrive_products(product_name)['price'])
            if price_on_web != db_price:
                wrong_prices.append({product_name: {price_on_web: db_price}})
        return wrong_prices
