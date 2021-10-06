import smtplib
from email.message import EmailMessage
from lib2to3.pgen2 import driver
from selenium import webdriver
import time
from fpdf import FPDF

PDFtext = []
# Chrome executable path
driver=webdriver.Chrome(executable_path='C:\Python39\Lib\site-packages\selenium\webdriver\chrome\chromedriver')

#To maximize window
driver.maximize_window()
driver.implicitly_wait(10)
PDFtext.append("Window Maximized")

#To open URL
driver.get("https://beneficienttest.appiancloud.com/suite/")
PDFtext.append("Website Opened")
time.sleep(2)

#To enter username
username=driver.find_element_by_xpath("//div[@class='login_box_inner']/form[2]/div[1]/div/input")
print(username.is_displayed()) #returns true/false based element status
print(username.is_enabled()) #return true/false
username.send_keys("neeraj.kumar")
PDFtext.append("Username Entered Successfully")
time.sleep(3)

#To enter password
password=driver.find_element_by_xpath("//div[@class='login_box_inner']/form[2]/div[2]/div/input")
print(password.is_displayed()) #returns true/false based element status
print(password.is_enabled()) #return true/false
password.send_keys("Crochet@786")

#PDFtext.append("Password Entered Successfully")

driver.find_element_by_xpath("//div[@class='login_box_inner']/form[2]/div[4]/div/div[2]/input").click()
PDFtext.append("Login successfully")
time.sleep(2)

# print(str(len(PDFtext)))
pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", 'B' , size=15)
pdf.image("C:/Users/Gagan/PycharmProjects/Exercise_01/Test_script/PDF_01/Ben.png", x = 150, y = 5, w = 40, h = 20, type = 'PNG', link = '')

#To Open Each Module
for x in range (1,6):
    driver.find_element_by_xpath("//ul[@class='SiteHeaderLayout---site_nav']/li["+str( x )+"]").click()
    for iat3 in range(1000):
        try:
            bool = driver.find_element_by_xpath(
                "//div[@id='appian-working-indicator-hidden']").is_enabled()
        except Exception:
            time.sleep(1)
            break
    time.sleep(10)
    get_title = driver.title
    print(get_title)
    PDFtext.append(get_title)

print(len(PDFtext))
for i in range (len(PDFtext)):
    print(PDFtext[i])
    pdf.cell(10, 15, txt =PDFtext[i], ln =10, align ="L")
pdf.output("C:/Users/Gagan/PycharmProjects/Exercise_01/Test_script/PDF_01/Exercise_02.pdf")
time.sleep(10)

# To Send Email
msg=EmailMessage()
sender_email="Gagan139896@gmail.com"
Password="7696139896"
receiver_email="gagandeep.singh@crochetech.com"

msg['From']=sender_email
msg['Subject']='Automation Test Report'
msg['To']=receiver_email
msg.set_content("Hello Sir,\nPlease find the attached automation test report below\n\n\n\n Many Thanks\nGagandeep Singh")

files = 'Exercise_02.pdf'
for file in files:
    with open('C:/Users/Gagan/PycharmProjects/Exercise_01/Test_script/PDF_01/'+files, 'rb') as f:
        file_data = f.read()
        file_name = "Exercise_02.pdf"

    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(sender_email, Password)
server.send_message(msg)
server.quit()
print("Email sent successfully")


driver.close()


