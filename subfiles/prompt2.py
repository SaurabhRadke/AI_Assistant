from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
def delay(x):
    time.sleep(x)

def create_lead_salesforce():
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
    # After Succesfull Login go to Leads Section
    driver.find_element('xpath', "//span[@aria-description='Show more My Leads records']").click()
    delay(4)
    driver.find_element('xpath', "//div[@title='New']").click()
    # ADD getails to create Leads
    wait = WebDriverWait(driver,10)
    wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div/records-modal-lwc-detail-panel-wrapper/records-record-layout-event-broker/slot/records-lwc-detail-panel/records-base-record-form/div/div/div/div/records-lwc-record-layout/forcegenerated-detailpanel_lead___012000000000000aaa___full___create___recordlayout2/records-record-layout-block/slot/records-record-layout-section[1]/div/div/div/slot/records-record-layout-row[2]/slot/records-record-layout-item[1]/div/span/slot/records-record-layout-input-name/lightning-input-name/fieldset/div/div/div[2]/lightning-input/div/div/input"))).send_keys("Max")
    delay(1)
    driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div/records-modal-lwc-detail-panel-wrapper/records-record-layout-event-broker/slot/records-lwc-detail-panel/records-base-record-form/div/div/div/div/records-lwc-record-layout/forcegenerated-detailpanel_lead___012000000000000aaa___full___create___recordlayout2/records-record-layout-block/slot/records-record-layout-section[1]/div/div/div/slot/records-record-layout-row[2]/slot/records-record-layout-item[1]/div/span/slot/records-record-layout-input-name/lightning-input-name/fieldset/div/div/div[4]/lightning-input/div[1]/div/input").send_keys("Nye")
    delay(1)
    driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div/records-modal-lwc-detail-panel-wrapper/records-record-layout-event-broker/slot/records-lwc-detail-panel/records-base-record-form/div/div/div/div/records-lwc-record-layout/forcegenerated-detailpanel_lead___012000000000000aaa___full___create___recordlayout2/records-record-layout-block/slot/records-record-layout-section[1]/div/div/div/slot/records-record-layout-row[3]/slot/records-record-layout-item[2]/div/span/slot/records-record-layout-base-input/lightning-input/div[1]/div/input").send_keys('Workplete')
    delay(1)
    # Click to generate Lead
    driver.find_element('xpath', "//button[@name='SaveEdit']").click()
    delay(10)

create_lead_salesforce()