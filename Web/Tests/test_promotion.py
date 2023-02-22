import allure

from Web.Pages.promotion_page import *


class Test_Promotion(PromotionPage):

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Check the number of products on the page")
    def test_number_of_products(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        time.sleep(3)
        assert self.count_number_of_products(self.products_path) == self.product_number_on_page_title()
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("varify if the product name on the first page matches the product name on the second page")
    def test_all_products_are_clickable(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        assert self.check_name_of_products() == 0
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify if the title of the page is displayed")
    def test_title_displayed(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self._is_displayed(self.page_title)
        self._driver.close()

    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Verify the font size of the title of the page")
    def test_font_size(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        assert self.checking_font_size(self.page_title) == '40px'
        self._driver.close()

    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Verify The font size of page title")
    def test_page_title_font_weight(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        assert self.checking_font_weight(self.page_title) == '700'
        self._driver.close()

    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Check the text alignment of the page title")
    def test_text_align_for_page_title(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        assert self.checking_text_align(self.page_title) == 'start'
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify if the language changer is working")
    def test_language_changer(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self.clicking_the_button(self.language_button)
        assert self.checking_text_align(self.text_align) == 'left'
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify if there is duplicated products")
    def test_if_products_are_duplicated(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        assert self.check_that_there_is_no_duplicated_products() == True
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify if the user can add all products on cart")
    def test_adding_all_products_to_cart(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        assert self.adding_products() == self.expected_product_number()
        self._driver.close()

    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Verify the background color of the page")
    def test_color_of_the_body_of_page(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        assert self.color(self.body) == self.white
        self._driver.close()

    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Check the color of the logo")
    def test_color_of_logo(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        assert self.color(self.logo_color) == 'rgba(47, 150, 185, 1)'
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Check if the bolded price and unit price of the product is equal")
    def test_the_bolded_price_and_price_on_detail(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        assert self.price_checking() == 0
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Check if autosuggestion of search works properly")
    def test_AutoSuggestive_for_search(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self.write_g_on_search_field()
        assert self.checking_auto_suggestion_works(self.finding) == True
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify the functionality of search feature")
    def test_search_functionality(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self.enter_item_name()
        assert self.check_search_functionality(self.enter_item_name()) == "גורילה גלו"
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify if the sorting feature has multiple otptions")
    def test_sorting_has_many_options(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self.clicking_the_button(self.sorting_dropdown)
        assert self.checking_sorting_options() > 1
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify facebook link functionality")
    def test_facebook_link_functionality(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self.clicking_the_button(self.facebook_link)
        self.switching_window()
        assert self.checking_current_url() == self.facebook_url
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify instagram link functionality")
    def test_instagram_link_functionality(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self.clicking_the_button(self.instagram_link)
        self.switching_window()
        assert self.checking_current_url() == self.instagram_url
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify twitter link functionality")
    def test_twitter_link_functionality(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self.clicking_the_button(self.twitter_link)
        self.switching_window()
        assert self.checking_current_url() == self.twitter_url
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify the functionality of payment solution link")
    def test_payment_solution_link_functionality(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self.clicking_the_button(self.payment_solution_link)
        self.switching_window()
        assert self.checking_current_url() == self.payment_solution_url
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify the functionality of max businees link")
    def test_max_business_link_functionality(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self.clicking_the_button(self.payment_solution_link)
        self.switching_window()
        assert self.checking_current_url() == self.payment_solution_url
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify the functionality of accessibility statement link")
    def test_accessibility_statement_link_functionality(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self.clicking_the_button(self.accessability_linck)
        self.switching_window()
        assert self.checking_current_url() != self.url
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify the functionality of privacy policy link")
    def test_privecy_policy_link_functionality(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self.clicking_the_button(self.privrcy_policy_link)
        self.switching_window()
        assert self.checking_current_url() != self.url
        assert self.text_reading(self.privecy_page_title) == "מדיניות פרטיות"
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify the functionality of terms link")
    def test_terms_link_functionality(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self.clicking_the_button(self.terms_link)
        self.switching_window()
        assert self.checking_current_url() != self.url
        assert self.text_reading(self.terms_page_title) == "תקנון"
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Checking if sorting is working from lowest price")
    def test_sorting_from_lowest_price(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self.clicking_the_button(self.sorting_dropdown)
        self.clicking_the_button(self.sort_lp)
        assert self.check_sorting_with_from_lowest_price() == True
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Checking if sorting is working from highest price")
    def test_sorting_from_highest_price(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self.clicking_the_button(self.sorting_dropdown)
        self.clicking_the_button(self.sort_hp)
        assert self.check_sorting_with_from_lowest_price() == True
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify the functionality of common question link")
    def test_common_question_link(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self.clicking_the_button(self.common_question_link)
        self.switching_window()
        assert self.checking_current_url() != self.url
        assert self.text_reading(self.common_question_text) == 'יש לכם שאלות ?\nהגעתם למקום הנכון'
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify the functionality of shipment link")
    def test_shipment_link_functionality(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self.clicking_the_button(self.common_question_link)
        self.switching_window()
        assert self.checking_current_url() != self.shipment_url
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify the functionality of who we are link")
    def test_who_we_are_link_functionality(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self.clicking_the_button(self.who_we_are_link)
        self.switching_window()
        assert self.checking_current_url() == self.who_we_are_url
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify the functionality of my account link")
    def test_account_link_functionality(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        self.clicking_the_button(self.account_link)
        assert self.text_reading(self.account_title) == 'ברוכים השבים! מתרגשים לראות אתכם כאן'
        self._driver.close()

    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Verify the number of header bars on restaurant options")
    def test_header_bars_in_restaurant_option(self):
        self.open()
        self.select_option1()
        self.click_save_button()
        assert self.check_header_bars() == self.restaurant_links
        self._driver.close()

    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Verify the number of products on restaurant options")
    def test_product_number_restaurant_option(self):
        self.open()
        self.select_option1()
        self.click_save_button()
        assert self.count_number_of_products(self.products_path) == self.product_number_on_page_title()
        self._driver.close()

    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Verify the number of header bars on cocktail options")
    def test_header_bars_in_cocktail_option(self):
        self.open()
        self.select_option2()
        self.click_save_button()
        assert self.check_header_bars() == self.coctail_links
        self._driver.close()

    @allure.severity(allure.severity_level.MINOR)
    @allure.description("check product numbers in cocktails option")
    def test_product_number_cocktail_option(self):
        self.open()
        self.select_option2()
        self.click_save_button()
        assert self.count_number_of_products(self.products_path) == self.product_number_on_page_title()
        self._driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify the price of products on database")
    def test_price_of_products_on_database(self):
        self.open()
        self.select_option1()
        self.select_option2()
        self.click_save_button()
        assert self.checking_unit_price_on_database() == []
        self._driver.close()







