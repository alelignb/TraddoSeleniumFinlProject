import allure
from Web.Pages.snacks_page import SnacksPage


class Test_SnacksPage(SnacksPage):

    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Verify if the title of snacks page correct")
    def test_page_title(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        assert self.text_reading(self.page_title) == "חטיפים"
        self._driver.close()

    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Verify the number of products on the page")
    def test_number_of_products(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self.clicking_snacks_link()
        assert self.count_number_of_products(self.snacks_path) == self.expected_product_number()
        self._driver.close()

    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Verify the font size of the page title")
    def test_font_size(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self.clicking_snacks_link()
        assert self.checking_font_size(self.page_title) == '40px'
        self._driver.close()

    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Verify the font weight of page title")
    def test_page_title_font_weight(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self.clicking_snacks_link()
        assert self.checking_font_weight(self.page_title) == '700'
        self._driver.close()

    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Verify the text alignment of the page title")
    def test_text_align_for_page_title(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self.clicking_snacks_link()
        assert self.checking_text_align(self.page_title) == 'start'
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify if there is duplicated product on the page")
    def test_if_products_are_duplicated(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self.clicking_snacks_link()
        assert self.check_that_there_is_no_duplicated_products() == True
        self._driver.close()

    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Verify the background color is black")
    def test_color_of_the_body_of_page(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self.clicking_snacks_link()
        assert self.color(self.body) == 'rgba(248, 248, 250, 1)'
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify if all products are clickable")
    def test_all_products_are_clickable(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self.clicking_snacks_link()
        self.click_all_products()
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify if the sorting has different options")
    def test_sorting_has_many_options(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self.clicking_snacks_link()
        self.clicking_the_button(self.sorting_dropdown)
        assert self.checking_sorting_options() > 1
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify if sorting works from lowest price")
    def test_sorting_from_lowest_price(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self.clicking_snacks_link()
        self.clicking_the_button(self.sorting_dropdown)
        self.clicking_the_button(self.sort_lp)
        assert self.check_sorting_with_from_lowest_price() == 0
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify if the sorting feature is working from highest price")
    def test_sorting_from_highest_price(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self.clicking_snacks_link()
        self.clicking_the_button(self.sorting_dropdown)
        self.clicking_the_button(self.sort_hp)
        assert self.check_sorting_with_from_lowest_price() == 0
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify the number of products on the cocktail option")
    def test_product_number_cocktail_option(self):
        self.open()
        self.select_option2()
        self.click_save_button()
        self.clicking_snacks_link()
        assert self.count_number_of_products(self.snacks_path) == self.product_number_on_page_title()
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify number of products in restaurant option")
    def test_product_number_restaurant_option(self):
        self.open()
        self.select_option1()
        self.click_save_button()
        self.clicking_snacks_link()
        assert self.count_number_of_products(self.snacks_path) == self.product_number_on_page_title()
        self._driver.close()