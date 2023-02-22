from selenium.webdriver.common.by import By


class SnackLocators:
    option1 = (By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div[3]/div[2]')
    option2 = (By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div[3]/div[1]')
    snacks_path = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/a")
    save = (By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/button')
    products_path = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/a")
    snacks_link = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/a[2]")
    add_to_cart = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div["
                             "1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]")
    product_title = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div["
                               "1]/div[1]/div[1]/div[2]/div[1]/h1[1]")
    page_title = (By.XPATH, "//h1[contains(text(),'חטיפים')]")
    page_title2 = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div["
                             "1]/h4[1]/span[1]/span[1]")
    add_icon = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div["
                          "1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]")

    cart_counter = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div["
                              "1]/div[1]/div[1]/div[1]/div[1]")
    body = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]")
    suggestions = (By.XPATH, "//header/div[1]/div[1]/div[1]/div[1]/div[1]/a")
    search_field = (By.XPATH, "//header/div[1]/div[1]/div[1]/span[1]/input[1]")
    searched = (By.XPATH, "//header/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/div[2]/div[1]")
    language_button = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/span[1]")
    text_align = (By.XPATH, "//header/div[1]/div[1]/div[1]/span[1]/input[1]")
    sorting_dropdown = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div["
                                  "2]/div[1]/div[3]/div[1]/select[1]")
    sorting_options = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div["
                                 "2]/div[1]/div[3]/div[1]/select[1]/option")
    sort_lp = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div["
                         "3]/div[1]/select[1]/option[2]")
    sort_hp = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div["
                         "3]/div[1]/select[1]/option[3]")