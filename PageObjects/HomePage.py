from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self,driver):
        self.driver = driver

    search_box_field_name ="search"
    search_button_path ="//button[contains(@class,'btn-default')]"
    my_account_drop_menu_xpath ="//a[@title='My Account']/span[1]"
    login_button_Link_text ="Login"
    register_button_Link_text ="Register"


    def enter_product_into_search_box_field(self,product_name):
        self.driver.find_element(By.NAME,self.search_box_field_name).click()
        self.driver.find_element(By.NAME, self.search_box_field_name).clear()
        self.driver.find_element(By.NAME, self.search_box_field_name).send_keys(product_name)

    def click_on_search_button(self):
        self.driver.find_element(By.XPATH,self.search_button_path).click()


    def click_on_my_account_menu(self):
        self.driver.find_element(By.XPATH,self. my_account_drop_menu_xpath).click()

    def click_on_login_button(self):
        self.driver.find_element(By.LINK_TEXT,self.login_button_Link_text).click()

    def click_on_register_button(self):
        # register link is a link text on the page, so use LINK_TEXT locator instead of XPATH
        self.driver.find_element(By.LINK_TEXT, self.register_button_Link_text).click()