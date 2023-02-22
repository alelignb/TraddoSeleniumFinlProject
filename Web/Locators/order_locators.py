from selenium.webdriver.common.by import By


class OrderLocators:
    create_account = (By.XPATH, "//button[contains(text(),'createAcount')]")
    coctail = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]")
    restaurant = (By.XPATH, "//p[contains(text(),'מסעדות')]")
    create_account_page_title = (By.XPATH, "//h2[contains(text(),'עזרו לנו להציג לכם מוצרים שמתאימים בדיוק לכם')]")
    option1 = (By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div[3]/div[2]')
    option2 = (By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div[3]/div[1]')
    save = (By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/button')
    phone_field = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div["
                             "1]/span[1]/input[1]")
    connection_button = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/input[1]")
    code_box = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div["
                          "1]/span[1]/input[1]")
    login_button = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/input[1]")
    add_to_cart_button = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div["
              "1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]")
    checkout_button = (By.XPATH, "//button[contains(text(),'תשלום')]")
    og_kush = (By.XPATH, "//div[contains(text(),'OG Kush')]")
    business_name = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form["
                               "1]/section[1]/div[1]/div[1]/input[1]")
    id_num = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section["
                        "1]/div[1]/div[2]/input[1]")
    business_email = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form["
                                "1]/section[1]/div[1]/div[3]/input[1]")
    city = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section["
                      "1]/div[2]/div[1]/input[1]")
    street = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section["
                        "1]/div[2]/div[2]/input[1]")
    home = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section["
                      "1]/div[2]/div[3]/input[1]")
    entrance =(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section["
                         "1]/div[2]/div[4]/input[1]")
    floor = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section["
                       "1]/div[2]/div[5]/input[1]")

    city2 = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section["
                       "2]/div[1]/div[1]/input[1]")
    street2 = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section["
                         "2]/div[1]/div[2]/input[1]")
    home2 = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section["
                       "2]/div[1]/div[3]/input[1]")
    entrance2 = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section["
                           "2]/div[1]/div[4]/input[1]")
    floor2 = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section["
                        "2]/div[1]/div[5]/input[1]")
    business_name2 = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form["
                                "1]/section[2]/div[2]/div[1]/input[1]")
    fst_name = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section["
                            "2]/div[2]/div[2]/input[1]")
    lst_name = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section["
                          "2]/div[2]/div[3]/input[1]")
    tel_field = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section["
                           "2]/div[2]/div[4]/input[1]")
    finish = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section["
                        "3]/div[3]/button[1]")
    payment_option = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section["
                                "1]/div[3]/div[1]/label[2]/div[1]")
    pay = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section[2]/div["
                     "3]/button[1]")
    branch = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/form[1]/section[1]/div[3]/input[1]")
    card_num = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/form[1]/section[1]/div[4]/input[1]")
    confirm_transfer = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/form[1]/button[1]")
    thanks = (By.XPATH, "//h2[contains(text(),'תודה שהזמנת דרכנו!')]")
    back_to_home = (By.XPATH, "//button[contains(text(),'חזור לדף הבית')]")
    fname_error = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form["
                             "1]/section[2]/div[2]/div[2]/div[2]")
    lname_error = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form["
                             "1]/section[2]/div[2]/div[3]/div[2]")
    id_error = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section["
                          "1]/div[1]/div[2]/div[2]")
    email_error = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form["
                             "1]/section[1]/div[1]/div[3]/div[2]")

    city_error = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section["
                            "1]/div[2]/div[1]/div[2]")
    street_error = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form["
                              "1]/section[1]/div[2]/div[2]/div[2]")
    edit = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[3]/form[1]/input[1]")
    fn_error = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section["
                          "2]/div[2]/div[2]/div[2]")
    bname_error = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form["
                             "1]/section[1]/div[1]/div[1]/div[2]")
    my_wallet = (By.XPATH, "//h1[contains(text(),'הארנק שלי')]")
    bank_trans = (By.XPATH, "//h1[contains(text(),'bankTransfer')]")
    new_card = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section["
                          "1]/div[2]/div[1]/div[1]/div[1]")

    fin_trado = (By.XPATH, "//input[@id='finTrado']")
    digital_market = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section["
                                "1]/div[3]/div[1]/label[3]/div[1]")
    b2b = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/section[1]/div["
                     "3]/div[1]/label[3]/div[1]")

    iframe = (By.XPATH, "//iframe[@id='yaadFrame']")

    main_card = (By.ID, "credit-card-input")
    payment_id = (By.ID, "userId-input")
    expyear = (By.ID, "expyear")
    expmon = (By.ID, "expmonth")
    cvv = (By.ID, "cvv")
    credit_pay = (By.ID, "btnSubmit")
    total_price = (By.XPATH, "//span[contains(text(),'₪32.64')]")
    title_of_iframe = (By.XPATH, "//h1[contains(text(),'הוספת כרטיס אשראי')]")











