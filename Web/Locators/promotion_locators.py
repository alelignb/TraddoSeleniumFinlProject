from selenium.webdriver.common.by import By


class Promo_Locators:

    products_path = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div["
                               "3]/a")
    # first_popup = (By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/button')
    option1 = (By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div[3]/div[2]')
    option2 = (By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div[3]/div[1]')
    save = (By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/button')
    add_to_cart = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div["
                             "1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]")
    product_title = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div["
                               "1]/div[1]/div[1]/div[2]/div[1]/h1[1]")
    page_title = (By.XPATH, "//h1[contains(text(),'מבצעים')]")
    add_icon = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div["
                          "1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]")

    cart_counter = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div["
                              "1]/div[1]/div[1]/div[1]/div[1]")
    body = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]")
    logo_color = (By.XPATH, "//header/div[1]/div[1]/a[2]/div[1]")
    suggestions = (By.XPATH, "//header/div[1]/div[1]/div[1]/div[1]/div[1]/a")
    search_field = (By.XPATH, "//header/div[1]/div[1]/div[1]/span[1]/input[1]")
    searched = (By.XPATH, "//header/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/div[2]/div[1]")
    page_title2 = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div["
                             "1]/h4[1]/span[1]/span[1]")
    language_button = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/span[1]")
    text_align = (By.XPATH, "//header/div[1]/div[1]/div[1]/span[1]/input[1]")
    sorting_dropdown = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div["
                                  "2]/div[2]/div[3]/div[1]/select[1]")
    sorting_options = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div["
                                 "2]/div[2]/div[3]/div[1]/select[1]/option")

    facebook_link = (By.XPATH, "//a[contains(text(),'Facebook')]")
    facebook_url = "https://www.facebook.com/"
    instagram_link = (By.XPATH, "//a[contains(text(),'Instagram')]")
    instagram_url = "https://www.instagram.com/"
    twitter_link = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[3]/div[1]/div[3]/a[3]")
    twitter_url = "https://twitter.com/?lang=he"
    payment_solution_link = (By.XPATH, "//a[contains(text(),'פתרונות תשלום')]")
    payment_solution_url = "https://www.max.co.il/cards/card/8649"
    max_businees_link = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[3]/div[1]/div[2]/a[4]")
    accessability_linck = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[3]/div[1]/div[5]/div[1]/a[3]")
    privrcy_policy_link = (By.XPATH, "//a[contains(text(),'מדיניות פרטיות')]")
    privecy_page_title = (By.XPATH, "//h1[contains(text(),'מדיניות פרטיות')]")
    terms_page_url = (By.XPATH, "//h1[contains(text(),'תקנון')]")
    terms_link = (By.XPATH, "//a[contains(text(),'קראתי ואני מאשר/ת את תקנון השימוש ומדיניות הפרטיות')]")
    terms_page_title = (By.XPATH, "//h1[contains(text(),'תקנון')]")
    sort_lp = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div["
                         "3]/div[1]/select[1]/option[2]")
    sort_hp = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div["
                         "3]/div[1]/select[1]/option[3]")

    add_products_button = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div["
                                     "1]/div[2]/a[5]/span[1]")
    common_question_text = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/h4[1]")
    common_question_link = (By.XPATH, "//a[contains(text(),'שאלות נפוצות')]")
    shipment_url = (By.XPATH, "https://qa.trado.co.il/shipment")
    shipment_link = (By.XPATH, "//a[contains(text(),'איך עובד השילוח')]")
    who_we_are_link = (By.XPATH, "//a[contains(text(),'מי אנחנו')]")
    who_we_are_url = "https://www.trado.co.il/page"
    account_link = (By.XPATH, "//a[contains(text(),'החשבון שלי')]")
    account_title = (By.XPATH, "//h2[contains(text(),'ברוכים השבים! מתרגשים לראות אתכם כאן')]")
    etrado_link = (By.XPATH, "//a[contains(text(),'eTrado')]")
    etrado_url = "https://qa.trado.co.il/etrado"
    bars = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/a")
    restaurant_links = ['מבצעים', 'קנאביס', 'משקאות', '+ העלאת מוצר חדש']
    coctail_links = ['מבצעים', 'חטיפים', 'קנאביס', 'משקאות', '+ העלאת מוצר חדש']













