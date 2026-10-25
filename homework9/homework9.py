# open browser
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
try:
    driver.get("https://demowebshop.tricentis.com/")

    # by NAME - search field
    search_by_name = driver.find_element(By.NAME, "q")
    print("'q' element is found")

    # by NAME - radiobuttons
    search_by_name2 = driver.find_elements(By.NAME, "pollanswers-1")
    print(f"'pollanswers-1' elements are found in count: {len(search_by_name2)}")

    # by TAG_NAME - a (links)
    search_by_tag_name = driver.find_elements(By.TAG_NAME, "a")
    print(f"'a' elements are found in count: {len(search_by_tag_name)}")

    # by CLASS_NAME - add to cart buttons
    search_by_class_name = driver.find_elements(By.CLASS_NAME, "product-box-add-to-cart-button")
    print(f"CLASS elements 'product-box-add-to-cart-button' are found in count: {len(search_by_class_name)}")

    # by ID - newsletter subscribe button
    search_by_id = driver.find_element(By.ID, "newsletter-subscribe-button")
    print("'newsletter-subscribe-button' element is found")

    # by CSS_SELECTOR - tags
    search_by_css_selector_tags = driver.find_elements(By.CSS_SELECTOR, "div")
    print(f"'div' tags are found in count: {len(search_by_css_selector_tags)}")

    # by CSS_SELECTOR - classes
    search_by_css_selector_classes = driver.find_elements(By.CSS_SELECTOR, ".actual-price")
    print(f"'actual-price' classes are found in count: {len(search_by_css_selector_classes)}")

    # by CSS_SELECTOR - ID
    search_by_css_selector_id = driver.find_element(By.CSS_SELECTOR, "#vote-poll-1")
    print("'vote-poll-1' id is found")

    # by attribute - radiobutton
    radio_button_exact = driver.find_element(By.CSS_SELECTOR, 'input[type="radio"][value="1"]')
    print("'radio-button-1' element is found")

    # by attribute - slideshow
    slideshow_exact = driver.find_element(By.CSS_SELECTOR, 'a[class="nivo-imageLink"]')
    print("'slideshow_exact' element is found")

finally:
    driver.quit()