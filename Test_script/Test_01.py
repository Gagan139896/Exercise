from selenium import webdriver
import selenium.webdriver.common.keys
import time
import pyautogui
from fpdf import FPDF
#from reportlab.pdfgen import canvas


# Chrome executable path
driver=webdriver.Chrome(executable_path='C:\Python39\Lib\site-packages\selenium\webdriver\chrome\chromedriver')

#To maximize window
driver.maximize_window()
driver.implicitly_wait(10)

# To open URL
driver.get("https://beneficienttest.appiancloud.com/suite/")
time.sleep(2)

# To enter username
username=driver.find_element_by_xpath("//div[@class='login_box_inner']/form[2]/div[1]/div/input")
print(username.is_displayed()) #returns true/false based element status
print(username.is_enabled()) #return true/false
username.send_keys("neeraj.kumar")
time.sleep(3)

# To enter password
password=driver.find_element_by_xpath("//div[@class='login_box_inner']/form[2]/div[2]/div/input")
print(password.is_displayed()) #returns true/false based element status
print(password.is_enabled()) #return true/false
password.send_keys("Crochet@786")
driver.find_element_by_xpath("//div[@class='login_box_inner']/form[2]/div[4]/div/div[2]/input").click()
time.sleep(2)

funds = driver.find_element_by_xpath("//a[@aria-current='page']")

if funds.is_displayed():
        print("User Logged In Successfully")
        #profile = driver.find_element_by_xpath("//div[@class ='SiteHeaderLayout---showSiteNameNav'] / nav / div[3] / div / a / span").click()
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("helvetica", size=16)
        pdf.cell(200, 20, txt="User Logged In Successfully", ln=2, align="L")
        # pdf.txt('Logged In Successfully')
        pdf.output("Exercise_01.pdf")

else:
        print("Try again")

driver.close()

# filename= 'Exercise_01.pdf'
# title= 'Test_script'
# case1= 'LoggedIn Successfully'
# case2= 'Logout Button Clicked'
# case3= 'Logged Out Successfully'
# path= 'C:/Users/Gagan/Ben.jpg'
# pdf = canvas.Canvas("path")
# pdf.save()

