from selenium.webdriver.common.by import By


class LoginLocators:
    option1 = (By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div[3]/div[2]')
    option2 = (By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div[3]/div[1]')
    save = (By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/button')
    connection_button = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/input[1]")
    connect_button = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]")
    loginpage_title = (By.XPATH, "//h2[contains(text(),'ברוכים השבים! מתרגשים לראות אתכם כאן')]")
    twitter_link = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div["
                              "1]/img[1]")
    google_link = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/button["
                             "1]/img[1]")
    facebook_link = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/span["
                               "1]/button[1]")
    facebook_title = (By.XPATH, "//h2[@id='homelink']")
    phone_field_text = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div["
                                   "1]/div[1]/label[1]")
    phone_field = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div["
                             "1]/span[1]/input[1]")
    remember_check_box = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div["
                                    "1]/div[2]/span[1]/span[1]/span[1]/i[1]")
    check_box_text = (By.XPATH, "//label[contains(text(),'זכור אותי לפעם הבאה :)')]")
    login_button = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/input[1]")
    cancel_button = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/span[1]")
    page = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]")
    account_link = (By.XPATH, "//a[contains(text(),'החשבון שלי')]")
    code_box = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div["
                          "1]/span[1]/input[1]")
    etrado_title = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/section[1]/header["
                              "1]/div[1]/h1[1]")
    enter_phone_error = (By.XPATH, "//div[contains(text(),'נא למלא שדה זה')]")
    no_such_phone = (By.XPATH, "//div[contains(text(),'no such user please register')]")












