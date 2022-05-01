from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://in.bookmyshow.com/bengaluru/movies/beast/ET00311733")

input=driver.find_element_by_xpath('//*[@id="wzrk-confirm"]')
input.click()

input=driver.find_element_by_xpath('//*[@id="page-cta-container"]/button/div/span')
input.click()

input=driver.find_element_by_xpath('//*[@id="venuelist"]/li[2]/div[2]/div[2]/div/a/div/div')
input.click()

input=driver.find_element_by_xpath('//*[@id="btnPopupAccept"]')
input.click()

input=driver.find_element_by_xpath('//*[@id="proceed-Qty"]')
input.click()

input=driver.find_element_by_xpath('//*[@id="B_4_016"]/a')
input.click()

input=driver.find_element_by_xpath('//*[@id="btmcntbook"]')
input.click()






