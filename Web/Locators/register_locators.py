from selenium.webdriver.common.by import By


class RegisterLocators:
    option1 = (By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div[3]/div[2]')
    option2 = (By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div[3]/div[1]')
    save = (By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/button')
    connection_button = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/input[1]")
    register_button = (By.XPATH, "//span[contains(text(),'הרשם')]")
    register_title = (By.XPATH, "//h2[contains(text(),'כיף שבאתם! כבר יוצרים לכם מקום בזירה')]")
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
    id_no_text = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/label[1]")
    id_field = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div["
                          "2]/span[1]/input[1]")
    security_check_box = (By.CLASS_NAME, "checkbox_checkboxCircle")
    check_box_text = (By.XPATH, "//label[contains(text(),'קראתי ואני מאשר/ת את תקנון השימוש ומדיניות הפרטיות')]")
    cancel_button = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/span[1]")
    page = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]")
    account_link = (By.XPATH, "//a[contains(text(),'החשבון שלי')]")
    code_box = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div["
                          "1]/span[1]/input[1]")
    enter_phone_error = (By.XPATH, "//div[contains(text(),'נא למלא שדה זה')]")
    no_such_phone = (By.XPATH, "//div[contains(text(),'no such user please register')]")
    perform_verification = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/input[1]")
    text_under_button = (By.XPATH, "//div[contains(text(),'שלחו לי שוב, לא קיבלתי SMS')]")
    empty_phone_error = (By.XPATH, "//div[contains(text(),'נא למלא שדה זה')]")
    empty_id_error = (By.XPATH, "//body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[3]")
    invalid_phone_error = (By.XPATH, "//div[contains(text(),'מס׳ טלפון לא תקין')]")
    page_title2 = (By.XPATH, "//h2[contains(text(),'רק מוודאים שאנחנו מכירים')]")
    existing_phone_error = (By.XPATH, "//div[contains(text(),'שדה צריך להיות ייחודיי')]")
    etrado_title = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/section[1]/header["
                              "1]/div[1]/h1[1]")
    trado = (By.XPATH, "//header/div[1]/div[1]/a[3]/div[1]")
    food = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]")
    drin = (By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]")
    crate_account = (By.XPATH, "//button[contains(text(),'createAcount')]")
    fn = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[3]/form[1]/div[1]/div[1]/span[1]/input[1]")
    ln = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[3]/form[1]/div[1]/div[2]/span[1]/input[1]")
    em = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[3]/form[1]/div[1]/div[4]/span[1]/input[1]")
    tz = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[3]/form[1]/div[1]/div[5]/span[1]/input[1]")
    irr = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[3]/form[1]/div[2]/div[1]/div[1]/div[1]/input[1]")
    mispar = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[3]/form[1]/div[2]/div[1]/div[1]/div[2]/span[1]/input[1]")
    edit = (By.XPATH, "//div[contains(text(),'עריכה')]")
    saving = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[3]/form[1]/input[1]")
    exit_but = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/header[1]/div[1]/div[1]/a[2]/span[1]")



