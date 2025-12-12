import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from dotenv import load_dotenv

# ------------------------------- Setup ---------------------------------------------
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)

load_dotenv()

ACCOUNT_EMAIL = os.getenv("ACCOUNT_EMAIL")
ACCOUNT_PASSWORD = os.getenv("ACCOUNT_PASSWORD")
GYM_URL = "https://appbrewery.github.io/gym/"

driver.get(GYM_URL)

# ------------------------------- Retry Function ---------------------------------------------
def retry(func, retries=7, description=None):
    for i in range(retries):
        print(f"Trying {description}. Attempt: {i + 1}")
        if func():
            break

# ------------------------------- Login ---------------------------------------------
wait = WebDriverWait(driver, timeout=3)

# Wait for login button and click on it.
def login():
    login_button = wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
    login_button.click()

    email_input = wait.until(ec.presence_of_element_located((By.NAME, "email")))
    email_input.clear()
    email_input.send_keys(ACCOUNT_EMAIL)

    password_input = driver.find_element(By.NAME, value="password")
    password_input.clear()
    password_input.send_keys(ACCOUNT_PASSWORD)

    driver.find_element(By.ID, value="submit-button").click()
    try:
        wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))
    except TimeoutException:
        return False
    else:
        return True

retry(login, description="Login")

# ------------------------------- Book the upcoming Tuesday class ---------------------------------------------
booked_count = 0
waitlist_count = 0
already_booked_count = 0
to_book_classes = []
days = driver.find_elements(By.CSS_SELECTOR, value="div[id^='day-group-']")
def book_class():
    global days
    global booked_count
    global waitlist_count
    global already_booked_count
    global to_book_classes
    for day in days:
        if "tue" in day.get_attribute("id") or "thu" in day.get_attribute("id"):
            class_to_book = day.find_element(By.CSS_SELECTOR, "div[id$='1800']")
            class_button = class_to_book.find_element(By.TAG_NAME, "button")
            class_name = class_to_book.find_element(By.TAG_NAME, "h3").text
            date = day.find_element(By.TAG_NAME, "h2").text
            if class_button.text == "Booked":
                print(f"✓ Already Booked: {class_name} on {date}")
                already_booked_count += 1
            elif class_button.text == "Waitlisted":
                print(f"Already on waitlist: {class_name} on {date}")
                already_booked_count += 1
            elif class_button.text == "Join Waitlist":
                class_button.click()
                if class_button.text != "Waitlisted":
                    return False
                print(f"Joined waitlist for: {class_name} on {date}")
                waitlist_count += 1
            else:
                class_button.click()
                if class_button.text != "Booked":
                    return False
                print(f"✓ Booked: {class_name} on {date}")
                booked_count += 1
            #Format date:
            if "Tomorrow" in date:
                date = date.replace(" (", "")
                date =  date.replace(")", "")
                date = date.replace("Tomorrow", "")
            hour = ' '.join(class_to_book.find_element(By.CSS_SELECTOR, value="p[id^='class-time-spin-']").text.split()[1:])
            date = date+', '+hour
            if (class_name, date) not in to_book_classes:
                to_book_classes.append((class_name, date))
    return True
retry(book_class, description="Booking class")


print("--- BOOKING SUMMARY ---")
print(f"Classes booked: {booked_count}")
print(f"Waitlists joined: {waitlist_count}")
print(f"Already booked/waitlisted: {already_booked_count}")
print(f"Total classes processed: {booked_count+waitlist_count+already_booked_count}")
# ------------------------------- Verify Class bookins on the "My Bookings" Page ---------------------------------------------
def get_my_bookings():
    try:
        driver.find_element(By.ID, "my-bookings-link").click()
        wait.until(ec.presence_of_all_elements_located((By.ID, "confirmed-bookings-title")))
    except TimeoutException:
        return False
    else:
        return True

retry(get_my_bookings, description="Get My Bookings")

list_booked_classes = []
booked_classes = driver.find_elements(By.CSS_SELECTOR, "div[id^='booking-card-booking_']")
try:
    for booked_class in booked_classes:
        class_name = booked_class.find_element(By.TAG_NAME, "h3").text
        date = ' '.join(booked_class.find_element(By.TAG_NAME, "p").text.split()[1:])
        list_booked_classes.append((class_name, date))
except ec.NoSuchElementException:
    pass

verified_count = 0
print("--- VERIFYING ON MY BOOKINGS PAGE ---")
for class_to_check in to_book_classes:
    if class_to_check in list_booked_classes:
        verified_count += 1
        print(f"✓ Verified: {class_to_check[0]}")

print("--- VERIFICATION RESULT ---")
print(f"Expected: {len(to_book_classes)} Bookings")
print(f"Found: {verified_count} Bookings")
if verified_count == len(to_book_classes):
    print("✅ SUCCESS: All bookings verified!")
else:
    print(f"❌ MISMATCH: Missing {to_book_classes - verified_count} bookings")
