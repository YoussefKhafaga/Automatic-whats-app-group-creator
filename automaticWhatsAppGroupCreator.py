from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Initialize WebDriver (Firefox)
driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com")

# Wait for user to scan QR code manually
input("Scan QR Code and press Enter to continue\n")

# Click on "New chat" button
new_chat_button = driver.find_element(By.XPATH, "//div[@title='New chat']")
new_chat_button.click()
time.sleep(1)

# Read the CSV file into a DataFrame
df = pd.read_csv('csvfile.csv')
names = df['Name']


# Wait for the new chat input field to appear
new_chat_input = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div[1]/span/div/span/div/div[2]/div[1]/div[2]/div/span")
new_chat_input.click()
time.sleep(1)

for name in names:

# Clear the input field and enter the contact name
    new_chat_input = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div[1]/span/div/span/span/div/div/div[1]/div/div/div[2]/input")
    new_chat_input.clear()
    new_chat_input.send_keys(name)  # Replace with the contact name
    time.sleep(1)  # Give WhatsApp time to update search results

    # Click on the contact to add to the group
    try:
        contact_element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div[1]/span/div/span/span/div/div/div[2]/div/div/div/div/div")  # Replace with the contact name
        contact_element.click()
    except:
        print("Cannot find the contact " + name + " This could not be a whats app number")
    time.sleep(1)

# Click on the "Create Group" button
create_group_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div[1]/span/div/span/span/div/div/span/div/span")
create_group_button.click()
time.sleep(2)

# Enter the group name
groupName = "جروب تجربة"
group_name_input = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div[1]/span/div/span/span/div/div/div[1]/div[2]/div/div[2]/div[3]/div/div[1]")
group_name_input.send_keys(groupName)  # Replace with your desired group name
time.sleep(2)

# Click the "Create" button to create the group
create_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div[1]/span/div/span/span/div/div/span/div/div")
create_button.click()