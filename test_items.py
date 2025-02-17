import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_stepik(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    browser.find_element(By.CSS_SELECTOR , 'span a.btn.btn-default')
    