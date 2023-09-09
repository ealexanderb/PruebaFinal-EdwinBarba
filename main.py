from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://sonikaecuador.com/154-guitarras")
search_box = driver.find_element(by=By.CSS_SELECTOR, value="#search_widget > form > input.ui-autocomplete-input")
search_box.send_keys("Guitarra Clasica")

search_button = driver.find_element(by=By.CSS_SELECTOR, value="#search_widget > form > button")
search_button.click()

vehicle_cards = driver.find_elements(By.CSS_SELECTOR, "#js-product-list > div.products.row > div")


for card in vehicle_cards:
    try:
        title = card.find_element(By.CSS_SELECTOR, "div > div.product-description > h2").text
        kms_y_city = card.find_element(By.CSS_SELECTOR, "div > div.product-description > div > span.price").text
        price = card.find_element(By.CSS_SELECTOR, "div > div.product-description > div > span:nth-child(5)").text
        print(title)
        print(kms_y_city)
        print(f"${price}")

        coche_actual = {
            "title": title,
            "kms_y_city": kms_y_city,
            "price": price
        }

        print("++++++++++++++++++++++++++++++++")
    except Exception as e:
        print(e)
        print("++++++++++++++++++++++++++++++++")


driver.close()
