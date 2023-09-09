from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://sonikaecuador.com/")
search_box = driver.find_element(by=By.CSS_SELECTOR, value="#search_widget > form > input.ui-autocomplete-input")
search_box.send_keys("Guitarra Clasica")

search_button = driver.find_element(by=By.CSS_SELECTOR, value="#search_widget > form > button")
search_button.click()

guitarras = driver.find_elements(By.CSS_SELECTOR, "#js-product-list > div.products.row > div")


for card in guitarras:
    try:
        Nombre_del_producto = card.find_element(By.CSS_SELECTOR, "div > div.product-description > h2").text
        Precio = card.find_element(By.CSS_SELECTOR, "div > div.product-description > div > span.price").text
        Estado = card.find_element(By.CSS_SELECTOR, "div > div.product-description > div > span:nth-child(5)").text
        print(Nombre_del_producto)
        print(Precio)
        print(Estado)

        coche_actual = {
            "Nombre_del_producto": Nombre_del_producto,
            "Precio": Precio,
            "Estado": Estado
        }

        print("________________________________________________________")
    except Exception as e:
        print(e)
        print("________________________________________________________")


driver.close()
