from selenium import webdriver

driver = webdriver.Chrome('/usr/lib/python2.7/site-packages/selenium/webdriver/chrome/chromedriver')
  # Optional argument, if not specified will search path.
r = driver.get(" https://wits.worldbank.org/CountryProfile/en/Country/JPN/Year/2017/TradeFlow/Export/Partner/All/Product/Total")
html_ = driver.page_source
print (html_)
driver.maximize_window()

#box = driver.find_element_cas_selector("country")
