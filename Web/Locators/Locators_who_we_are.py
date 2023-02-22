from selenium.webdriver.common.by import By

class Locators_who_we_are:

    option1 = (By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div[3]/div[2]')
    option2 = (By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div[3]/div[1]')
    save = (By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/button')
    path_who_we_are = (By.XPATH, "//a[contains(text(),'מי אנחנו')]")
    mischar_button= (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[3]")
    pratim_nosafim_button = (By.LINK_TEXT, "פרטים נוספים")
    pratim_text1 = (By.XPATH, "//body[1]/main[1]/div[3]/div[1]/h1[1]")
    pratim_text2 = (By.XPATH, "//body[1]/main[1]/div[3]/div[1]/div[1]/div[1]/div[1]/h4[1]")
    pratim_text3 = (By.XPATH, "//body[1]/main[1]/div[3]/div[1]/div[1]/div[4]/div[1]/h4[1]")
    new_order_button = (By.LINK_TEXT, "הזמנה חדשה")
    welcome_text = (By.XPATH, "//body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/h1[1]")
    create_contact_button = (By.LINK_TEXT, "הזמנה חדשה")
    create_contact_text1 = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/h4[1]")
    create_contact_text2 = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/h3[1]")
    rkisha_ve_mehira_text = (By.XPATH, "//body[1]/main[1]/div[2]/div[1]/div[2]/div[1]/h4[1]")
    efshariyot_tashlum_text = (By.XPATH, "//body[1]/main[1]/div[2]/div[1]/div[2]/div[2]/h4[1]")
    maarah_mishlohim_text = (By.XPATH, "//body[1]/main[1]/div[2]/div[1]/div[2]/div[3]/h4[1]")
    footer = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[3]")
    who_we_are_txt = (By.XPATH, "//body[1]/main[1]/div[1]/div[1]/h1[1]")


    # mischar_button = (By.LINK_TEXT, "לזירת המסחר")

