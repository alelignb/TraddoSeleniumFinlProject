from selenium.webdriver.common.by import By


class CartLocators:
    cart_title = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div["
                            "1]/div[1]/div[1]/div[1]/h4[1]")
    products_path = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div["
                               "3]/a")
    empty_cart = (By.XPATH, "//h5[contains(text(),'העגלה שלך ריקה')]")
    option1 = (By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div[3]/div[2]')
    option2 = (By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div[3]/div[1]')
    save = (By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/button')
    total_price = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div["
                             "3]/div[1]/h6[4]/span[2]")
    tp_after_add = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div["
                              "1]/div[3]/div[1]/h6[4]/span[2]")
    prod_price = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div["
                            "3]/div[1]/h6[1]/span[2]")
    pr_price_after_add = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div["
                                    "2]/div[1]/div[3]/div[1]/h6[1]/span[2]")

    random_product = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div["
                                "3]/a[1]/div[1]/div[2]/div[2]/div[1]")
    add_to_cart_button = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div["
                             "1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]")

    cart_frame = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]")
    delete = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div["
                        "2]/div[1]/a[1]/div[1]/div[3]/div[2]/img[1]")
    product_counter = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div["
                                 "2]/div[1]/div[2]/div[1]/a[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/input[1]")
    sub_total = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div["
                              "2]/div[1]/a[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]")

    price_in_box = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div["
                              "1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[3]/div[1]")
    bolded_price = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div["
                              "1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]")

    units1 = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div["
                        "1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]")

    units2 = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div["
                        "1]/div[1]/div[2]/div[4]/div[4]/span[1]")

    background = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]")

    plus_minus_color = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div["
                                  "1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]")
    product_title = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div["
                               "1]/div[1]/div[1]/div[2]/div[1]/h1[1]")

    minus_button = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div["
                              "1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/span[2]")
    payment = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div["
                         "3]/button[1]")

    prod_title_oncart = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div["
                                   "2]/div[1]/div[2]/div[1]/a[1]/div[1]/div[2]/div[1]")

    initial_vat = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div["
                             "3]/div[1]/h6[3]/span[2]")
    initial_shipment = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div["
                                  "1]/div[3]/div[1]/h6[2]/span[2]")
    products_on_cart = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div["
                                  "1]/div[1]/div[2]/div[1]/a")
