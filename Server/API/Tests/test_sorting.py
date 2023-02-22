import json
import allure
import jsonpath
import requests
from Server.API.Constants.sorting_constants import Sorting


class Test_Sorting(Sorting):
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Test api for sorting products from low price")
    def test_api_for_sorting_from_lowest(self):
        url = self.sorting_lp_url
        data = self.sorting_from_low
        res = requests.post(url, json=data)
        products = len(res.json()["payload"]["data"])
        first_prod_price = jsonpath.jsonpath(json.loads(res.text), 'payload[data][0].price')[0]
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
        assert products == 20
        assert first_prod_price == 1

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Test api for sorting products from high price")
    def test_api_for_sorting_from_highest(self):
        url = self.sorting_hp_url
        data = self.sorting_from_hp
        res = requests.post(url, json=data)
        products = len(res.json()["payload"]["data"])
        first_prod_price = jsonpath.jsonpath(json.loads(res.text), 'payload[data][0].price')[0]
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
        assert products == 20
        assert first_prod_price == 555

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Test api for searching the product called kevin jackie")
    def test_api_for_searching_kevin_jackie(self):
        url = self.searching_kevin_url
        data = self.searching_kevin
        res = requests.post(url, json=data)
        products = len(res.json()["payload"]["data"])
        product_name = jsonpath.jsonpath(json.loads(res.text), 'payload[data][0].name')[0]
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
        assert products == 1
        assert product_name == "קווין ג'קי"

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Test api for clicking snacks link")
    def test_api_for_snack_link(self):
        url = self.snacks_url
        data = self.snack_link
        res = requests.post(url, json=data)
        products = len(res.json()["payload"]["data"])
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
        assert products == 4

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Test api for selecting the product called gorilla glu")
    def test_api_for_selecting_gorilla_glu(self):
        url = self.gorilla_glu_url
        data = self.gorilla_glu
        res = requests.post(url, json=data)
        products = len(res.json()["payload"])
        product_name = jsonpath.jsonpath(json.loads(res.text), 'payload[0].name')[0]
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
        assert products == 1
        assert product_name == "גורילה גלו"

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Test api for filtering using letter 'g'")
    def test_api_for_with_g(self):
        url = self.filter_withg_url
        data = self.filter_by_letter_g
        res = requests.post(url, json=data)
        product_num = jsonpath.jsonpath(json.loads(res.text), 'payload[count]')[0]
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
        assert product_num == 4
