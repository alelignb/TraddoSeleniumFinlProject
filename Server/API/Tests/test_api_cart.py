import json
import allure
import jsonpath
import requests

from Server.API.Constants.cart_constants import Cart
from Server.API.Constants.sorting_constants import Sorting


class Test_Cart(Cart):
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Test api for sorting products from low price")
    def test_api_for_sorting_from_lowest(self):
        url = self.add_prod_url
        data = self.add_to_cart
        res = requests.post(url, json=data)
        products = res.json()['err']
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
        assert products == 'not logged in'

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Test api for sorting products from low price")
    def test_api_for_sorting_from_lowest(self):
        url = self.add_prod_url
        data = self.add_to_cart
        res = requests.post(url, json=data)
        products = res.json()['err']
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
        assert products == 'not logged in'
