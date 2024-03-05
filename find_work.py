from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
from datetime import datetime

chrome_driver_path = './chromedriver.exe'

# URL of the page
url = 'https://optim8.com'

#initialize options 
chrome_options = Options()
#add headless option to remove chrome opening on ur computer
chrome_options.add_argument('--headless')

# Initialize the WebDriver (Chrome in this example)
driver = webdriver.Chrome(executable_path=chrome_driver_path,options=chrome_options)

# Open the page
driver.get(url)

# Find the button that triggers the form visibility
button = driver.find_element(By.ID, 'btnlogin')

# Click the button to make the form visible
button.click()

# Wait for the form to become visible
wait = WebDriverWait(driver, 10)
form = wait.until(EC.visibility_of_element_located((By.ID, 'divlogin')))

# Fill in the form
company_id = form.find_element(By.ID, 'companyid')
company_id.send_keys('uasouthhackensack')

user_id = form.find_element(By.ID, 'userid')
user_id.send_keys('848')

password_id = form.find_element(By.ID, 'pwd')
password_id.send_keys('0115')

login_button = driver.find_element(By.ID, 'btnloginsubmit')
login_button.click()

schedule_button = driver.find_element(By.ID, 'divschedule')
schedule_button.click()

time.sleep(1)
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table')

shifts={}
count=0
if table:
    for row in table.find_all('tr'):
        cells = row.find_all(['td', 'th'])
        row_data = [cell.text.strip() for cell in cells]
        if len(row_data) >= 7:
            count += 1
            if count not in shifts:
                    shifts[count] = []
            shifts[count].append(row_data[2])
            shifts[count].append(row_data[6])

#print(shifts)
# for item in workdates:
#     try:
#         if workdates[item][0] == workdates[item+1][0]:
#           print(workdates[item][0])
#     except KeyError:
#         pass

def convert_to_24_hour(time_str):
    time_str = time_str.replace(" ", "")
    print(time_str)
    hour, minute = map(int, time_str[:-2].split(':'))
    if time_str.endswith('PM') and hour != 12:
        hour += 12
    elif time_str.endswith('AM') and hour == 12:
        hour = 0
    return f"{hour:02d}:{minute:02d}:00"

def formatDate(workdates):
    shifts = {}     
    count = 0       
    for item in workdates:
        count += 1
        date_string = workdates[item][0]
        date_obj = datetime.strptime(date_string, "%a %m/%d/%Y")
        iso_date_string = date_obj.strftime("%Y-%m-%dT")
        time_string_start = workdates[item][1][0:8]
        time_string_end = workdates[item][1][10:18]
        time_string_start = convert_to_24_hour(time_string_start)
        time_string_end = convert_to_24_hour(time_string_end)
        
        if count not in shifts:
            shifts[count] = []
        
        shift_start = iso_date_string + time_string_start
        shift_end = iso_date_string + time_string_end
        shifts[count].append(shift_start)
        shifts[count].append(shift_end)
    return shifts



print(formatDate(shifts))


# Submit the form if necessary
# form.submit()

# Close the WebDriver
# driver.quit()