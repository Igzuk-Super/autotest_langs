import pytest
from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

#@pytest.mark.parametrize('link')
def test_find_add_to_basket_button(browser):
    browser.get(link)
    curr_language = browser.execute_script('return window.navigator.language || window.navigator.userLanguage')
    if 'fr' in curr_language:
        time.sleep(30)
    find_buttons = browser.find_elements(By.CSS_SELECTOR, 'button.btn-add-to-basket')
    assert len(find_buttons) > 0, 'Не найдена кнопка добавления в корзину'
    assert len(find_buttons) < 2, 'Кнопка добавления в корзину не уникальна'
