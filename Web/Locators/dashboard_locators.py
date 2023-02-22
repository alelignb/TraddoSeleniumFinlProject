from selenium.webdriver.common.by import By


class Dashboard_Locators:

    correct_phone_number = (By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[1]/span[1]/form[1]/div[1]/div[1]/span[1]/div[1]/input[1]")
    phone_code = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/span[1]/form[1]/input[1]")
    correct_passward = (By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[1]/span[1]/form[1]/div[1]/div[1]/span[1]/div[1]/input[1]")
    check_box = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/span[1]/form[1]/div[1]/div[2]/span[1]")
    connection_button = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/span[1]/form[1]/input[1]")
    dsheboard_button = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/nav[1]/div[2]/a[1]/span[2]")
    coupon_button = (By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[1]/nav[1]/div[2]/a[4]")
    order_button = (By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[1]/nav[1]/div[2]/a[5]")
    product_button = (By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[1]/nav[1]/div[2]/a[2]")
    invoice_button = (By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[1]/nav[1]/div[2]/a[6]")
    shping_certificate_button = (By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[1]/nav[1]/div[2]/a[7]")
    delivery_dasheboard = (By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[1]/nav[1]/div[2]/a[8]")
    delevery_table = (By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[1]/nav[1]/div[2]/a[9]")
    acskquestion_overview = (By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[1]/nav[1]/div[2]/a[10]")
    dasheboard_text = (By.XPATH,"//h4[contains(text(),'דשבורד')]")
    title_with_finance = (By.XPATH,"//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/a[8]/span[1]")

    finance2_count = (By.XPATH,"//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/a[8]")

    dsheboard_footer = (By.XPATH,"//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[3]")
    dasheboard_all_pages = (By.XPATH,"//body/div[@id='root']/div[1]/div[2]")
    dasheboard_page_width = (By.XPATH,"//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]/canvas[1]")
    dashboard_page_size = (By.XPATH,"//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[1]")
    dashboard_page_font = (By.XPATH,"//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]")
    dashboard_page_graph = (By.XPATH,"//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]/canvas[1]")


