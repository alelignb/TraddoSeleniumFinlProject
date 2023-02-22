import allure
from Web.Pages.cart_page import CartPage


class TestCart(CartPage):
    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Verify if the title of cart frame is correct")
    def test_the_cart_frame_title(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        assert self.check_the_title_of_cart_is_correct() == 'סל הקניות שלך'

    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Check the font weight of cart frame title")
    def test_cart_title_font_weight(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        assert self.checking_font_weight(self.cart_title) == '700'
        self._driver.close()

    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Check the test alignment of cart frame title")
    def test_text_align_for_cart_title(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        assert self.checking_text_align(self.cart_title) == 'right'
        self._driver.close()

    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Verify the background color of the cart frame")
    def test_background_color_of_cart_page(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        assert self.color(self.background) == 'rgba(0, 0, 0, 0)'
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify if the cart is empty without adding the product")
    def test_cart_without_adding_products(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        assert self.check_the_cart_is_empty_without_adding_products() == "העגלה שלך ריקה"
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify total price without adding products")
    def test_total_price_without_adding_products(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self.scroll(self.total_price, "window.scrollBy(0,250)")
        assert self.check_total_price_on_cart(self.total_price) == self.total_price_calculation(self.prod_price)
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify total price by adding products")
    def test_total_price_by_adding_products(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self.click_the_product(self.random_product)
        self.adding_to_cart()
        assert self.check_total_price_on_cart(self.tp_after_add) == self.total_price_calculation(self.pr_price_after_add)
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify the functionality of delete feature on the cart")
    def test_delete_feature_functionality(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self.click_the_product(self.random_product)
        self.adding_to_cart()
        self.click_the_button(self.delete)
        assert self.check_total_price_on_cart(self.tp_after_add) == 0
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify the functionality of plus and minus buttons")
    def test_functionality_plus_minus_button(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self.click_the_product(self.random_product)
        self.double_click_on_addition(self.add_to_cart_button)
        self.click_the_button(self.minus_button)
        assert self.amout_on_cart() == 1
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify if the price will be doubled when we add the same products")
    def test_price_increment_duplicated_product(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self.click_the_product(self.random_product)
        self.double_click_on_addition(self.add_to_cart_button)
        assert self.amout_on_cart() == 2
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify if the bolded price and subtotal of the a product on cart")
    def test_prices_on_cart(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self.checking_subtotal_and_bolded_prices()
        assert self.checking_subtotal_and_bolded_prices() == 0
        self._driver.close()

    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Verify the color of plus and minus buttons")
    def test_color_of_plus_and_minus(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self.click_the_product(self.random_product)
        assert self.color(self.plus_minus_color) == 'rgba(47, 150, 185, 1)'
        self._driver.close()

    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Verify the font weight of product specification page")
    def test_font_size_of_spec_page_title(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self.click_the_product(self.random_product)
        assert self.checking_font_weight(self.product_title) == '700'
        self._driver.close()

    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Verify if we can send a message with  all valid data")
    def test_text_alignment_of_spec_page_title(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self.click_the_product(self.random_product)
        assert self.checking_text_align(self.product_title) == 'start'
        self._driver.close()

    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Verify the text of payment button is correct")
    def test_verify_text_of_payment_button(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self.click_the_product(self.random_product)
        self.double_click_on_addition(self.add_to_cart_button)
        assert self.text_reading(self.payment) == 'תשלום'
        self._driver.close()

    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Verify the color of payment button")
    def test_color_of_payment_button(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self.click_the_product(self.random_product)
        self.double_click_on_addition(self.add_to_cart_button)
        assert self.color(self.payment) == 'rgba(47, 150, 185, 1)'
        self._driver.close()

    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Verify the font size of the product on cart")
    def test_font_size_of_prod_title_on_cart(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self.click_the_product(self.random_product)
        self.click_the_button(self.add_to_cart_button)
        assert self.checking_font_weight(self.prod_title_oncart) == '600'
        self._driver.close()

    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Verify the color total price of the product on cart")
    def test_color_of_total_price(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        assert self.text_color(self.total_price) == 'rgba(47, 150, 185, 1)'
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify the width of cart bar")
    def test_width_of_cart_bar(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        assert self.frame_width(self.total_price) == '37.7875px'
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify distribution cost before add product")
    def test_distribution_cost_before_add_product(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        assert self.text_reading(self.initial_shipment) == '₪0.00'
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify if vat is zero before adding product on cart")
    def test_vat_before_add_product(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        assert self.text_reading(self.initial_vat) == '₪0.00'
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify if the products are visible on cart")
    def test_products_are_visible_on_cart(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        assert self.checking_products_are_displayed_on_cart() == True
        self._driver.close()

