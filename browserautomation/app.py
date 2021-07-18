from selenium import webdriver
import time
import os

chr_options = webdriver.ChromeOptions()
chr_options.add_argument("start-maximized");
chr_options.add_experimental_option("detach", True)
browser = webdriver.Chrome(chrome_options=chr_options, executable_path=r'/Users/smenezes/downloads/chromedriver')
browser.get("https://www.github.com")


sigin_link = browser.find_element_by_link_text("Sign in")
sigin_link.click()

username_box = browser.find_element_by_id("login_field")
username_box.send_keys("seanmenezes")
password_box = browser.find_element_by_id("password")
password_box.send_keys("password")
password_box.submit()
assert "ninjacoder22" in browser.page_source

profile_link = browser.find_element_by_class_name("user-profile-link")
link_label= profile_link.get_attribute("innerHTML")
assert "ninjacoder22" in link_label

browser.quit()




