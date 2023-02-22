import datetime
import re

import allure
from pymongo import MongoClient
import pyodbc
from Web.BasePage.basepage import BasePage
import string
import random


class Utilities(BasePage):

    def extracted_num(self, price):
        string = self._find(price).text
        num = re.findall("\d+\.\d+", f"Current Level: {string}")
        return num[0]

    def total_price_calc(self, locate1):
        initial_price = float(self.extracted_num(locate1))
        tax = 0.169892473
        total_price = round(tax * initial_price, 2) + initial_price
        return total_price

    @allure.step
    def checking_font_size(self, location):
        return self._find(location).value_of_css_property("font-size")

    @allure.step
    def checking_font_weight(self, location):
        return self._find(location).value_of_css_property("font-weight")

    @allure.step
    def checking_text_align(self, location):
        return self._find(location).value_of_css_property("text-align")

    @allure.step
    def color(self, location):
        element_color = self._find(location).value_of_css_property("background-color")
        return element_color

    @allure.step
    def text_color(self, locate):
        element_color = self._find(locate).value_of_css_property("color")
        return element_color

    @allure.step
    def frame_width(self, locate):
        width = self._find(locate).value_of_css_property("width")
        return width

    @allure.step
    def count_number_of_products(self, locate):
        self._wait_until_element_is_visible(locate)
        products = self._find_elements(locate)
        return len(products)

    @allure.step
    def switching_window(self):
        parent_window = self._driver.current_window_handle
        all_windows = self._driver.window_handles
        for window in all_windows:
            if window != parent_window:
                self._driver.switch_to.window(window)

    def random_name(self):
        word = ""
        for i in range(7):
            l = random.choices(string.ascii_letters)[0]
            word = l + word
        return word

    def login_code(self, phone):
        connect = MongoClient(
            "mongodb+srv://qa_agency:veHt1JK5@cluster0.qnr3p.mongodb.net/trado_qa?retryWrites=true&w=majority")
        db = connect.trado_qa
        col = db.users
        cur = col.find_one({"phone": phone})['loginCode']
        return cur

    def code_for_register(self, id_no):
        connect = MongoClient(
            "mongodb+srv://qa_agency:veHt1JK5@cluster0.qnr3p.mongodb.net/trado_qa?retryWrites=true&w=majority")
        db = connect.trado_qa
        col = db.users
        cur = col.find_one({"userId": id_no})['loginCode']
        return cur

    @allure.step
    def checking_current_url(self):
        return self._driver.current_url

    def record_to_sql(self, table,col1,col2,col3, value1, value2):
        connect = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL '
                                 'Server};SERVER=MIKE;DATABASE=QA;Trusted_Connection=yes;')
        cursor = connect.cursor()
        cursor.execute(f"insert into [{table}] ([{col1}],[{col2}],[{col3}]) "
                       "values(?,?,?)", (value1, value2, datetime.datetime.now()))
        cursor.commit()
        cursor.close()
        connect.close()

    def retrive_data(self, phone):
        connect = MongoClient(
            "mongodb+srv://qa_agency:veHt1JK5@cluster0.qnr3p.mongodb.net/trado_qa?retryWrites=true&w=majority")
        db = connect.trado_qa
        col = db.users
        cur = col.find_one({"phone": f'{phone}'})
        return cur

    def retrive_products(self, name):
        connect = MongoClient(
            "mongodb+srv://qa_agency:veHt1JK5@cluster0.qnr3p.mongodb.net/trado_qa?retryWrites=true&w=majority")
        db = connect.trado_qa
        col = db.products
        cur = col.find_one({"name": f'{name}'})
        return cur

    def import_from_icloud(self, key1, key2):
        connect = MongoClient("mongodb+srv://admin:mikipassed@cluster0.7xf5de2.mongodb.net/test")
        db = connect.Trado
        col = db.test_data
        cur = col.find_one({key1: 3464024896})[key2]
        return cur











