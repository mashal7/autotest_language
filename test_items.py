import time
from selenium.webdriver.common.by import By

def test_for_checking_language(browser):

    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(url)

    locator = '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]'
    time.sleep(10)

    assert browser.find_element(By.XPATH, locator), 'Ошибка! Проблема с кнопкой'
    print('Успешно! Кнопка есть')