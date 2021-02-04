from selenium import webdriver
import time

driver = webdriver.Chrome('/home/vishal/Downloads/chromedriver')

driver.get('https://tinder.com/?lang=en')
time.sleep(10)

log_in = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button/span').click()
time.sleep(5)

   

login_with_fb = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]').click()
time.sleep(10)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
#fb_login
phone = driver.find_element_by_name('email').send_keys('Your phone number')
password = driver.find_element_by_name('pass').send_keys('Your facebook password\n')

time.sleep(10)
driver.switch_to.window(base_window)

allow = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]/span').click()
time.sleep(5)
enable = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]/span').click()

time.sleep(10)
for _ in range(50):
    try:
        love = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button').click()
        time.sleep(2)
        no_thanks = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/button[2]/span').click()
    except:
        pass
    time.sleep(2)
