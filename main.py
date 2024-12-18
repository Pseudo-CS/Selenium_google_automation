from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

form_url = "https://forms.gle/WT68aV5UnPajeoSc8"

# Example data to be filled in
form_data = {
    "Full Name": "Saandeep CS",
    "Contact Number": "9113532561",
    "Email ID": "saandeepcs010@gmail.com",
    "Full Address": "Ashok Nagar, Bangalore",
    "Pin Code": "560025",
    "Date of Birth": "10/01/2004",
    "Gender": "Male", 
    "Code": "GNFPYC"
}


# Initialize the WebDriver
driver = webdriver.Chrome()

try:
    driver.get(form_url)
    wait = WebDriverWait(driver, 10)
    
    # Find all input fields with the class `whsOnd zHQkBf`
    input_fields = driver.find_elements(By.CLASS_NAME, "whsOnd.zHQkBf")
    
    # Fill in the input fields sequentially
    input_fields[0].send_keys(form_data["Full Name"])  # Full Name
    input_fields[1].send_keys(form_data["Contact Number"])  # Contact Number
    input_fields[2].send_keys(form_data["Email ID"])  # Email ID
    input_fields[3].send_keys(form_data["Pin Code"])  # Pin Code
    input_fields[4].send_keys(form_data["Date of Birth"])  # Date of Birth
    input_fields[5].send_keys(form_data["Gender"])  # gender
    input_fields[6].send_keys(form_data["Code"])  # Code
    
    # Fill in the address (textarea with class `KHxj8b tL9Q4c`)
    address_field = driver.find_element(By.CLASS_NAME, "KHxj8b.tL9Q4c")
    address_field.send_keys(form_data["Full Address"])
    
    # Submit the form (adjust based on the submit button, e.g., a button or span)
    submit_button = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Submit"]')))
    submit_button.click()
    
    print("Form submitted successfully!")
finally:
    time.sleep(15)  
    driver.quit()

