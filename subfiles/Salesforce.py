from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
def delay(x):
    time.sleep(x)

def log_a_call_salesforce():
    # Get Web Chrome driver
    driver = webdriver.Chrome()

    # Maximize Driver Window
    driver.maximize_window()

    # Open our targeted webpage on driver
    driver.get("https://www.salesforce.com/in/")
    delay(2)

    # Shadow element Travesing
    shadow_root0=driver.find_element('css selector',"hgf-c360nav[locale='in']").shadow_root
    shadow_root0.find_element('css selector', ".utility-icons-items.login").click()
    delay(1)
    shadow_root1=shadow_root0.find_element('css selector',"hgf-c360login[aria-haspopup='true']").shadow_root
    delay(2)

    # Get login Page
    shadow_root1.find_element('css selector',"hgf-popover:nth-child(2)>div:nth-child(2)>div:nth-child(2)>a:nth-child(2)>h4:nth-child(1)").click()
    delay(5)

    # Enter username in Login Page
    driver.find_element('xpath'," //input[@id='password']").send_keys('Saurabh@123')
    delay(2)

    #Enter Password in Login Page
    driver.find_element('xpath', "//input[@id='username']").send_keys('radkesaurabh1999-lem3@force.com')
    delay(2)

    # Try to Login
    driver.find_element('xpath',"//input[@id='Login']").click()
    delay(10)

    # After Succesfull Login gor to Leads Section
    driver.find_element('xpath',"//span[@aria-description='Show more My Leads records']").click()
    delay(10)

    # Select the desired lead to log a Call
    driver.find_element('xpath',"//a[@title='James Wheel']").click()
    delay(5)

    # Log a call
    driver.find_element('xpath',"//span[@value='LogACall']").click()


    # Enter text message nedd to send with Log
    wait = WebDriverWait(driver, 5)
    wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[4]/div[1]/section/div[2]/div[1]/div[5]/div/div/div/div/div/div[2]/div/div[1]/section/div/section/div/div/div/div/div/div[2]/div[1]/div/div/div/div/textarea"))).send_keys("Are you looking to by 100 widgets")
    delay(3)

    # Finally Send the LOG
    driver.find_element(By.XPATH,"//button[@class='slds-button slds-button--brand cuf-publisherShareButton uiButton']").click()
    delay(20)

log_a_call_salesforce()
