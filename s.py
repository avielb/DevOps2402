from selenium import webdriver
from time import sleep

my_driver = webdriver.Chrome()
my_driver.get("file:///Users/avielb/Downloads/tip_calc 3/index.html")
my_driver.find_element_by_id("billamt").send_keys("100")
my_driver.find_element_by_id("peopleamt").send_keys("5")
my_driver.find_element_by_xpath("//*[@id=\"serviceQual\"]/option[4]").click()
my_driver.find_element_by_id("calculate").click()
expected = "3.00"
actual = my_driver.find_element_by_id("tip").text
assert expected == actual

