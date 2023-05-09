from selenium import webdriver
import time

def delay(x):
    time.sleep(x)

def Find_A_House(Location,range):
    l = len(range)
    range=range[:l - 1] + "000"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.redfin.com/")
    delay(5)
    driver.find_element("id", "search-box-input").send_keys(f"{Location}")
    delay(5)
    driver.find_element('css selector', "#tabContentId0 > div > div > form > div > button").click()
    delay(5)
    driver.find_element('css selector',"#sidepane-header > div > div.desktopExposedSearchFiltersContainer > form > div:nth-child(2) > div").click()
    # Price
    delay(10)
    driver.find_element("css selector","#sidepane-header > div > div.desktopExposedSearchFiltersContainer > form > div:nth-child(2) > div > div.Flyout.standard.v83.position-right.alignment-below.CustomFilter__flyout.transparent.standard > div.flyout > div > div.CustomFilter__container > div > div > div.flex.align-center.inputRangeAfterHistogram > span:nth-child(3) > span > div > input").send_keys(f"{range}")
    delay(3)
    driver.find_element('css selector',"#sidepane-header > div > div.desktopExposedSearchFiltersContainer > form > div:nth-child(2) > div > div.Flyout.standard.v83.position-right.alignment-below.CustomFilter__flyout.transparent.standard > div.flyout > div > div.CustomFilter__footer.flex.align-center > div > button.button.Button.primary").click()
    delay(3)
    # SELECT hometype
    driver.find_element('css selector',"#sidepane-header > div > div.desktopExposedSearchFiltersContainer > form > div.CustomFilter.inline-block.desktopExposedSearchFilter.default.desktopExposedPropertyTypeFilter.showDesktopFilterMenuRedesign").click()
    delay(2)
    driver.find_element('css selector',"#sidepane-header > div > div.desktopExposedSearchFiltersContainer > form > div.CustomFilter.inline-block.desktopExposedSearchFilter.desktopExposedPropertyTypeFilter.showDesktopFilterMenuRedesign > div.Flyout.standard.v83.position-left.alignment-below.CustomFilter__flyout.transparent.standard > div.flyout > div > div.CustomFilter__container > div > div > div > div > div > div > div:nth-child(1)").click()
    # SELECT HOUSE

    delay(2)
    driver.find_element('xpath',"/html/body/div[1]/div[9]/div[2]/div[2]/div[2]/div/div/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/button[2]/span").click()

    delay(2)
    driver.find_element('css selector',"#sidepane-header > div > div.desktopExposedSearchFiltersContainer > form > div.CustomFilter.inline-block.desktopExposedSearchFilter.desktopExposedBedsAndBathsContainer.showDesktopFilterMenuRedesign").click()
    # HOUSE DONE
    delay(5)
    driver.find_element('xpath',"/html/body/div[1]/div[9]/div[2]/div[2]/div[2]/div/div/div[1]/form/div[4]/div[2]/div[1]/div/div[1]/div/div[1]/div/div[2]/div/div/div/div[6]").click()
    delay(2)
    driver.find_element('css selector',"#sidepane-header > div > div.desktopExposedSearchFiltersContainer > form > div.CustomFilter.inline-block.desktopExposedSearchFilter.desktopExposedBedsAndBathsContainer.showDesktopFilterMenuRedesign > div.Flyout.standard.v83.position-left.alignment-below.CustomFilter__flyout.transparent.standard > div.flyout > div > div.CustomFilter__footer.flex.align-center > div > button.button.Button.primary").click()
    delay(20)






