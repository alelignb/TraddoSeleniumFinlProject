from selenium.webdriver.common.by import By


class Locators_Cannabis:
    option1 = (By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div[3]/div[2]')
    option2 = (By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div[3]/div[1]')
    save = (By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/button')
    add_to_cart = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div["
                             "1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]")
    CANNABIS_URL = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/a[3]")
    CANNABIS_TEXT = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/h1[1]")
    CART_URL = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]")
    product = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/a[4]/div[1]/div[2]/div[1]/img[1]")
    product_text = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/h1[1]")
    plus_button = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]")
    minus_button = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/span[2]")

    product_text_on_cart = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/a[1]/div[1]/div[2]/div[1]")
    product_pics_number_on_cart = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/a[1]/div[1]/div[2]/div[2]/div[1]")
    product_carton_number_on_cart = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/a[1]/div[1]/div[2]/div[2]/div[2]")
    whatsapp = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[4]/div[2]")
    whatsapp_text = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[2]/span[1]")
    whatsapp_message =(By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[3]/input[1]")
    whatsapp_send_button = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[3]/button[1]")
    english_icon = (By.XPATH, "//body[1]/div[1]/div[1]/div[1]")
    english_text = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/h1[1]")

    hebrew_icon = (By.XPATH, "//body[1]/div[1]/div[1]/div[1]")
    hebrew_text = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/h1[1]")

    max_asakim = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/p[1]")
    shelot_nosafot = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/h3[1]")
    shelot_nosafot2 = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/li[1]")
    yetsirat_kesher = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/h3[1]")
    yetsirat_kesher2 = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/li[1]")
    eah_oved_hashiluwah = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/h3[1]")
    eah_oved_hashiluwah2 = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/li[1]")
    option_list = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div[1]/select[1]")
    popularity = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div[1]/select[1]/option[1]")
    arrow_from_highest = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div[1]/select[1]/option[2]")
    arrow_from_list = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div[1]/select[1]/option[3]")
    order_diagonally_btn = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[4]/span[2]")
    order_vertically_btn = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[4]/span[1]")